from setuptools import setup, find_packages

setup(name='trustar',
      version='0.0.1',
      author='TruSTAR Technology Inc.',
      url='https://github.com/trustar/trustar-python',
      description='Python SDK for the TruSTAR REST API',
      author_email='support@trustar.co',
      license='MIT',

      # package source directory
      # package_dir={'': 'trustar'},
      # packages=find_packages('trustar'),
      packages=find_packages(),
      use_2to3=True
      )
