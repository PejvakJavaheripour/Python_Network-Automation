from netmiko import ConnectHandler

with open('03-configure_multiple_devices/commands_file') as f:
  commands_list = f.read().splitlines()

with open('03-configure_multiple_devices/devices_file') as f:
  devices_list = f.read().splitlines()

for devices in devices_list:
  print ('Connecting to device: ' + devices)
  ip_address_of_devices = devices
  
  ios_devices = {
    'device_type': 'cisco_ios',
    'ip': ip_address_of_devices,
    'username': 'pejvak',
    'password': 'cisco' 
  }

  net_connect = ConnectHandler(**ios_devices)
  output = net_connect.send_config_set(commands_list)
  print(output)