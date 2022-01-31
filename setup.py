#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cover-rest",
    version="0.0.1",
    author="Linus Behrens",
    author_email="linus@thebehrens.net",
    description="A REST API for coverage data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/cover-rest/restapi",
    packages=setuptools.find_packages(),
    license='MIT',
    keywords='rest api coverage continuous-integration',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.1',
    include_package_data=True,
    zip_safe=False,
    entry_points="""
    [console_scripts]
    analyse_pplog = analyse_pplog.jira_upload:main
    """,
    install_requires=[
        'flask_api>=-2.0.0'
    ],
)
