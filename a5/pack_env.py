#!/usr/bin/env python3
import pkg_resources

packages = [
    "jupyterlab",
    "pandas",
    "numpy",
    "scikit-learn",
    "django",
    "tensorflow",
    "scipy",
    "matplotlib",
    "keras"
]

import sys
print(f"Python version:\n{sys.version}\n")


for package in packages:
    try:
        version = pkg_resources.get_distribution(package).version
        print(f"{package}: {version}")
    except pkg_resources.DistributionNotFound:
        print(f"{package}: not installed")