"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = ["sqlalchemy==1.*", "pyomniscidb>=5.5.2", "pyomnisci>=0.27.0"]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

with open("requirements_dev.txt", "r") as f:
    dev_requirements = [line for line in f.read().split("\n") if line.strip()]
dev_requirements += requirements

setup(
    author="OmniSci",
    author_email="community@omnisci.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="OmniSciDB driver for SQLAlchemy",
    install_requires=requirements,
    extras_require={"dev": dev_requirements},
    license="Apache 2.0",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="sqlalchemy_omnisci",
    name="sqlalchemy-omnisci",
    packages=find_packages(include=["sqlalchemy_omnisci"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/omnisci/sqlalchemy-omnisci",
    version="0.1.0",
    zip_safe=False,
    entry_points={
        "sqlalchemy.dialects": [
            "omnisci = sqlalchemy_omnisci:OmnisciDialect",
        ]
    },
)
