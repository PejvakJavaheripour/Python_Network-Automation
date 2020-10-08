from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

# username = input('Enter Your Username: ')
# password = getpass()

with open('06-determine_device_types/commands_file_switch') as f:
  commands_list_switch = f.read().splitlines()

with open('06-determine_device_types/commands_file_router') as f:
  commands_list_router = f.read().splitlines()

with open('06-determine_device_types/commands_file_phy_router') as f:
  commands_list_phy_router = f.read().splitlines()

with open('06-determine_device_types/devices_file') as f:
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

  try:
    net_connect = ConnectHandler(**ios_devices)
  except(AuthenticationException):
    print('Authentication failures: ' + ip_address_of_devices)
    continue
  except(NetMikoTimeoutException):
    print('Timeout to device: ' + ip_address_of_devices)
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

  # Types of devices
  list_versions = [ 'C1900-UNIVERSALK9-M', 
                    'C3750-ADVIPSERVICESK9-M',
                    'C2600-ADVSECURITYK9-M'   
                  ]
  
  # Check software versions
  for software_ver in list_versions:
    print('Checking for ' + software_ver)
    output_version = net_connect.send_command('show version')
    int_version = 0 # Reset integer value
    int_version = output_version.find(software_ver)
    if int_version > 0:
      print ('Software version found: ' + software_ver)
      break
    else:
      print('Did not find (' + software_ver + ') !!!')
  if software_ver == 'C1900-UNIVERSALK9-M':
    print('Running ' + software_ver + ' commands:')
    output = net_connect.send_config_set(commands_list_phy_router)
  elif software_ver == 'C3750-ADVIPSERVICESK9-M':
    print('Running ' + software_ver + ' commands:')
    output = net_connect.send_config_set(commands_list_switch)
  elif software_ver == 'C2600-ADVSECURITYK9-M':
    print('Running ' + software_ver + ' commands:')
    output = net_connect.send_config_set(commands_list_router)
  
  print(output)
