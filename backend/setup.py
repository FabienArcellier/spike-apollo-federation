from setuptools import setup, find_packages

setup(
    name='backend',
    version='1.0',
    packages=find_packages(exclude=["tests", "tests.*"]),
    license='',
    long_description='',
    classifiers= [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3'
    ],
    install_requires = [
        'ariadne',
        'uvicorn'
    ]
)