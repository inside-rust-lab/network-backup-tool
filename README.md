# Network Backup Tool (nbtool)

A simple Python CLI tool that simulates backing up configuration files from network devices.
This project was built to practice core Python concepts while modeling a realistic network automation workflow.

The tool reads a device inventory, connects to devices, retrieves configuration data, and saves timestamped backups locally.

---

# Features

* Backup a single device
* Backup all devices in the inventory
* List devices in the inventory
* List unique vendors
* Simulated device connection failures
* Retry logic for connection attempts
* Timestamped configuration backups
* CLI interface using `argparse`
* Password input hidden with `getpass`

---

# Project Structure

```
network-backup-tool/
│
├── main.py               # CLI entrypoint
├── device.py             # NetworkDevice class
├── backup_manager.py     # Backup logic and inventory loading
├── devices.json          # Device inventory
├── backups/              # Saved configuration backups
├── configs/              # Mock configuration files 
└── README.md
```

---

# Example Inventory

`devices.json`

```
[
  {
    "hostname": "R1",
    "ip": "10.0.0.1",
    "vendor": "cisco"
  },
  {
    "hostname": "R2",
    "ip": "10.0.0.2",
    "vendor": "juniper"
  },
  {
    "hostname": "R3",
    "ip": "10.0.0.3",
    "vendor": "juniper"
  }
]
```

---

# Example Conf file

`configs/R1.conf`

```
hostname R1
!
interface GigabitEthernet0/0
 description Link to Juniper Router
 ip address 10.0.0.1 255.255.255.252
 no shutdown
!
ip route 0.0.0.0 0.0.0.0 10.0.0.2
```

---

# Installation

Clone the repository:

```
git clone <repo-url>
cd network-backup-tool
```

Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

---

# Usage

## Backup All Devices

```
python3 main.py -a
```

Example output:

```
Backing up all devices
Attempting to connect to R1...
Connection established
Config was saved as ./backups/R1_03-10-26_23:36:29.conf
Disconnecting...
Disconnect successful
```

---

## Backup a Single Device

```
python3 main.py -b R1
```

Example:

```
Backing up: R1
Attempting to connect to R1...
Connection established
Config was saved as ./backups/R1_03-10-26_23:37:03.conf
```

---

## List All Devices

```
python3 main.py -l
```

Example output:

```
Listing all devices:

Hostname: R1
IP: 10.0.0.1
Vendor: cisco

Hostname: R2
IP: 10.0.0.2
Vendor: juniper
```

---

## List Vendors

```
python3 main.py -v
```

Example:

```
Listing all vendors:
{'cisco', 'juniper'}
```

---

# How It Works

1. The CLI parses user arguments using `argparse`.
2. Device inventory is loaded from `devices.json`.
3. Each device is represented by a `NetworkDevice` object.
4. The tool attempts to connect to the device.
5. Configuration data is retrieved (simulated).
6. The configuration is written to the `backups/` directory with a timestamped filename.

Example backup filename:

```
R1_03-10-26_23:36:29.conf
```

---

# Python Concepts Practiced

This project intentionally exercises common Python fundamentals:

* Classes and object-oriented design
* Lists, dictionaries, and sets
* Functions and modules
* Loops and conditional logic
* File I/O
* JSON parsing
* CLI argument parsing with `argparse`
* Error handling with `try/except`
* Hidden password input using `getpass`
* Basic automation workflow design

---

# Possible Improvements

Future enhancements could include:

* Parallel device backups using `ThreadPoolExecutor`
* YAML-based inventory
* Vendor filtering (e.g., backup only Juniper devices)
* Logging to a file using the `logging` module
* Real SSH connections using libraries like Netmiko
* Case-insensitive hostname matching
* Packaging the tool as an installable Python CLI

---

# Purpose of the Project

This project was created as a hands-on way to refresh Python skills and explore patterns commonly used in:

* Network automation
* DevOps tooling
* Infrastructure scripting

The design intentionally mirrors real automation workflows used to manage network devices at scale.
