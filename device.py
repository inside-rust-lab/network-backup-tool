class NetworkDevice:
    def __init__(self, hostname, ip, vendor):
        self.hostname = hostname
        self.ip = ip
        self.vendor = vendor

    def connect():
        '''
        connect the device and have a percentage of failure
        maybe have a file with "configs" 
        '''

    def get_config():
        # pull config from device

    def disconnect():
        # disconnect from the device

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