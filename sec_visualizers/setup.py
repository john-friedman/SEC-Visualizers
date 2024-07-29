from setuptools import setup, find_packages

from pathlib import Path
long_description = Path("../readme.md").read_text()

setup(
    name="sec_visualizers",
    author="John Friedman",
    version="0.009",
    description = "A package to visualize SEC filings",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/john-friedman/SEC-Visualizers",
    install_requires=[
        'flask',
    ],
    packages=find_packages(),
    include_package_data=True,
)