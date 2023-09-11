import asyncio
from bleak import BleakScanner, AdvertisementData
import json
import argparse

class BLEScanner:
    def __init__(self, target_mac=None, continuous=True):
        self.target_mac = target_mac.lower().replace(":", "") if target_mac else None
        self.continuous = continuous
        self.scanner = None

    async def initialize(self):
        self.scanner = BleakScanner(detection_callback=self.detection_callback)  # Changed here
        if self.continuous:
            await self.continuous_scan()


    async def detection_callback(self, device, advertisement_data: AdvertisementData):
        if self.filter_by_mac(device):
            manufacturer_data = self.extract_manufacturer_data(advertisement_data)  # Changed here
            print(f"Manufacturer Data: {manufacturer_data}")

    @staticmethod
    def custom_serializer(o):
        if isinstance(o, (bytes, bytearray)):
            return o.hex()
        raise TypeError(f'Object of type {o.__class__.__name__} is not JSON serializable')

    @staticmethod
    def extract_metadata(device):
        metadata_dict = {}
        for key, value in device.metadata.items():
            formatted_value = json.dumps(value, default=BLEScanner.custom_serializer, indent=4)
            metadata_dict[key] = formatted_value
        return metadata_dict

    @staticmethod
    def extract_manufacturer_data(advertisement_data: AdvertisementData):
        manufacturer_data_dict = {}
        manufacturer_data = advertisement_data.manufacturer_data  # Changed here
        for key, value in manufacturer_data.items():
            key_hex = hex(key).replace("0x", "")
            manufacturer_data_dict[key_hex] = value.hex()
        return manufacturer_data_dict

    def filter_by_mac(self, device):
        if self.target_mac:
            device_mac = device.address.lower().replace(":", "")
            return self.target_mac.lower() in device_mac
        return True

    async def continuous_scan(self):
        await self.scanner.start()
        await asyncio.sleep(3600)  # Run for 1 hour, or until manually stopped

async def main():
    parser = argparse.ArgumentParser(description='BLE Scanner with Custom MAC Address')
    parser.add_argument('--mac', type=str, help='Specify the MAC address to scan for')
    args = parser.parse_args()

    scanner = BLEScanner(target_mac=args.mac)
    await scanner.initialize()

if __name__ == "__main__":
    asyncio.run(main())
