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
print(socket.getaddrinfo('0.0.0.0', 80))
print(socket.getaddrinfo('0.0.0.0', 80)[0])
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

print('Listening on', addr)

def get_servo_degree(request,key_string):
    index = request.find(key_string) + len(key_string)
    if request[index].isdigit():
        offset = 1
        if request[index+1].isdigit():
            offset = 2
            if request[index+2].isdigit():
                offset = 3
        degree = int(request[index:index+offset])
        print(degree)
    return degree

# Listen for connections
while True:
    try:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        # print('Content = %s' % str(request))
        request = str(request)
        
        index_servo_base = request.find('servo_base=') + len('servo_base=')
        if request[index_servo_base].isdigit():
            offset = 1
            if request[index_servo_base+1].isdigit():
                offset = 2
                if request[index_servo_base+2].isdigit():
                    offset = 3
            deg_servo_base = int(request[index_servo_base:index_servo_base+offset])
            print(deg_servo_base)
        
            servo_base.rotateDeg(deg_servo_base)
            
        index_servo_vertical = request.find('servo_vertical=') + len('servo_vertical=')
        if request[index_servo_vertical].isdigit():
            offset = 1
            if request[index_servo_vertical+1].isdigit():
                offset = 2
                if request[index_servo_vertical+2].isdigit():
                    offset = 3
            deg_servo_vertical = 180 - int(request[index_servo_vertical:index_servo_vertical+offset])
            print(deg_servo_vertical)
            servo_vertical.rotateDeg(deg_servo_vertical)
        
        index_servo_forward = request.find('servo_forward=') + len('servo_forward=')
        if request[index_servo_forward].isdigit():
            offset = 1
            if request[index_servo_forward+1].isdigit():
                offset = 2
                if request[index_servo_forward+2].isdigit():
                    offset = 3
            deg_servo_forward = int(request[index_servo_forward:index_servo_forward+offset])
            print(deg_servo_forward)
            servo_forward.rotateDeg(deg_servo_forward)

        index_end_effector = request.find('end_effector=') + len('end_effector=')
        if request[index_end_effector].isdigit():
            offset = 1
            if request[index_end_effector+1].isdigit():
                offset = 2
                if request[index_end_effector+2].isdigit():
                    offset = 3
            deg_end_effector = int(request[index_end_effector:index_end_effector+offset])
            print(deg_end_effector)
            end_effector.rotateDeg(deg_end_effector)    
        
        # Load html and replace with current data 
        response = get_html('index.html')
        try:
            response = response.replace('slider_value_servo_base', str(deg_servo_base))
            response = response.replace('slider_value_servo_vertical', str(deg_servo_vertical))
            response = response.replace('slider_value_servo_forward', str(deg_servo_forward))
            response = response.replace('slider_value_end_effector', str(deg_end_effector))

        except Exception as e:
            response = response.replace('slider_value_servo_base', '0')
            response = response.replace('slider_value_servo_vertical', '0')
            response = response.replace('slider_value_servo_forward', '0')
            response = response.replace('slider_value_end_effector', '0')           
        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.send(response)
        conn.close()
    except OSError as e:
        conn.close()
        s.close()
        print('Connection closed')

