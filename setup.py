from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import supplycrate

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='supplycrate',
    #version=supplycrate.__version__,
    version='0.0.1',
    url='https://bitbucket.org/Zivia/gw2-supply-crate/overview',
    license='MIT License',
    author='Troy Squillaci',
    tests_require=['pytest'],
    install_requires=[
        # TODO
    ],
    cmdclass={'test': PyTest},
    author_email='zivia@unm.edu',
    description='Python wrapper for the Guild Wars 2 API.',
    long_description=long_description,
    packages=['supplycrate'],
    include_package_data=True,
    platforms='any',
    test_suite='supplycrate.test.test_supplycrate',
    classifiers=[
        # TODO
    ],
    extras_require={
        'testing': ['pytest'],
    }
)