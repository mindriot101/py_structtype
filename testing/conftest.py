import pytest
from structtype import Struct


@pytest.fixture
def struct():
    return Struct("a", "b")


@pytest.fixture
def DefaultSubclass(struct):

    class SubClass(struct):
        pass

    return SubClass
