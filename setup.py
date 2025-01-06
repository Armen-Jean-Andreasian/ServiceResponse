from setuptools import setup, find_packages

__version__ = "0.1"

setup(
    name='service_response',
    version='0.1',
    packages=find_packages(),
    author='Armen-Jean Andreasian',
    author_email='armen_andreasian@proton.me',
    license='Custom License',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    description='A library for managing git repositories in a directory.',
    url='https://github.com/Armen-Jean-Andreasian/ServiceResponse',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    python_requires=">=3.6",
)
