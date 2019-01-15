import setuptools

setuptools.setup(
    name='rocket-build',  
    version='0.1.0',
    entry_points = {
        'console_scripts': ['rocket-build=rocketbuild.__main__:main'],
    },
    packages=setuptools.find_packages()
 )