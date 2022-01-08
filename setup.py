#!/usr/bin/env python
from setuptools import setup

from lt3opencorpora import __version__

setup(
    name='LT3OpenCorpora',
    version=__version__,
    author='Danylo Halaiko',
    author_email='d9nich@pm.me',
    packages=['lt3opencorpora'],
    url='https://github.com/no-plagiarism/LT3OpenCorpora',
    description='Python script to convert Ukrainian morphological dictionary '
                'from LanguageTool project to OpenCorpora forma'
                'more than million lexemes',
    scripts=['bin/lt_convert.py', 'bin/lt_plot.py'],
    package_data={"lt3opencorpora": ["mapping.csv",
                                     "open_corpora_tagset.xml"]},
    license='MIT license',
    install_requires=[
        'blinker ~= 1.4',
        'requests==2.27.1',
    ],
    extras_require={
        'plot': ["pydot ~= 1.4.2"],
    },
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],
)
