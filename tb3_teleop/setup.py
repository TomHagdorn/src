from setuptools import setup

package_name = 'tb3_teleop'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tom',
    maintainer_email='T.Hagdorn@wzl.rwth-aachen.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop = tb3_teleop.teleop:main',
            'auto = tb3_teleop.auto:main',
            'test = tb3_teleop.test:main',
            'apriltags = tb3_teleop.apriltags:main',
        ],
    },
)
