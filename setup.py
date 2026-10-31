#!/usr/bin/env python3
"""
Setup script for ASCII Telescope
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ascii-telescope",
    version="1.0.0",
    author="Chris Vickers",
    description="Real-time solar observations in ASCII art",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ptxxdxxd/ascii_telescope",
    py_modules=["ascii_telescope"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Multimedia :: Graphics :: Viewers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ascii-telescope=ascii_telescope:run_stream",
        ],
    },
    keywords="astronomy solar nasa ascii art terminal visualization",
)
