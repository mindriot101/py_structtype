import inspect
from structtype import Struct


def test_stuct_instance_is_class(struct):
    assert inspect.isclass(struct)


def test_instance_values_initialised_to_None(DefaultSubclass):

    s = DefaultSubclass()

    assert s.a is None and s.b is None


def test_constructor_args(instance):

    assert instance.a == 10 and instance.b == 20


def test_constructor_kwargs(instance):

    assert instance.a == 10 and instance.b == 20


def test_length(instance):

    assert len(instance) == 2


def test_to_list(instance):

    assert list(instance) == [10, 20]


def test_to_list_ordering(instance):

    assert list(instance) == [10, 20]


def test_dictionary_access(instance):

    assert (instance['a'] == 10) & (instance['b'] == 20)
