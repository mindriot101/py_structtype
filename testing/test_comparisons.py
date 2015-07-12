import inspect
from structtype import Struct
import pytest


def test_equality_operator(default_subclass):

    a = default_subclass(a=10, b=20)
    b = default_subclass(a=10, b=20)
    assert a == b
