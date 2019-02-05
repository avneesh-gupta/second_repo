import setuptools


with open("README.md", "r") as fh:
    desc = fh.read()

setuptools.setup(
    name='second_repo',
    version='10.0.1',
    scripts=['exe_file'],
    author="Avneesh Gupta",
    author_email="avneesh.gupta@paytm.com",
    description="A demo package",
    long_description="has two function long description",
    long_description_content_type="text/markdown",
    url="https://github.com/avneesh-gupta/second_repo",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3"])