[![PyPI version](https://badge.fury.io/py/types-wxpython.svg)](https://badge.fury.io/py/types-wxpython)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/types-wxpython)
![GitHub branch checks state](https://img.shields.io/github/checks-status/AlexionSoftware/types-wxpython/main)
![PyPI - Downloads](https://img.shields.io/pypi/dm/types-wxpython)
![GitHub](https://img.shields.io/github/license/AlexionSoftware/types-wxpython)

# Typing stubs for wxPython
Version: wxPython 4.2.0

This package contains typings stubs for [wxPython](https://pypi.org/project/wxPython/)

This package is not maintained by the maintainers of wxPython. This is made by users of wxPython.

Any help is always welcome.

## How it works
The base for the stubs is generated from [docs.wxpython.org](https://docs.wxpython.org/). It crawls the documentation looking for the Python-classes, functions and literals. This means changes in the documentation will also be applied in the stubs automatically, when they are regenerated.

We do not update anything in the `wx-stubs` folder manually. Everything is generated using the generator.

Execute `run.bat`/`run.sh` to generate the stubs.

### Overrides
Because we generated things based of online information, we sometimes has to resort to guessing, or sometimes the online documentation does not contain certain information. This fix these problems we can override the typing.

You will find the overrides in [`generator/overrides.py`](https://github.com/AlexionSoftware/types-wxpython/blob/main/generator/overrides.py).

In this file any parameter can be overriden by specifing the key and the params you want to overrides. You can change the typing of any class, function or literal. These are applied after the typing is collected from the online docs. 

To update the stubs run: `run.bat`. This will result in newly updated stubs in the `wx-stubs` folder.

### Missing
The online documentation can be incomplete, or sometimes we just don't seem to be able to comprehend the page. In these cases we can add typing to the stubs.

You will find this file in: [`generator/extras.py`](https://github.com/AlexionSoftware/types-wxpython/blob/main/generator/extras.py).

Here you can add any missing typing.

To update the stubs run: `run.bat`. This will result in newly updated stubs in the `wx-stubs` folder.

## Help is appreciated
We started this project because we use wxPython ourselves and code typing is really helpful to find bugs. 
But there is so much in wxPython. We fixed problems in the stubs as they came up for our code. This can result in things not working for your code. 

We decided to opensource the work we put in to create the best wxPython typing there is. 
We would like you help to. You can create an issue if you find problems with the typing. Or create a pull request if you fixed something.

### Guidelines
* You don't need to commit newly generated stubs in your PR. We will generate them when we publish a new version of the stubs.
