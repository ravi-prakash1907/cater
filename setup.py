#from setuptools import setup
from distutils.core import setup

setup(
    name = 'cater',
    packages=['cater','shareBox'],
    version = '0.1',  # Ideally should be same as your GitHub release tag varsion
    description='A TCP based file sharing application',
    author='Ravi Prakash',
    author_email='ravi.cs20@iiitmk.ac.in',
    url='github.com/ravi-prakash1907/cater.git', # github source url
    download_url = 'github.com/ravi-prakash1907/cater/archive/refs/tags/v1.0.tar.gz',
    keywords = ['v0.1', 'cater'],
    classifiers = []
)
