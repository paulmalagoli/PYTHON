from scapy.all import Ether, IP
 
mac = Ether().src
ip = IP(dst="0.0.0.0").src
 
print("Mac: "+mac)
print("IP: "+ip)