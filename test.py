import asyncio
from ble_scanner.BLEScanner import BLEScanner

async def main():
   # Create a BLEScanner instance
    scanner = BLEScanner(target_mac="E2:15")  # Replace the MAC
    # await scanner.initialize()

if __name__ == "__main__":
    asyncio.run(main())
