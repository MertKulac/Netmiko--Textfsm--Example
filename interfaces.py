from netmiko import Netmiko
from pyats_parser import parser

con = Netmiko(host = '192.168.10.1',
              username = 'username',
              password = 'password',
              port = 22,
              device_type = 'cisco_xr',
              timeout = 160,
              verbose = False)

show_version  = con.send_command('show interface description')

results = parser.parse(show_version,"show interface description","nxos")

#print(len(results["interfaces"]))

for key,value in results.items():
        for key1,value1 in value.items():
                for key2,value2 in value1.items():
                        if value2 == "up":
                                print(key1)
