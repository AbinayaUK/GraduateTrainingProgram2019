from setuptools import setup,find_packages

setup(
    name='calcegg',
    version='1.0.0',
    packages=find_packages(execute=['*tests*']),

)