"""
>>> d = StrKeyDict0([('2', 'two'), ('4', 'four')])
>>> d['2']
'two'
>>> d[4]
'four'
>>> d[1] # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
KeyError: '1'
>>> d.get('2')
'two'
>>> d.get(4)
'four'
>>> d.get(1, 'N/A')
'N/A'
>>> 2 in d
True
>>> 1 in d
False
"""

class StrKeyDict0(dict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    
    def __contains__(self, __key: object) -> bool:
        return __key in self.keys() or str(__key) in self.keys()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
