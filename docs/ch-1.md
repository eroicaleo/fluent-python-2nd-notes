# Chapter -1 Misc Notes

* [Github link](https://github.com/fluentpython/example-code-2e)
* [pythontutor](https://pythontutor.com) to visualize the program.

## How to run doctest

* Example 1:

```python
"""
vector2d.py: a simplistic class demonstrating some special methods
It is simplistic for didactic reasons. It lacks proper error handling,
especially in the ``__add__`` and ``__mul__`` methods.
This example is greatly expanded later in the book.

Addition::

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

"""

class Vector:
  	# ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

```shell
 python vector.py -v
```

* Example 2

```python
>>> from vector import Vector
>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v1 + v2
Vector(4, 5)
>>> v = Vector(3, 4)
>>> abs(v)
5.0
>>> v * 3
Vector(9, 12)
>>> abs(v * 3)
15.0
```

```shell
python -m doctest -v vector.doctest
```

* How to add `...` if the output is too long:

  * Reference from [stackoverflow](https://stackoverflow.com/questions/17092215/how-enable-ellipsis-when-calling-python-doctest).

  ```python
  def foo():
      """
      >>> foo() # doctest: +ELLIPSIS
      hello ...
      """
      print("hello world")
  ```

  ```
  python -m doctest foo.py 
  ```

  * If we want to use `...` for all the tests

  ```python
  def foo():
      """
      >>> foo()
      hello ...
      """
      print("hello world")
  
  if __name__ == "__main__":
      import doctest
      doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
  ```

  ```shell
  python foo.py -v
  ```

* How to catch exception?

  * [Stackover anwser](https://stackoverflow.com/questions/12592/can-you-check-that-an-exception-is-thrown-with-doctest-in-python).

  ```python
  >>> c # doctest: +IGNORE_EXCEPTION_DETAIL
  Traceback (most recent call last):
  NameError: name 'c' is not defined
  ```

* How to do multiline in output when it's too long: adding `+NORMALIZE_WHITESPACE`

```python
>>> tshirts = [(color, size) for color in colors
...                          for size in sizes ]
>>> tshirts   # doctest: +NORMALIZE_WHITESPACE
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'),
('white', 'M'), ('white', 'L')]
```

* How to use verbose output

```python
doctest.testmod(verbose=True)
```

## Further Reading

### Chapter 1

* [Data model chapter](https://docs.python.org/3/reference/datamodel.html).
* [Python in a nutshell](https://www.oreilly.com/library/view/python-in-a/9781491913833/).
* Python Essential Reference
* Python Cook‐ book, 3rd ed.
* The Art of the Metaobject Protocol (Author's favorite)

## Cool Staff I Learned

### Chapter 1

* The use of `doctest`

### Chapter 2

* `timeit` module
* `hash` built-in
* `dis.dis` to check the byte code

## Typo

### Chapter 3

* pg 82
