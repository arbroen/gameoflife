# -*- coding: utf8 -*-
from setuptools import setup, find_packages
from pathlib import Path


SETUP_DIR = Path.cwd()
README_FILE = SETUP_DIR / "README.md"
PYTHON_VERSION = SETUP_DIR / "runtime.txt"
META_FILE = SETUP_DIR / "src" / "shine_on_life" / "__version__.py"


def get_requirements(filename):
    return open('requirements/' + filename).read().splitlines()


about = {}
# Get the project meta_data from __version__.py file
with META_FILE.open(mode="r", encoding="utf-8") as f:
    exec(f.read(), about)

# Get the long description from the README file
with README_FILE.open(mode="r", encoding="utf-8") as f:
    long_description = f.read()

# Get the long description from the README file
with PYTHON_VERSION.open(mode="r", encoding="utf-8") as f:
    python_version = f.read().strip()


setup(
    name=about["__project__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    author="Jeroen",
    author_email="",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["tests"]),
    install_requires=get_requirements("default.txt"),
    package_data={},
    data_files=[],
    entry_points={  # Optional
        "console_scripts": [
            "shine=shine_on_life.start:cmd_line"]
    },
    project_urls={},
)
