# Network Backup Tool (nbtool)

A simple Python CLI tool that backs up configuration files from network devices.
This project was built to practice core Python concepts while modeling a realistic network automation workflow.

The tool reads a device inventory, connects to devices, retrieves configuration data, and saves timestamped backups locally.

---

# Features

* Backup a single device
* Backup all devices in the inventory
* List devices in the inventory
* List unique vendors
* Retry logic for connection attempts
* Timestamped configuration backups
* CLI interface using `argparse`
* Password input hidden with `getpass`

---

# Project Structure

```
network-backup-tool/
│
├── main.py               # Handles CLI args
├── nbtool                # CLI entrypoint
├── requirements.txt      # Dependencies
├── device.py             # NetworkDevice class
├── backup_manager.py     # Backup logic and inventory loading
├── devices.json          # Device inventory
├── backups/              # Saved configuration backups
└── README.md
```

---

# Example Inventory

`devices.json`

```
[
  {
    "hostname": "FW-LAB-01",
    "host": "10.0.0.1",
    "device_type": "juniper_junos"
  },
  {
    "hostname": "AD-LAB-01",
    "host": "10.0.0.2",
    "device_type": "adtran_os"
  },
  {
    "hostname": "SW-LAB-01",
    "host": "192.168.20.1",
    "device_type": "cisco_ios"
  }
]
```

---

# Quick Start

Required packages:

* Python3
* Git

Required Python3 modules:

* pip
* venv

```
git clone https://github.com/inside-rust-lab/network-backup-tool.git
cd network-backup-tool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./nbtool -l
```

# Usage

## Backup All Devices

```
nbtool -a
```

Example output:

```
Attempting to connect to SW-LAB-01...
Successfully connected to SW-LAB-01
Config was saved as ./backups/SW-LAB-01_03-12-26_08:09:23.conf
Disconnecting from SW-LAB-01...
Attempting to connect to FW-LAB-01...
Successfully connected to FW-LAB-01
Config was saved as ./backups/FW-LAB-01_03-12-26_08:09:26.conf
Disconnecting from FW-LAB-01...
```

---

## Backup a Single Device

```
nbtool -b SW-LAB-01
```

Example:

```
Attempting to connect to SW-LAB-01...
Successfully connected to SW-LAB-01
Config was saved as ./backups/SW-LAB-01_03-12-26_08:09:23.conf
Disconnecting from SW-LAB-01...
```

---

## List All Devices

```
nbtool -l
```

Example output:

```
Listing all devices:

Hostname: FW-LAB-01
Host: 10.0.0.1
Vendor: juniper_junos

Hostname: AD-LAB-01
Host: 10.0.0.2
Vendor: adtran_os

Hostname: SW-LAB-01
Host: 192.168.20.1
Vendor: cisco_ios
```

---

## List Vendors

```
nbtool -v
```

Example:

```
Listing all vendors:

{'juniper_junos', 'adtran_os', 'cisco_ios'}
```

---

# How It Works

1. The CLI parses user arguments using `argparse`.
2. Device inventory is loaded from `devices.json`.
3. Each device is represented by a `NetworkDevice` object.
4. The tool attempts to connect to the device.
5. Configuration data is retrieved.
6. The configuration is written to the `backups/` directory with a timestamped filename.

Example backup filename:

```
SW-LAB-01_03-12-26_08:09:23.conf
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
* Connection management and network device integration using `netmiko`
* Basic automation workflow design

---

# Possible Improvements

Future enhancements could include:

* Parallel device backups using `ThreadPoolExecutor`
* YAML-based inventory
* Vendor filtering (e.g., backup only Juniper devices)
* Logging to a file using the `logging` module
* Real SSH connections using libraries like Netmiko
* Packaging the tool as an installable Python CLI

---

# Purpose of the Project

This project was created as a hands-on way to refresh Python skills and explore patterns commonly used in:

* Network automation
* DevOps tooling
* Infrastructure scripting

The design intentionally mirrors real automation workflows used to manage network devices at scale.