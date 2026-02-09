from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'centering_manager'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'srv'),
            glob('srv/*.srv')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nuc-lassie',
    maintainer_email='aditya.k.jyotis@gmail.com',
    description='Package to manage centering controller',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'centering_server = centering_manager.action_server_node:main',
        ],
    },
)