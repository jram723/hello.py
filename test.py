import socket
from datetime import datetime

from IPy import IP


def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)

out_file = ""

print("-" * 50)
print("    Project B Scanner        ")
print("    project By Ivan Ramirez  ")
print("    Created Sept 1, 2021     ")
print("-" * 50)

ipaddress = input('Enter target to scan: ')
converted_ip = check_ip(ipaddress)
print("time started: " + str(datetime.now()))
t1 = datetime.now()



def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        return '[+] Port' + str(port) + ' Is Open'
    except:
        return '[-] Port' + str(port) + ' Is Closed'





t2 = datetime.now()
total = t2 - t1
print("scanning complete in: ", total)


for port in range(1, 1025):
    result = scan_port(converted_ip, port)
    print(result, str(datetime.now()))
    time = datetime.now()
    out_file = open("test.txt", "a")
    out_file.write(str(time) + " \n " + str(result) + " \n " + str(total))
    out_file.close()