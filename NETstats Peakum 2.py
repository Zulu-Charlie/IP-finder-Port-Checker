
import socket
from requests import get
import whois

#IP abfrage
ip = get('https://api.ipify.org').text

print('My public IP address is: {}'.format(ip))

#port cheker
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('ip',10)) #in die 'ip' kommt die IP, hinter dem Komma der Port
if result == 0:
   print("Port ist offen")
else:
   print ("Port ist geschlossen")
sock.close()

#