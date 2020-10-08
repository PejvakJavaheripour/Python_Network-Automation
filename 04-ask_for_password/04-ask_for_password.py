from getpass import getpass
from netmiko import ConnectHandler

username = input('Enter Your Username: ')
password = getpass()

with open('commands_file') as f:
  commands_list = f.read().splitlines()

with open('devices_file') as f:
  devices_list = f.read().splitlines()

for devices in devices_list:
  print ('Connecting to device: ' + devices)
  ip_address_of_devices = devices
  ios_devices = {
    'device_type': 'cisco_ios',
    'ip': ip_address_of_devices,
    'username': username,
    'password': password 
  }

  net_connect = ConnectHandler(**ios_devices)
  output = net_connect.send_config_set(commands_list)
  print(output)