#from setuptools import setup
from distutils.core import setup

setup(
    name = 'cater',
    packages=['cater','shareBox'],
<<<<<<< HEAD
    version = '2.0',  # Ideally should be same as your GitHub release tag varsion
=======
    version = '1.1',  # Ideally should be same as your GitHub release tag varsion
>>>>>>> 8864ab3e387b5b3d1a9d0208cd3e3f7fe83b2752
    description='A TCP based file sharing application',
    author='Ravi Prakash',
    author_email='ravi.cs20@iiitmk.ac.in',
    url='https://github.com/ravi-prakash1907/cater', # github source url
<<<<<<< HEAD
    download_url = 'https://github.com/ravi-prakash1907/cater/archive/refs/tags/v2.0.tar.gz',
    long_descp = 'README.md',
    keywords = ['v2.0', 'cater'],
=======
    download_url = 'https://github.com/ravi-prakash1907/cater/archive/refs/tags/v1.1.tar.gz',
    long_descp = 'README.md',
    keywords = ['v1.1', 'cater'],
>>>>>>> 8864ab3e387b5b3d1a9d0208cd3e3f7fe83b2752
    classifiers=[
    'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable" ---- the current state of this package
    'License :: OSI Approved :: MIT License',   # picking a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',    
  ],
)
