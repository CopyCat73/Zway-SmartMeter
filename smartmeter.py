import sys
import serial
import requests

zwayserver = 'http://192.168.0.1:8083'
username = 'admin'
password = 'yourpassword'

deviceurl= zwayserver +'/ZAutomation/api/v1/devices'
loginurl = zwayserver + '/ZAutomation/api/v1/login'
header = {'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json'}
form = '{"form": true, "login": "'+username+'", "password": "'+password+'", "keepme": false, "default_ui": 1}'

session = requests.Session()
response = session.post(loginurl,headers=header, data=form)
#response = session.get(deviceurl)

#print response.status_code
#print session.cookies

#Set COM port config
ser = serial.Serial()
ser.baudrate = 9600
ser.bytesize=serial.SEVENBITS
ser.parity=serial.PARITY_EVEN
ser.stopbits=serial.STOPBITS_ONE
ser.xonxoff=0
ser.rtscts=0
ser.timeout=20
ser.port="/dev/ttyUSB0"

try:
    ser.open()
except:
    sys.exit ("Error opening %s!"  % ser.name)      

p1_count=0
stack=[]

while p1_count < 20:
    p1_line=''
    try:
        p1_raw = ser.readline()
    except:
        sys.exit ("Unable to access serial port %s." % ser.name )      
    p1_str=str(p1_raw)
    p1_line=p1_str.strip()
    stack.append(p1_line)
    p1_count = p1_count +1

stack_count=0
while stack_count < 20:
   if stack[stack_count][0:9] == "1-0:1.8.1":
    sendvalue = ''
   elif stack[stack_count][0:9] == "1-0:1.8.2":
    sendvalue = ''
   elif stack[stack_count][0:9] == "1-0:2.8.1":
    sendvalue = ''
   elif stack[stack_count][0:9] == "1-0:2.8.2":
    sendvalue = ''
   elif stack[stack_count][0:9] == "1-0:1.7.0":
    sendvalue = str(int(float(stack[stack_count][10:17])*1000))
    response = session.get(deviceurl+'/SmartMeter_23/command/update?level='+sendvalue)
   elif stack[stack_count][0:9] == "1-0:2.7.0":
    sendvalue = str(int(float(stack[stack_count][10:17])*1000))       
    response = session.get(deviceurl+'/SmartMeter_24/command/update?level='+sendvalue)
   else:
    pass
   stack_count = stack_count +1

try:
    ser.close()
except:
    sys.exit ("Error closing %s!" % ser.name )      
