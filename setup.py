from setuptools import setup, find_packages

setup(
    name='guiapp',
    version='0.1.0',
    package_dir={'':'guiapp'},
    py_modules=['testprog', 'app', 'sort'],
    packages=find_packages(where="guiapp"),
    install_requires=[
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'testprog = testprog:func',
        ],
    },
)