import unittest
import pickle

from methodpickle.defer import defer, deferred, MethodStore

@deferred
def test_method(a, b):
    return a+b

@deferred
def another_method(x):
    return x*x

class DeferredClass(object):
    def __init__(self, value):
        self._x = value
    def calc(self, other):
        return (self._x * self._x) + (other * other)


def factorial(x):
    if x == 1: return 1
    return x * factorial(x-1)


class TestDefer(unittest.TestCase):

    def test_decorated(self):
        """Test deferred methods via decorator."""
        a = test_method(1,3)
        b = test_method(3,4)
        b.run()
        a.run()
        self.assertEqual(a.result, 4)
        self.assertEqual(b.result, 7)
        c = another_method(9)
        c.run()
        self.assertEqual(c.result, 81)

    def test_pickling(self):
        """Test pickling & unpickling a function invocation."""
        a = another_method(11)
        a_str = pickle.dumps(a)

        b = pickle.loads(a_str)
        b.run()
        self.assertEqual(b.result, 121)

    def test_straightup(self):
        """Test direct deferring of a function call."""
        d = defer(factorial, 4)
        r = d.run()
        self.assertEqual(d.result, 24)

    def test_classmethod(self):
        """Test deferring a class method."""
        x = DeferredClass(5)
        d = defer(x.calc, 1)
        result = d.run()
        self.assertEqual(d.result, 26)


class TestMethodStore(unittest.TestCase):

    def test_simple(self):
        """Test loading a method by name."""
        # We have not loaded this method in this file, so we're testing the
        # dynamic loading capability of the MethodStore here.
        loaded_method = MethodStore(module_name='methodpickle.test_helper',
                                    method_name='a_method')
        result = loaded_method.run(2, 3)
        self.assertEqual(result, 6)



if __name__ == '__main__':
    unittest.main()
