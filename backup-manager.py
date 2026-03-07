class BackupManager:

def load_devices():
    '''
    create a list of 'device' objects
    will have to get info from the devices.json file
    loop which parses the dictionaries in the list of devices in devices.json
    ''' 

def save_config():
    '''
    exports backups to backups/[hostname].cfg
    '''

def backup_device():
    '''
    argument takes a device name
    
    searches the list of devices objects, gets the config and calls the save_config() method
    '''

def backup_all():
    '''
    loops throuh the list of device objects and calls the backup_device() method
    '''
'''
questions:

does the backup_device() method connect to the device or the save_config()?
probably the backup_device() method?


devices.json:

[
  {
    "hostname": "core-sw1",
    "ip": "10.0.0.1",
    "vendor": "cisco"
  },
  {
    "hostname": "dist-sw1",
    "ip": "10.0.0.2",
    "vendor": "arista"
  }
]

responsibilities:

load_devices()
backup_device()
save_config()
backup_all()

workflow:

1 read devices.json
2 create NetworkDevice objects
3 connect to device
4 get config
5 save to backups/<hostname>.cfg

concepts:

file I/O
loops
calling class methods
'''