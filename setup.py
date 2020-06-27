from setuptools import setup
from os.path import join, dirname

setup(
    name='workingtitle',
    version='0',
    license='MIT',
    requires_python='>=3.7', 
    long_description_content_type="text/markdown",
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",],

    install_requires=[
        'aiohttp',
        'aiofiles']
)