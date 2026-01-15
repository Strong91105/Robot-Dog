from setuptools import find_packages
from setuptools import setup

setup(
    name='pc_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('pc_interfaces', 'pc_interfaces.*')),
)
