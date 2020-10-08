from netmiko import ConnectHandler

ios_devices = {
  'device_type': 'cisco_ios',
  'ip': '192.168.1.104',
  'username': 'pejvak',
  'password': 'cisco' 
}

net_connect = ConnectHandler(**ios_devices)
output = net_connect.send_command('sh ver')
print(output)