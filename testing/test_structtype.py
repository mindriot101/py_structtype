import inspect
from structtype import Struct

def test_stuct_instance_is_class():
    s = Struct("a", "b")
    assert inspect.isclass(s)
