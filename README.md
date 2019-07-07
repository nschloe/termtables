<p align="center">
  <a href="https://github.com/nschloe/termtables"><img alt="termtables" src="https://nschloe.github.io/termtables/termtables.svg" width="60%"></a>
  <p align="center">The tables have termed.</p>
</p>

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/termtables/master.svg?style=flat-square)](https://circleci.com/gh/nschloe/termtables/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/termtables.svg?style=flat-square)](https://codecov.io/gh/nschloe/termtables)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)
[![awesome](https://img.shields.io/badge/awesome-yes-8209ba.svg?style=flat-square)](https://github.com/nschloe/termtables)
[![PyPi Version](https://img.shields.io/pypi/v/termtables.svg?style=flat-square)](https://pypi.org/project/termtables)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/termtables.svg?logo=github&label=Stars&logoColor=white&style=flat-square)](https://github.com/nschloe/termtables)
[![PyPi downloads](https://img.shields.io/pypi/dd/termtables.svg?style=flat-square)](https://pypistats.org/packages/termtables)


termtables is a lightweight Python package for pretty-printing tables on the command
line. Install with
```
pip3 install termtables --user
```
The code
```python
import termtables as tt
import numpy

numpy.random.seed(0)
data = numpy.random.rand(5, 2)

print(tt.to_string(data))
```
produces

![table1](https://nschloe.github.io/termtables/table1.png)

You can control border style, padding, alignment, and various other attributes. For
example,
```python
import termtables as tt

header = ["a", "bb", "ccc"]
data = [
    [1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]
]

print(tt.to_string(data, header=header, style=tt.styles.thin_double_ascii, padding=(0, 1), alignment="lcr"))
```
produces
```
+-----------------+-----------------+-----------------+
| a               |       bb        |             ccc |
+=================+=================+=================+
| 1               |        2        |               3 |
+-----------------+-----------------+-----------------+
| 613.23236243236 | 613.23236243236 | 613.23236243236 |
+-----------------+-----------------+-----------------+
```
See
[`test/test_termtables.py`](https://github.com/nschloe/termtables/blob/master/test/test_termtables.py)
for more examples.


### Testing

To run the termtables unit tests, check out this repository and type
```
pytest
```

### License

termtables is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
