from setuptools import setup

from payzen import __version__


setup(
    name='payzen',
    version=__version__,
    description="Payzen API Client and utilities",
    author="Jurismarchés",
    author_email='contact@jurismarches.com',
    url='https://www.jurismarches.com',
    packages=[
        'payzen',
        'payzen.codes'
    ],
    install_requires=[
        'suds-jurko==0.6'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ])
