from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name='ble_scanner',
    version='{{VERSION_PLACEHOLDER}}',
    author="John Doe",
    author_email="oashaikhe@gmail.com",
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

