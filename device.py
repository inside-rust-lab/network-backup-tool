import time
import random

class NetworkDevice:
    def __init__(self, hostname, ip, vendor):
        self.hostname = hostname
        self.ip = ip
        self.vendor = vendor

    def connect(self):
        print(f"Attempting to connect to {self.hostname}...")
        time.sleep(1)
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