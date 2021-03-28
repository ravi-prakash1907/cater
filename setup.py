from setuptools import setup

setup(
    name = 'cater', # pkg name
    version='0.1',
    description='A TCP based file sharing application',
    url='git@github.com:ravi-prakash1907/cater.git', # post the http "clone" link
    author='Ravi Prakash',
    author_email='ravi.cs20@iiitmk.ac.in',
    license='unlicense',
    packages=['cater'],
    zip_safe=False
)