#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from probe.version import __version__

setup(name='probedesign',
      version=__version__,
      python_requires='>3.6',
      description='probe design',
      author='Ran zhou',
      author_email='ranzhou1005@gmail.com',
      url='https://github.com/luguodexxx/probe',
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ],
      keywords='RNAprobe',
      packages=find_packages(),
      install_requires=[
          'biopython'
      ],
      entry_points={
          'console_scripts': [
              'probedesign=probe.command_parser:main'
          ],
      },
      )
