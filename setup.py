from setuptools import setup
from setuptools import find_packages

setup(
    name='consoleserialize',
    packages=[
        'factory',
        'factory/parsers'
    ],
    version='0.1.7.1',
    description='Console serialize',
    author='gor0b0t',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='/tests',
    scripts=['bin/consoleserialize']
)