import inspect
from structtype import Struct
import pytest


def test_equality_operator(DefaultSubclass):

    a = DefaultSubclass(a=10, b=20)
    b = DefaultSubclass(a=10, b=20)
    assert a == b
