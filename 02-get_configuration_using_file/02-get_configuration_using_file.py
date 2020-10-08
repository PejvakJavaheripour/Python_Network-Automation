# =================================================================
# To give you an idea of what that means, add this to your code:

# import os
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))
# =================================================================

from netmiko import ConnectHandler

with open('02-get_configuration_using_file/commands_file') as f:
  commands_to_send = f.read().splitlines()

ios_devices = {
  'device_type': 'cisco_ios',
  'ip': '192.168.1.104',
  'username': 'pejvak',
  'password': 'cisco' 
}

all_devices = [ios_devices]

for devices in all_devices:
  net_connect = ConnectHandler(**devices)
  output = net_connect.send_config_set(commands_to_send)
  print (output)