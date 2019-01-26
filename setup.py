import setuptools

setuptools.setup(
    name='rocket-build',  
    version='0.1.0',
    entry_points = {
        'console_scripts': ['rocket-build=rocketbuild.main:main'],
    },
    packages=['rocketbuild']
 )