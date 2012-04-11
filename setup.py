import os
from ez_setup import use_setuptools

use_setuptools()

from setuptools import setup, find_packages

APP_NAME = "AirbrakePy"
VERSION = "1.0.0b2"
SOURCE_URL = "http://github.com/pulseenergy/airbrakepy"

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def writeVersion():
    metadata_py = open('airbrakepy/metadata.py', 'w')
    content = """
# GENERATED BY setup.py DO NOT EDIT OR CHECKIN
app_name='%(app_name)s'
version='%(version)s'
source_url='%(source_url)s'
    """
    try:
        metadata_py.write(content % {'app_name': APP_NAME, 'version': VERSION, 'source_url': SOURCE_URL})
    finally:
        metadata_py.close()

writeVersion()

setup(
    name="AirbrakePy",
    version=VERSION,
    packages=find_packages(),
    install_requires=["xmlbuilder >= 0.9, < 1.0"],
    author="Tim Meighen",
    author_email="tim at pulseenergy dot com",
    maintainer="Pulse Energy",
    description="Airbrake notifier for Python logging framework",
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: System :: Logging",
        "License :: OSI Approved :: Apache Software License",
        ],
    license="Apache License 2.0",
    keywords="airbrake python logging",
    url=SOURCE_URL,
    download_url=SOURCE_URL,
    zip_safe=True
)
