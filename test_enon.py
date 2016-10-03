"""
Withstand the test of time.
"""

from itertools import permutations

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
    assert enon['test'] is enon
    assert enon[1] is enon
    assert enon[-1:3:-2] is enon


def test_setitem():
    enon[1] = 'test'
    enon['test'] = 'test'


def test_get_set_attr():
    assert enon.test is enon
    enon.test = 'test'
    assert enon.test is enon


def test_call():
    args = (1, 'two', range(3))
    kwargs = {'four': set([4])}
    assert enon(*args, **kwargs) is enon
    other_enon = Enon()
    other_enon_result = other_enon(*args, **kwargs)
    assert (other_enon is other_enon) and (other_enon is not enon)


def test_contains():
    assert 'test' not in enon
    assert 1 not in enon


def test_append():
    enon.append(1)


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


def test_comps():
    operable = (
        set(),
        -1, 0, 1,
        -1.5, 0.0, 1.5,
        '', 'test',
        list(), tuple(),
    )
    for val in operable:
        for left, right in permutations([val, enon], 2):
            assert not (left == right)
            assert not (left < right)
            assert not (left <= right)
            assert not (left > right)
            assert not (left >= right)


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
