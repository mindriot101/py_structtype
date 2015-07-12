import inspect
from structtype import Struct


def test_stuct_instance_is_class(struct):
    assert inspect.isclass(struct)


def test_instance_values_initialised_to_None(default_subclass):

    s = default_subclass()

    assert s.a is None and s.b is None


def test_constructor_args(default_subclass):

    s = default_subclass(15, 25)

    assert s.a == 15 and s.b == 25


def test_constructor_kwargs(default_subclass):

    s = default_subclass(a=10, b=20)

    assert s.a == 10 and s.b == 20


def test_length(default_subclass):

    s = default_subclass(a=10, b=20)

    assert len(s) == 2


def test_to_list(default_subclass):

    s = default_subclass(a=10, b=20)

    assert list(s) == [10, 20]


def test_to_list_ordering(default_subclass):

    s = default_subclass(b=20, a=10)

    assert list(s) == [10, 20]
