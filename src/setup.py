from setuptools import setup, find_packages

with open("requirements.txt", "r") as req_file:
    requirements = req_file.read().splitlines()

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="gptengineer",
    version="0.1",
    description="A version of gptengineer which can be used on iPhone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gptengineer",
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Operating System :: IOS :: IOS",
    ],
    python_requires='>=3.6',
)