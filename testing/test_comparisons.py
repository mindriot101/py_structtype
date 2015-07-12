import inspect
from structtype import Struct
import pytest


@pytest.fixture
def struct():
    return Struct("a", "b")


def test_equality_operator(struct):

    class Subclass(struct):
        pass

    a = Subclass(a=10, b=20)
    b = Subclass(a=10, b=20)
    assert a == b
