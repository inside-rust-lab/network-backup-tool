class NetworkDevice

'''
Attributes
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