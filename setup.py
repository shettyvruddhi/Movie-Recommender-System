from setuptools import setup

with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read()

AUTHOR_NAME = 'VRUDDHI SHETTY'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='shetty@gmail.com',
    description='A small example package for movies recommendation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package=[SRC_REPO],
    python_requires='>=3.8',
    install_requires=LIST_OF_REQUIREMENTS,

)