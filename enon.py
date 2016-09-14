"""
I'm glad you could make it. Please, sit down and have a drink.
"""


class Enon(BaseException, object):
    # Ensure nothing ever happens during construction.
    def __init__(self, *args, **kwargs):
        pass

    # Behave like a string
    def __str__(self):
        return ''

    def __unicode__(self):
        return u''

    # Behave like a number.
    def __int__(self):
        return 0

    def __float__(self):
        return 0.0

    # Behave like an iterable.
    def __iter__(self):
        return self

    def next(self, *args, **kwargs):
        raise StopIteration()

    def __len__(self):
        return 0

    # Behave like a collection.
    def __getitem__(self, *args, **kwargs):
        return enon

    def __setitem__(self, *args, **kwargs):
        pass

    def __contains__(self, *args, **kwargs):
        return False

    def append(self, *args, **kwargs):
        pass

    # Behave like a context manager.
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    # Behave like a file.
    def open(self, *args, **kwargs):
        return self

    def close(self):
        return 0

    def write(self, *args, **kwargs):
        pass

    def flush(self):
        pass

    # Behave like something that handles operators.
    def _ident(self, other):
        return other

    __add__ = _ident
    __radd__ = _ident
    __sub__ = _ident
    __rsub__ = _ident
    __mul__ = _ident
    __rmul__ = _ident
    __div__ = _ident
    __rdiv__ = _ident


# The global enon. Praise be unto him.
enon = Enon()
