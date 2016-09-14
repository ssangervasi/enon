"""
Withstand the test of time.
"""

from enon import Enon, enon


def test_str():
    assert str(enon) is ''


def test_int():
    assert int(enon) == 0


def test_float():
    assert float(enon) == 0.0


def test_iter():
    count = 0
    for entry in enon:
        count += 1
    assert count == 0
    assert list(enon) == []


def test_len():
    assert len(enon) == 0


def test_getitem():
    assert enon['asdf'] is enon
    assert enon[1] is enon
    assert enon[-1:3:-2] is enon


def test_setitem():
    pass


def test_contains():
    return False


def test_append():
    pass


def test_context_manager():
    with enon as context:
        assert context is enon


def test_open():
    assert enon.open() is enon
    with enon.open() as context:
        assert context is enon


def test_close():
    assert not enon.close()


def test_write():
    enon.write('test')


def test_flush():
    enon.flush()


def test_ops():
    subable = (
        set(),  # Exclued from addable.
        -1, 0, 1,
        -1.5, 0.0, 1.5,
    )
    for val in subable:
        assert (enon - val) == val
        assert (val - enon) == val

    addable = subable[1:] + (
        '', 'test',
        list(), tuple(),
    )
    for val in addable:
        assert (enon + val) == val
        assert (val + enon) == val
