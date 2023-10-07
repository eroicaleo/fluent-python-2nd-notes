'''
>>> tt = (1, 2, (30, 40))
>>> hash(tt)
-3907003130834322577
>>> tl = (1, 2, [30, 40])
>>> hash(tl) # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
TypeError: unhashable type: 'list'
>>> tf = (1, 2, frozenset([30, 40]))
>>> hash(tf)
5149391500123939311
'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()
