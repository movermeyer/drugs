import unittest
from mock import MagicMock

from ..utils import (
    _classproperty,
    _cached,
    classproperty,
    cached_classproperty,
    cached_property,
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

    def test_cached_method(self):
        class A(object):
            @_cached
            def x(self_):
                return self.heavy_method()

        obj = A()
        self.assertEqual(obj.x(), "method")
        self.heavy_method.assert_called_once_with()
        self.assertEqual(obj.x(), "method")
        self.assertEqual(obj.x(), "method")
        self.assertEqual(self.heavy_method.call_count, 1)

    def test_cached_classmethod(self):
        class A(object):
            @classmethod
            @_cached
            def x(cls):
                return self.heavy_method()

        self.assertEqual(A.x(), "method")
        self.heavy_method.assert_called_once_with()
        self.assertEqual(A.x(), "method")
        self.assertEqual(A.x(), "method")
        self.assertEqual(self.heavy_method.call_count, 1)

    def test_cached_property(self):
        class A(object):
            @cached_property
            def x(self_):
                return self.heavy_method()
        obj = A()
        self.assertEqual(obj.x, "method")
        self.heavy_method.assert_called_once_with()
        self.assertEqual(obj.x, "method")
        self.assertEqual(obj.x, "method")
        self.assertEqual(self.heavy_method.call_count, 1)

    def test_cached_classproperty(self):
        class A(object):
            @cached_classproperty
            def x(cls):
                return self.heavy_method()

        self.assertEqual(A.x, "method")
        self.heavy_method.assert_called_once_with()
        self.assertEqual(A.x, "method")
        self.assertEqual(A.x, "method")
        self.assertEqual(self.heavy_method.call_count, 1)
