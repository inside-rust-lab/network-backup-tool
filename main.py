'''
Needs to accept user credentials for login
Needs to accept what the user wants to do
    Backup all devices
    Backup a particular device
python main.py backup-all
python main.py backup R1
python main.py list-devices
python main.py show-vendors

use argparse
'''
from backupmanager import BackupManager
import argparse

def get_login_credentials():
    username = input("Username: ")
    password = input("Password: ")
    return (username, password)

parser = argparse.ArgumentParser("nbtool", "Backup network device(s)")
parser.add_argument("-b", "--backup", 
                    metavar="HOSTNAME", 
                    type=str, 
                    help="Backup the config of a host")
parser.add_argument("-a", "--backup-all",
                    action="store_true", 
                    help="Backup all devices in devices.json")
parser.add_argument("-l", "--list-devices", 
                    action="store_true",
                    help="List all devices configed in devices.json")
parser.add_argument("-v", "--list-vendors", 
                    action="store_true",
                    help="List the unique vendors for all devices configured in devices.json")

args = parser.parse_args()

if args.backup:
    get_login_credentials()
    print(f"Backing up: {args.backup}")

if args.backup_all:
    get_login_credentials()
    print("Backing up all devices")

if args.list_devices:
    print("Listing all devices")

if args.list_vendors:
    print("Listing all vendors")