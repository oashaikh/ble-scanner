from setuptools import setup, find_packages
import codecs
import os
import subprocess

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

remote_version = subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
print("remote_version: ", remote_version)
assert "." in remote_version, "Version number is not valid"


setup(
    name='ble_scanner',
    version=remote_version,
    author="Osama Ashaikh",
    author_email="oashaikh@gmail.com",
    description="BLE Beacon scanner",
    url = "https://github.com/oashaikh/ble-scanner",
    long_description_content_type="text/markdown",
    long_description=long_description,
    keywords=['pypi', 'BLE', 'python', 'scanner', 'beacon'],
    packages=find_packages(),
    install_requires=[
        'bleak',
        # other dependencies
    ],
)

