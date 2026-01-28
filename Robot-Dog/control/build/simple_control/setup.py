from setuptools import find_packages, setup

package_name = 'simple_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nuc-lassie',
    maintainer_email='mustermann@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'go_forward = simple_control.go_forward:main',
            'rotate_left_90 = simple_control.rotate_left_90:main',
            'rotate_left_90_odom = simple_control.rotate_left_90_odom:main',
        ],
    },
)
