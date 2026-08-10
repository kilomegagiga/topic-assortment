from setuptools import setup, find_packages

setup(
    name="word_frequencies",
    version="22",

    author="kilomegagiga",
    author_email="kilomegagiga93@gmail.com",

    license="MIT",

    python_requires=">=3.6.15",

    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
