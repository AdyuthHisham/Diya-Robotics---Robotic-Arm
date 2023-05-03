# %% IMPORTANT %%
# Make sure the hotspot / wifi that is being connected to is set as private network
# and then disable the any built in firewall like windows security for private networks.
# Can be done in firewall & network protection settingg
# 

import network                     # import the network module to enable network configuration
import machine                     # import the machine module to interact with hardware pins
import socket                      # import the socket module to enable socket programming
from secrets import secrets        # import a configuration file with network credentials
import rp2                         # import rp2 module to set the Wi-Fi country code
import ubinascii                   # import ubinascii module to work with binary data in ASCII format
import time                        # import time module to use time-related functions

# create a class for Servo motor to rotate it to a specific angle
class Servo:
    def __init__(self, MIN_DUTY=300000, MAX_DUTY=2300000, pin=0, freq=50):
        self.pwm = machine.PWM(machine.Pin(pin))    # initialize PWM with specific pin
        self.pwm.freq(freq)                         # set the frequency of PWM signal
        self.MIN_DUTY = MIN_DUTY                    # set minimum duty cycle value for Servo motor
        self.MAX_DUTY = MAX_DUTY                    # set maximum duty cycle value for Servo motor
        
    def rotateDeg(self, deg):
        if deg < 0:                                      
            deg = 0
        elif deg > 180:
            deg = 180
        # Calculating the duty cycle based on the specified angle    
        duty_ns = int(self.MAX_DUTY - (self.MAX_DUTY-self.MIN_DUTY) * deg/180)
        # Setting the duty cycle for the servo motor
        self.pwm.duty_ns(duty_ns)

# Creating Servo objects for each servo motor
base_servo = Servo(pin=0)
right_link_servo = Servo(pin=1)
left_link_servo = Servo(pin=2)
end_effector = Servo(pin=3)


rp2.country('IN') # set Wi-Fi country code to IN (India)

wlan = network.WLAN(network.STA_IF) # Creating WLAN object for station mode
wlan.active(True)                   # activate the WLAN interface
# If you need to disable powersaving mode
# wlan.config(pm = 0xa11140)

# See the MAC address in the wireless chip OTP
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print('mac = ' + mac)

# Other things to query
# print(wlan.config('channel'))
# print(wlan.config('essid'))
# print(wlan.config('txpower'))

# Load login credentials from configuration/secrets file for to hide data
ssid = secrets['ssid']  # Getting Wi-Fi SSID from secrets module
pw = secrets['pw']      # Getting Wi-Fi password from secrets module

wlan.connect(ssid, pw)  # Connecting to the Wi-Fi network using the specified credentials

# Wait for connection with 10 second timeout
timeout = 10
while timeout > 0:
    # Checking if the status is not connecting or connected
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    timeout -= 1
    print('Waiting for connection...')
    time.sleep(1)

# Handle connection error
# Error meanings
# 0  Link Down
# 1  Link Join
# 2  Link NoIp
# 3  Link Up
# -1 Link Fail
# -2 Link NoNet
# -3 Link BadAuth

wlan_status = wlan.status() # Getting the status of the Wi-Fi connection


if wlan_status != 3:    # Checking if the status is not connected
    raise RuntimeError('Wi-Fi connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()    # Getting the IP address assigned by the DHCP server
    print('ip = ' + status[0])

# Function to read the contents of an HTML file and return it as a string 
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
        
    return html

# HTTP server with socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]         # Defines the address and port of the server.
s = socket.socket()                                     # Creates a new socket object
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Enables reuse of the socket address.
s.bind(addr)                                            # associates the socket with the server address and port
s.listen(1)                                             # starts listening for incoming connections
print('Listening on', addr)

# Function that extracts the degree value from a given key string in the HTTP request
def get_servo_input(request,key_string):
    index = request.find(key_string) + len(key_string)
    degree = 0
    if request[index].isdigit():
        offset = 1
        if request[index+1].isdigit():
            offset = 2
            if request[index+2].isdigit():
                offset = 3
        degree = int(request[index:index+offset])
        print(f'{key_string[:-1]} = {degree}')
    return degree

# Listen for connections
while True:
    try:
        # Continuously listens for incoming connections and establishes connection with client
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr)) 
        request = conn.recv(1024)
        # print('Content = %s' % str(request))
        request = str(request)
        
        deg_base_servo = get_servo_input(request,'base_servo=')
        base_servo.rotateDeg(deg_base_servo)
            
        deg_right_link_servo = get_servo_input(request,'right_link_servo=')
        right_link_servo.rotateDeg(180 - deg_right_link_servo)

        deg_left_link_servo = get_servo_input(request,'left_link_servo=')
        left_link_servo.rotateDeg(deg_left_link_servo)
            
        deg_end_effector = get_servo_input(request,'end_effector=')
        end_effector.rotateDeg(deg_end_effector)
        
        # Load html and replace with current data 
        response = get_html('index.html')
        try:
            response = response.replace('Last input:', 'Last input:'+str(
                [str(deg_base_servo),str(deg_right_link_servo),
                 str(deg_left_link_servo),str(deg_end_effector)]))
        except Exception as e:
            print(e)
            
        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.send(response)
        conn.close()
    except OSError as e:
        conn.close()
        s.close()
        print('Connection closed')




