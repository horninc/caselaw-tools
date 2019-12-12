#!/usr/bin/env python

from setuptools import setup

setup(name='caselaw-tools',
      version='0.1',
      description='Python toolkit for working with case law',
      url='https://github.com/horninc/caselaw-tools',
      author='Kristaps Horns',
      author_email='k.horns@ideaspool.nl',
      license='GPL-3.0',
      packages=['caselaw-tools'],
      install_requires=[
          'numpy',
          'pytz',
          'tqdm'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)