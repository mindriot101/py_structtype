import inspect
from structtype import Struct
import pytest


def test_equality_operator(DefaultSubclass):

    a = DefaultSubclass(a=10, b=20)
    b = DefaultSubclass(a=10, b=20)
    assert a == b


class SubClass(Struct('a', 'b')):
    pass


@pytest.mark.parametrize('a,b,expected', [
    (SubClass(a=9,
              b=15), SubClass(a=10,
                              b=20), True),
    (SubClass(a=100,
              b=200), SubClass(a=10,
                               b=20), False),
])
def test_less_than_operator(a, b, expected):
    assert (a < b) == expected
