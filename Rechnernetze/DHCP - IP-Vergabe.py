from random import *

class DHCP:
    def __init__(self, name, ip, start, ende, adressraum):
        self.name = name
        self.ip = ip
        self.start = start
        self.ende = ende
        self.adressraum = adressraum
        self.range = []
        
    def ip_vergabe(self, client):
        ip_adresse = randint(self.start, self.ende)
        
        while ip_adresse in self.range:
            ip_adresse = randint(self.start, self.ende)
        
        self.range.append(ip_adresse)
        client.ip = ip_adresse
        print(f"Die IP-Adresse {ip_adresse} wurde an {client.name} vergeben.")
        
class Client:
    def __init__(self, name, ip = None):
        self.name = name
        self.ip = ip
        

dhcp = DHCP("DHCP-Sever", "192.168.178.0", 1, 255, 3)
client1 = Client("Client1")
client2 = Client("Client2")
client3 = Client("Client3")
client4 = Client("Client4")
client5 = Client("Client5")
dhcp.ip_vergabe(client1)
dhcp.ip_vergabe(client2)
dhcp.ip_vergabe(client3)
dhcp.ip_vergabe(client4)
dhcp.ip_vergabe(client5)

print("IP-Adresse von Client1 lautet:", client1.ip)
print("IP-Adresse von Client2 lautet:", client2.ip)
print("IP-Adresse von Client3 lautet:", client3.ip)
print("IP-Adresse von Client4 lautet:", client4.ip)
print("IP-Adresse von Client5 lautet:", client5.ip)