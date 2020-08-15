import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easyenc",
    version="0.0.2",
    author="dsnk",
    author_email="erick.8bld@gmail.com",
    description="An easy encryption module.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dsnk24/easy-enc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)