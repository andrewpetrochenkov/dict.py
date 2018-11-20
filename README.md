[![](https://img.shields.io/pypi/pyversions/dict.svg?longCache=True)](https://pypi.org/pypi/dict/)
[![](https://img.shields.io/pypi/v/dict.svg?maxAge=3600)](https://pypi.org/pypi/dict/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/dict.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/dict.py/)

#### Install
```bash
$ [sudo] pip install dict
```

#### Features
*	**attribute-style access**
* 	**None** instead of **KeyError**
* 	safe **remove**
* 	jQuery like **methods chaining**

#### Classes

###### `dict.dict`

#### Examples
```python
>>> from dict import dict

>>> dict(k="v")["k"]
"v"

>>>  dict(k="v").k
"v"

>>> dict(k="v")["not_existing"]
None

>>> dict(k="v").not_existing
None

>>> dict(k="v").get("K",i=True) # case insensitive
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>