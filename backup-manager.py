import json
import datetime
from device import NetworkDevice

class BackupManager:
    
    def load_devices(self):

      network_devices = [] # list of NetworkDevice objects
      
      with open("devices.json") as f:
          devices = json.load(f)
      
      for device in devices:
          device_object = NetworkDevice(device["hostname"], 
                                 device["ip"], 
                                 device["vendor"])
          network_devices.append(device_object)

      return network_devices
    
    def save_config(self, device):
      device.connect() # need to add a "try" feature
      config = device.get_config()

      current_time = str(datetime.datetime.now())
      file_name = f"backups/{device.hostname}" + current_time + ".conf"
      # write config to backups/[hostname][date/time].conf
      with open(file_name, "w") as file:
         file.write(config)
         print("Config was saved as backups/" + file_name)
      device.disconnect()
      return


    def backup_device(self, hostname):
        
      network_devices = self.load_devices()

      for device in network_devices:
         if device.hostname == hostname:
            self.save_config(device)
            return
      error_message = f"No device with hostname '{hostname}' was found"
      return error_message
      
    def backup_all(self):
        
      network_devices = self.load_devices()
        
      for device in network_devices:
          self.save_config(device)