from setuptools import setup, find_packages, Extension
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "readme.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.2"
DESCRIPTION = "form for tkinter"
LONG_DESCRIPTION = "create a form for tkinter from a base dictionary"

# Setting up
setup(
    name="tkinter_form",
    version=VERSION,
    author="JohanEstebanCuervo",
    author_email="<jecuervoch@unal.edu.co>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires='>=3.6',
    packages=find_packages(),
    install_requires=["tk"],
    keywords=[
        "tkinter",
        "form",
        "form tkinter",
        "tkinter interface",
        "simple tkinter",
        "tkform",
        "tk form",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    license="MIT",
    url="https://github.com/JohanEstebanCuervo/tkinter_form",
)
