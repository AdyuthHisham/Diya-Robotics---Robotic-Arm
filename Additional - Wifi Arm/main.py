import network
import machine
import socket
from secrets import secrets
import rp2
import ubinascii
import time

class Servo:
    def __init__(self, MIN_DUTY=300000, MAX_DUTY=2300000, pin=0, freq=50):
        self.pwm = machine.PWM(machine.Pin(pin))
        self.pwm.freq(freq)
        self.MIN_DUTY = MIN_DUTY
        self.MAX_DUTY = MAX_DUTY
        
    def rotateDeg(self, deg):
        if deg < 0:
            deg = 0
        elif deg > 180:
            deg = 180
        duty_ns = int(self.MAX_DUTY - (self.MAX_DUTY-self.MIN_DUTY) * deg/180)
        self.pwm.duty_ns(duty_ns)

servo_base = Servo(pin=0)
servo_vertical = Servo(pin=1)
servo_forward = Servo(pin=2)
end_effector = Servo(pin=3)
    
ssid = secrets['ssid']
password = secrets['pw']

# ap = network.WLAN(network.STA_IF)
# ap.config(essid=ssid, password=password)
# ap.active(True)

# while ap.active() == False:
#   pass

# print('Connection successful')
# print(ap.ifconfig())

rp2.country('DE')

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# If you need to disable powersaving mode
# wlan.config(pm = 0xa11140)

# See the MAC address in the wireless chip OTP
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print('mac = ' + mac)

# Other things to query
# print(wlan.config('channel'))
# print(wlan.config('essid'))
# print(wlan.config('txpower'))

# Load login data from different file for safety reasons
ssid = secrets['ssid']
pw = secrets['pw']

wlan.connect(ssid, pw)

# Wait for connection with 10 second timeout
timeout = 10
while timeout > 0:
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

wlan_status = wlan.status()

if wlan_status != 3:
    raise RuntimeError('Wi-Fi connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

# Function to load in html page    
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
        
    return html

# HTTP server with socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
print('Listening on', addr)


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
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        # print('Content = %s' % str(request))
        request = str(request)
        
        deg_servo_base = get_servo_input(request,'servo_base=')
        servo_base.rotateDeg(deg_servo_base)
            
        deg_servo_vertical = get_servo_input(request,'servo_vertical=')
        servo_vertical.rotateDeg(180 - deg_servo_vertical)

        deg_servo_forward = get_servo_input(request,'servo_forward=')
        servo_forward.rotateDeg(deg_servo_forward)
            
        deg_end_effector = get_servo_input(request,'end_effector=')
        end_effector.rotateDeg(deg_end_effector)
        
        # Load html and replace with current data 
        response = get_html('index.html')
        try:
            response = response.replace('Last input:', 'Last input:'+str(
                [str(deg_servo_base),str(deg_servo_vertical),
                 str(deg_servo_forward),str(deg_end_effector)]))
        except Exception as e:
            print(e)
            
        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.send(response)
        conn.close()
    except OSError as e:
        conn.close()
        s.close()
        print('Connection closed')




