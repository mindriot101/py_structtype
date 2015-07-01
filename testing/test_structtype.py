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


def test_constructor_args(struct):

    class SubClass(struct):
        pass

    s = SubClass(15, 25)

    assert s.a == 15 and s.b == 25


def test_constructor_kwargs(struct):

    class SubClass(struct):
        pass

    s = SubClass(a=10, b=20)

    assert s.a == 10 and s.b == 20
