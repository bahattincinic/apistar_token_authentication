#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='apistar_token_auth',
    version='1.0',
    packages=['apistar_token_auth'],
    url='https://github.com/bahattincinic/apistar_token_authentication',
    license='MIT',
    description='Token Based Authentication for API Star',
    author='Bahattin Cinic',
    author_email='bahattincinic@gmail.com',
    install_requires=['apistar'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
