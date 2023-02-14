from setuptools import setup
from setuptools import find_packages

setup(
    name ='verbose' ,
    version='1.0.0',
    description='verbose',
    author='GrenManSK',
    install_requires=[],
    packages=find_packages(exclude=('tests*', 'testing*'))
)
