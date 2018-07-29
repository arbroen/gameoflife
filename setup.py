# -*- coding: utf8 -*-
from setuptools import setup, find_packages
from pathlib import Path


SETUP_DIR = Path.cwd()
README_FILE = SETUP_DIR / "README.md"
META_FILE = SETUP_DIR / "src" / "shine_on_life" / "__version__.py"


def get_requirements(filename):
    return open('requirements/' + filename).read().splitlines()


about = {}
# Get the long description from the README file
with open(README_FILE.absolute(), mode="r", encoding="utf-8") as f:
    long_description = f.read()

# Get the project meta_data from __version__.py file
with open(META_FILE.absolute(), mode="r", encoding="utf-8") as f:
    exec(f.read(), about)

setup(
    name=about["__project__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    author="ME",
    author_email="",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["tests"]),
    install_requires=get_requirements("default.txt"),
    extras_require={"test": get_requirements("test.txt")},
    package_data={},
    data_files=[],
    entry_points={  # Optional
        "console_scripts": [
            "shine=shine_on_life.start:cmd_line",
        ],
    },
    project_urls={},
)
