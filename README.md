<<<<<<< HEAD
# cater - 2.0 📤 
=======
# cater:1.1 📤
>>>>>>> 8864ab3e387b5b3d1a9d0208cd3e3f7fe83b2752

A Python library for instent file sharing, based on TCP.

## What's New  

<<<<<<< HEAD
Currently we are working to enhence the application and library with many new features.  
Following are out current aims:
1. Make the sharing speed more presentable at sender's end  
2. Compress/Extract feature if multiple files are to be shared  
3. Atomatically detect the Broadcast IP and lunch server smoothly
=======
In this final version (v1.1) of the `cater`, we have added following features:  

### 1. Auto IP Detection  
It is capable of detecting the IP-Address at its own in order to host the server while sharing the files at the sender's end. You won't be worry about finding you IP every time, when you are willing to share files quickly.  
It will also notify you the server's IP address so that receiver can easily connect.  

### 2. Better Speed Display  
The `cater` application will now be showing you the time taken to to complete the transfer in a far better way.  
Here, instead of showing the long length of time units, now sender will see time taken in seconds (up to 5 decimal places)  

>>>>>>> 8864ab3e387b5b3d1a9d0208cd3e3f7fe83b2752

## Usage 🎯

```python
from cater import cater

# Demo: cater.app()
cater.app()
```
<!-- See `examples` folder for more. -->

## Installation ⚠️

```sh
pip install cater
```  
or

```sh
pip install git+https://github.com/ravi-prakash1907/cater.git
```

## Requirements 🌌

Support for Python 3.0 and greater.

## Development 🛎️
Source code is in cater. Start editing and Happy contributing! 🌟

<!--
## Deployment to PyPI 💎

Based on descriptions from [here](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/), whenever project owner pushes a tagged commit to this Git repository remote on GitHub, GH workflow will publish it to PyPI.

And it'll publish any push to TestPyPI which is useful for providing test builds to repo's alpha users as well as making sure that your release pipeline remains healthy.

Manual deploy to TestPyPI:
```sh
python setup.py sdist bdist_wheel
twine upload -r testpypi dist/*
```
-->
## Running tests 🔥

```sh
python -m unittest
```

## Licence ✅

MIT. See LICENSE.md
<!--
## Version

Follows syntax vM.M.P
First is major and means not backwards compatible changes. Second is minor and means backwards compatible changes. 
Third is patch and means small backwards compatible changes.

The manual place of source of truth is at `cater/__init__.py`

Source: https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version

-->

## Authors ✏️

`cater` was written by [`Ravi Prakash`](http://ravi-prakash1907.gitlab.io/).


---  
