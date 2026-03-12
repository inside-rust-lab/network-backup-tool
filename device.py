import time
import random
from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException

class NetworkDevice:
    def __init__(self, hostname, host, device_type):
        self.hostname = hostname
        self.host = host
        self.device_type = device_type
        self.username = None
        self.password = None
        self.secret = None
        self.netconnect = None

    def connect(self):
        print(f"Attempting to connect to {self.hostname}...")
        connection_established = False
        connection_attempts = 0
        max_retries = 3

        while not connection_established and connection_attempts < max_retries:
            try:
                self.net_connect = ConnectHandler(
                    device_type=self.device_type,
                    host=self.host,
                    username=self.username,
                    password=self.password,
                    secret=self.secret
                )
                print(f"Successfully connected to {self.hostname}")
                connection_established = True
                return connection_established
            except NetmikoAuthenticationException:
                print("Invalid credentials")
                return connection_established
            except NetmikoTimeoutException:
                print(f"Unable to connect to {self.host}")
                connection_attempts += 1
            if connection_attempts >= max_retries:
                print(f"Unable to connect to {self.host} after {max_retries} attempts")


    def get_config(self):
        device_commands = {
            "cisco_ios": {
                "get_config": "show running-config",
            },
            "adtran_os": {
                "get_config": "show running-config",
            },
            "juniper_junos": {
                "get_config": "show configuration",
            }
        }
        if self.net_connect is not None:
            try:
                self.net_connect.enable()
                output = self.net_connect.send_command(device_commands[self.device_type]["get_config"])
                return output                    
            except:
                print(f"Unable to retrieve config file from {self.hostname}")
                return None

    def disconnect(self):
        print(f"Disconnecting from {self.hostname}...")
        self.net_connect.disconnect()
        return