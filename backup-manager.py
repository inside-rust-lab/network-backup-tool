import json
import datetime
from device import NetworkDevice

class BackupManager:
    
    def load_devices(self):

      network_devices = [] # list of NetworkDevice objects
      
      with open("devices.json") as f:
          devices_data = json.load(f)
      
      for device_info in devices_data:
          device_object = NetworkDevice(device_info["hostname"], 
                                 device_info["ip"], 
                                 device_info["vendor"])
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
      print(config)
      device.disconnect()
      return


    def backup_device(self, hostname):
        
      network_devices = self.load_devices()

      for device in network_devices:
         if device.hostname == hostname:
            self.save_config(device)
            return
      
      print("Hostname was not found")
      
    def backup_all(self):
        
      network_devices = self.load_devices()
        
      for device in network_devices:
          self.save_config(device)