import json

file_name = "device.json"

try: 
    with open(file_name) as f:
          devices = json.load(f)
except FileNotFoundError:
     print(f"File name {file_name} not found")

