import inspect
from structtype import Struct
import pytest


@pytest.fixture
def struct():
    return Struct("a", "b")


def test_stuct_instance_is_class(struct):
    assert inspect.isclass(struct)


def test_instance_values_initialised_to_None(struct):

    class SubClass(struct):
        pass

    s = SubClass()

    assert s.a is None and s.b is None
