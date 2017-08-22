#!/usr/bin/env python3
from setuptools import setup

setup(name='resume',
      version='0.1',
      description='resume utility',
      author='Benjamin Ran',
      packages=['resume'],
      install_requires=[
          'pypandoc',
      ],
      entry_points={
          'console_scripts': ['resume=resume.cli:main']
      },
      zip_safe=False)
