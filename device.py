import time
import random
from netmiko import ConnectHandler

class NetworkDevice:
    def __init__(self, hostname, host, device_type, username, password, secret):
        self.hostname = hostname
        self.host = host
        self.device_type = device_type
        self.username = username
        self.password = password
        self.secret = secret

    def connect(self):
        print(f"Attempting to connect to {self.hostname}...")
        connection_established = False
        connection_attempts = 3

        while not connection_established and connection_attempts >= 0:
            random_failure = random.randint(1, 10)
            if connection_attempts <= 0:
                print(f"Unable to connect to {self.hostname}. Connection attempts expired")
                return connection_established
            if random_failure == 1:
                connection_attempts -= 1
                print("Connection failed\nRe-attempting connection...")
                time.sleep(2)
            else:
                print("Connection established")
                connection_established = True
                time.sleep(1)
        return connection_established

    def get_config(self):
        try:
            with open("configs/" + self.hostname + ".conf", "r") as file:
                config = file.read()
                return config
        except FileNotFoundError:
            print(f"Unable to retrieve config file file from {self.hostname}")
            return None

    def disconnect(self):
        print("Disconnecting...")
        time.sleep(2)
        print("Disconnect successful")
        return