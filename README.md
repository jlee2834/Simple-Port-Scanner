# Simple-Port-Scanner
A simple multithreaded TCP port scanner built in Python.

This tool scans a target host across a specified port range and identifies open ports along with associated services where possible.


## Features

- Multithreaded scanning for faster results
- Custom port range input
- Service detection using common port mappings
- Clean and readable output
- Lightweight and easy to run


## How It Works

The scanner attempts to establish a TCP connection to each port in the specified range using Python’s `socket` library.

If a connection is successful, the port is considered open and is reported.


## Requirements

- Python 3.x
- No external libraries required


## Usage

Run the script:

```bash
python port_scanner.py
