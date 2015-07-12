import inspect
from structtype import Struct
import pytest


def test_equality_operator(DefaultSubclass):

    a = DefaultSubclass(a=10, b=20)
    b = DefaultSubclass(a=10, b=20)
    assert a == b


def test_less_than_operator(DefaultSubclass):

    a = DefaultSubclass(a=9, b=15)
    b = DefaultSubclass(a=10, b=20)
    assert a < b
