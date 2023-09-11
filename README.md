
# BLE Scanner Library
[![Build and Publish to PyPI](https://github.com/oashaikh/ble-scanner/actions/workflows/python-publish.yml/badge.svg)](https://github.com/oashaikh/ble-scanner/actions/workflows/python-publish.yml)
## Description

This is a Python library for scanning BLE beacon devices. It is built on top of the Bleak library and provides an easy-to-use API for BLE scanning.

## Installation

You can install the package directly from the source code:


    python setup.py install


Or, you can use pip for installation:


    pip install ble_scanner


## Usage

Here's a quick example:


    import asyncio
    from ble_scanner.BLEScanner import BLEScanner

    async def main():
       # Create a BLEScanner instance
        scanner = BLEScanner(target_mac="E2:15")  # Replace the MAC
        await scanner.initialize()

    if __name__ == "__main__":
        asyncio.run(main())


For more advanced usage, refer to the documentation.

## Requirements

- Python 3.7+
- Bleak

## License

MIT License

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

