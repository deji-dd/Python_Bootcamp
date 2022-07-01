import unittest
import unit_testing


class MyTestCase(unittest.TestCase):
    def test_something(self):
        text = 'python'
        result = unit_testing.cap_text(text)
        self.assertEqual(result, 'Python')  # add assertion here
    def test_multiple_words(self):
        text = 'monty python'
        result = unit_testing.cap_text(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()
