"""
Never regret anything.
"""

import os
from setuptools import find_packages, setup

PACKAGE_DIR = os.path.dirname(__file__)

with open(os.path.join(PACKAGE_DIR, 'README.md')) as readme:
    README = readme.read()

with open(os.path.join(PACKAGE_DIR, 'LICENSE')) as license:
    LICENSE = license.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='enon',
    version='0.1',
    packages=find_packages(),
    include_package_data=False,
    license=LICENSE,
    description='An object that does everything while doing nothing.',
    long_description=README,
    url='https://github.com/ssangervasi/enon',
    author='Sebastian Sangervasi',
    author_email='sorrymyemailadressisverylong@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
