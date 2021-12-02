# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('VERSION') as f:
    version = f.read()
with open('requirements.txt') as f:
    requirements = []
    for line in f.readlines():
        requirements.append(line)

setup(
    name='aoc',
    version=version,
    description='Advent Of Code',
    long_description='Advent Of Code',
    author='mattmulhern01@gmail.com',
    author_email='mattmulhern01@gmail.com',
    url='https://github.com/MattMulhern',
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=['setuptools', 'wheel'],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
