from setuptools import setup

setup(name='gendatafetcher',
      version='0.1',
      description='A small set of utility functions for using the UCSC mysql database and sequence API, focused around getting data relevant for graph-based genomes.',
      url='https://github.com/uio-cels/gendatafetcher',
      author='',
      author_email='',
      license='',
      packages=['gendatafetcher'],
      install_requires=['pymysql'],
      zip_safe=False)