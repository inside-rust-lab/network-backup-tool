import time
import random

class NetworkDevice:
    def __init__(self, hostname, ip, vendor):
        self.hostname = hostname
        self.ip = ip
        self.vendor = vendor

    def connect(self):
        # needs to accept hostname argument
        # needs failure handling if file does not exist
        print("Connecting...")
        time.sleep(1)
        connection_established = False

        while not connection_established:
            random_failure = random(1, 3)
            if random_failure == 1:
                print("Connection failed" + "\n" + 
                      "Re-attempting connection")
            else:
                print("Connection established")
                connection_established = True
                time.sleep(1)
                return connection_established

    def get_config(self):
        with open("configs/" + self.hostname + ".conf", "r") as file:
            config = file.read()
        print(config)

    def disconnect(self):
        print("Disconnecting...")
        time.sleep(2)
        print("Disconnect successful")
        return

'''
Attributes:
hostname
ip
vendor

methods:

connect()
get_config()
disconnect()

simulate behavior:

connect -> randomly fail sometimes
get_config -> return fake configuration text

example of fake config:
hostname core-sw1
interface eth0
 ip address 10.0.0.1
'''