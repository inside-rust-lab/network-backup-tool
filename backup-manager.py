import json
from device import NetworkDevice

class BackupManager:
    
    def load_devices(self):

      network_devices = [] # list of NetworkDevice objects
      
      with open("devices.json") as f:
          devices_data = json.load(f)
      
      for device_info in devices_data:
          device = NetworkDevice(device_info["hostname"], 
                                 device_info["ip"], 
                                 device_info["vendor"])
          network_devices.append(device)

      return network_devices
    
    def save_config(self):
      '''
      exports backups to backups/[hostname].cfg
      '''

    def backup_device(self):
        network_devices = self.load_devices()

    def backup_all():
        network_devices = self.load_devices()
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