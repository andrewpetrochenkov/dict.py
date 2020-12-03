<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/dict.svg?maxAge=3600)](https://pypi.org/project/dict/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/dict.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/dict.py/actions)

### Installation
```bash
$ [sudo] pip install dict
```

#### Features
*	**attribute-style access**
* 	**None** instead of **KeyError**
* 	safe **remove**
* 	jQuery like **methods chaining**

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

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
