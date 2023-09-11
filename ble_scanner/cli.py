# cli.py
import argparse
from ble_scanner import BLEScanner

# Argument parsing
parser = argparse.ArgumentParser(description='BLE Scanner with Custom MAC Address')
parser.add_argument('--mac', type=str, help='Specify the MAC address to scan for')
args = parser.parse_args()

# Usage as a standalone script
if __name__ == "__main__":
    scanner = BLEScanner(target_mac=args.mac)
