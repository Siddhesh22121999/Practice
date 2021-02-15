import unittest2
import methods

class TestClass(unittest2.TestCase):

    def test_add(self):
        result = methods.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(methods.add(10, 1), 11)

    def test_subtract(self):
        result = methods.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_divide(self):
        self.assertEqual(methods.divide(10, 2), 5)

        with self.assertRaises(ValueError):
            methods.divide(10, 0)
    def test_multiply(self):
        self.assertEqual(methods.multiply(12, -3), -36)

if __name__ == "__main__":
    unittest2.main()