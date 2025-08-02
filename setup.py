from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="py_xml_ccda",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "py_xml_ccda=py_xml_ccda.main:main",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
