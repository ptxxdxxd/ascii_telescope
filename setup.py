#!/usr/bin/env python3
"""
Setup script for Neural ASCII Telescope
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="neural-ascii-telescope",
    version="1.0.0",
    author="Neural ASCII Telescope Contributors",
    description="Real-time solar observations in ASCII art",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/neural-ascii-telescope",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Multimedia :: Graphics :: Viewers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "telescope=telescope:main",
        ],
    },
    keywords="astronomy solar nasa ascii art terminal visualization",
)
