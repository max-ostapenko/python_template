import unittest
from module_name.file_1 import add_numbers


class TestModuleFile1(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

        result = add_numbers(-1, 1)
        self.assertEqual(result, 0)

        result = add_numbers(0, 0)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
