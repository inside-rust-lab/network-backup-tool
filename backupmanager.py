import json
import datetime
import os
from device import NetworkDevice

class BackupManager:
    def __init__(self):
        self.devices = self.load_devices()
    
    def load_devices(self):

        network_devices = []
        json_file_name = "devices.json"
        
        try:
            with open(json_file_name) as file:
                devices_json_data = json.load(file)
        except FileNotFoundError:
            print(f"File name {json_file_name} was not found")
            return
        except json.JSONDecodeError:
            print(f"JSON data in {json_file_name} is not formatted properly")
            return
        except PermissionError:
            print(f"You do not have permissions to open {json_file_name}")
            return
        
        for device in devices_json_data:
            device_object = NetworkDevice(device["hostname"], 
                                          device["ip"], 
                                          device["vendor"])
            network_devices.append(device_object)

        return network_devices
    
    def save_config(self, device):
        config = device.get_config()
        if config is None:
            return
        
        device.connect()

        directory = "backups"
        if not os.path.isdir(directory):
            os.makedirs(directory)

        current_time = datetime.datetime.now()
        current_time_formatted = current_time.strftime("%m-%d-%y_%H:%M:%S")
        file_name = f"{directory}/{device.hostname}-{current_time_formatted}.conf"
        with open(file_name, "w") as file:
            file.write(config)
            print(f"Config was saved as {directory}/{file_name}")
            
        device.disconnect()
        return

    def backup_device(self, hostname):
        
        network_devices = self.devices

        if network_devices is None:
            print(f"Unable to backup device")
            return

        for device in network_devices:
            if device.hostname == hostname:
                self.save_config(device)
                return

        print(f"No device with hostname '{hostname}' was found")
      
    def backup_all(self):
        
        network_devices = self.devices
        
        if network_devices is not None:
            for device in network_devices:
                self.save_config(device)
            return
        
        print("Unable to backup devices")