#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup


def get_file(fn):
    with open(fn) as fp:
        return fp.read()


# FIXME: This requires the requirements in requirements.txt, but we need to
# pull that in without the hashes.

setup(
    name='antenna',
    version='0.1.0',
    description="Collector v2 for Socorro",
    long_description=get_file('README.rst'),
    author="Will Kahn-Greene",
    author_email='willkg@mozilla.com',
    url='https://github.com/willkg/antenna',
    packages=[
        'antenna',
    ],
    package_dir={
        'antenna': 'antenna'
    },
    include_package_data=True,
    license="MPLv2",
    zip_safe=False,
    keywords='breakpad crash',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
)
