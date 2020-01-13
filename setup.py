#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='caselaw-tools',
      version='0.1',
      description='Python toolkit for working with case law',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/horninc/caselaw-tools',
      author='Kristaps Horns',
      author_email='k.horns@ideaspool.nl',
      license='GPL-3.0',
      packages=setuptools.find_packages(),
      install_requires=[
          "numpy", 
          "pytz",
          "tqdm",
          "pandas", 
          "requests", 
          "lxml", 
          "urllib", 
          "json", 
          "time"
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL-3.0 License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6')