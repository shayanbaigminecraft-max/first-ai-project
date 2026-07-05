from setuptools import find_packages, setup

setup(
    name="mcq-generator",
    version="0.0.1",
    author="Shayan Baig",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langchain-core",
        "langchain-mistralai",
        "streamlit",
        "python-dotenv",
        "pypdf2"
    ]
)