#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="nightswatch",
    version='0.0.1',
    author='jon',
    url='https://gitlab.lixinio.com/sre/sentry-nightswatch.git',
    description='A Sentry extension which send errors stats to NightsWatch',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='sentry nightswatch',
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'sentry>=9.0.0',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'sentry_nightswatch = sentry_nightswatch.plugin:NightsWatchPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "License :: OSI Approved :: MIT License",
    ]
)
