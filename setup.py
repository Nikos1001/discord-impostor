import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="DiscordImpostor",
    version="1.0.2",
    description="A python package for creating bots that pretend to be real users",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Nikos1001/discord-impostor",
    author="Nikos Plugachev",
    author_email="nikos@plugachev.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["DiscordImpostor"],
    include_package_data=True
)