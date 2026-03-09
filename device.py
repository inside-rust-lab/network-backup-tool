import time
import random

class NetworkDevice:
    def __init__(self, hostname, ip, vendor):
        self.hostname = hostname
        self.ip = ip
        self.vendor = vendor

    def connect():
        print("Connecting...")
        time.sleep(1)
        connection_established = False

        while(connection_established != True):
            random_failure = random.number(1, 3)
            if random_failure == 1:
                print("Connection failed" + "\n" + 
                      "Re-attempting connection")
            else:
                print("Connection established")
                connection_established = True
                time.sleep(1)
        return
        
        '''
        connecting
        sleep
        try/except
        connection success or failure
        connect the device and have a percentage of failure
        create a directory called configs/ which houses all the fake devices
        '''

    def get_config():
        # open the configs/[hostname].conf

    def disconnect():
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