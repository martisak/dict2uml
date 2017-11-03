#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages

PACKAGES = find_packages(where=".")
KEYWORDS = ["jupyter", "ipython", "uml", "plantuml", "dictionary"]
INSTALL_REQUIRES = []

if __name__ == "__main__":

    setup(name='dict2uml',
          version='1.0',
          description='Converts a Python dictionary to PlantUML',
          author='Martin Isaksson',
          author_email='martin@martisak.com',
          url='https://www.python.org/sigs/distutils-sig/',
          license='MIT',
          keywords=KEYWORDS,
          install_requires=INSTALL_REQUIRES,
          classifiers=[
              'Development Status :: 4 - Beta',
              'Intended Audience :: Science/Research',
              "Framework :: IPython",
              "License :: OSI Approved :: MIT License",
              "Operating System :: OS Independent",
              'Programming Language :: Python',
              "Programming Language :: Python :: 2.7"
          ],
          packages=PACKAGES,
          entry_points={
              'console_scripts': [
                  'dict2uml = dict2uml.__main__:main'
              ]
          },
          )
