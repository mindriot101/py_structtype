import pytest
from structtype import Struct


@pytest.fixture
def struct():
    return Struct("a", "b")


@pytest.fixture
def default_subclass(struct):

    class SubClass(struct):
        pass

    return SubClass
