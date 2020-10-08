from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

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

  try:
    net_connect = ConnectHandler(**ios_devices)
  except(AuthenticationException):
    print('Authentication failures: ' + ip_address_of_devices)
    continue
  except(NetMikoTimeoutException):
    print('Timeout to device: ') + ip_address_of_devices)
    continue
  except(EOFError):
    print('End of file while attemting device: ' + ip_address_of_devices)
    continue
  except(SSHException):
    print('SSH Issue. Are you sure SSH is enable for device: ' + ip_address_of_devices)
    continue
  except Exception as unknown_error:
    print('Some other error: ' + unknown_error)
    continue

  output = net_connect.send_config_set(commands_list)
  print(output)