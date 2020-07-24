import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skytempy",
    version="0.1",
    author="Renee Spiewak",
    author_email="respiewak@gmail.com",
    description="A simple package to calculate sky temperatures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/respiewak/skytempy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
