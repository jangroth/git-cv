from setuptools import setup, find_packages

setup(
    name="gitcv",
    version="0.1",
    packages=find_packages(),
    author="Jan Groth",
    license="MIT License",
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
