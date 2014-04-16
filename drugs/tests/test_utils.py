import unittest
from mock import MagicMock

from ..utils import (
    _classproperty,
    _lazy,
    classproperty,
    lazy_classproperty,
    lazy_property,
)


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.heavy_method = MagicMock(return_value="method")

    def test__classproperty(self):
        class A(object):
            @_classproperty
            @classmethod
            def x(cls):
                return "works"

        self.assertEqual(A.x, "works")

    def test_classproperty(self):
        class A(object):
            @classproperty
            def x(cls):
                return "works"

        self.assertEqual(A.x, "works")

    def test_lazy_method(self):
        class A(object):
            @_lazy
            def x(self_):
                return self.heavy_method()

        obj = A()
        self.assertEqual(obj.x(), "method")
        self.heavy_method.assert_called_once_with()
        self.assertEqual(obj.x(), "method")
        self.assertEqual(obj.x(), "method")
        self.assertEqual(self.heavy_method.call_count, 1)

    def test_lazy_classmethod(self):
        class A(object):
            @classmethod
            @_lazy
            def x(cls):
                return self.heavy_method()

        self.assertEqual(A.x(), "method")
        self.heavy_method.assert_called_once_with()
        self.assertEqual(A.x(), "method")
        self.assertEqual(A.x(), "method")
        self.assertEqual(self.heavy_method.call_count, 1)

    def test_lazy_property(self):
        class A(object):
            @lazy_property
            def x(self_):
                return self.heavy_method()
        obj = A()
        self.assertEqual(obj.x, "method")
        self.heavy_method.assert_called_once_with()
        self.assertEqual(obj.x, "method")
        self.assertEqual(obj.x, "method")
        self.assertEqual(self.heavy_method.call_count, 1)

    def test_lazy_classproperty(self):
        class A(object):
            @lazy_classproperty
            def x(cls):
                return self.heavy_method()

        self.assertEqual(A.x, "method")
        self.heavy_method.assert_called_once_with()
        self.assertEqual(A.x, "method")
        self.assertEqual(A.x, "method")
        self.assertEqual(self.heavy_method.call_count, 1)
