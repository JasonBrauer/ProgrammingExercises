import unittest
from hashdiff_problem import diff


#####################
# Test harness
#####################
class TestDiffer(unittest.TestCase):
    def test_shallow(self):
        actual = {
            'apples': 3,
            'oranges': 4
        }

        expected = {
            'apples': 3,
            'grapes': 5
        }

        result = diff(actual, expected)
        self.assertEqual(len(result), 2)
        self.assertIn(['-', 'grapes', 5], result)
        self.assertIn(['+', 'oranges', 4], result)

    def test_different_values(self):
        actual = {
            'apples': 3,
            'oranges': 4
        }

        expected = {
            'apples': 3,
            'oranges': 5
        }

        result = diff(actual, expected)
        self.assertEqual(len(result), 2)
        self.assertIn(['-', 'oranges', 5], result)
        self.assertIn(['+', 'oranges', 4], result)

    def test_nested(self):
        actual = {
            'apples': 3,
            'oranges': {
                'navel': 5
            }
        }

        expected = {
            'apples': 3,
            'oranges': {
                'valencia': 4
            }
        }

        result = diff(actual, expected)
        self.assertEqual(len(result), 2)
        self.assertIn(['-', 'oranges.valencia', 4], result)
        self.assertIn(['+', 'oranges.navel', 5], result)

    def test_very_nested(self):
        actual = {
            'apples': 3,
            'oranges': {
                'bergamot': 3,
                'navel': {
                    'peaches': 1,
                    'apples': 3
                }
            }
        }

        expected = {
            'apples': 3,
            'oranges': {
                'bergamot': 3,
                'valencia': {
                    'pears': 2,
                    'oranges': 4
                }
            }
        }
        result = diff(actual, expected)
        self.assertEqual(len(result), 4)
        self.assertIn(['+', 'oranges.navel.peaches', 1], result)
        self.assertIn(['+', 'oranges.navel.apples', 3], result)
        self.assertIn(['-', 'oranges.valencia.pears', 2], result)
        self.assertIn(['-', 'oranges.valencia.oranges', 4], result)

    def test_comparing_object_to_value(self):
        actual = {
            'apples': 3,
            'oranges': 5
        }

        expected = {
            'apples': 3,
            'oranges': {
                'bergamot': 3,
                'valencia': {
                    'pears': 2,
                    'oranges': 4
                }
            }
        }

        result = diff(actual, expected)
        self.assertEqual(len(result), 4)
        self.assertIn(['+', 'oranges', 5], result)
        self.assertIn(['-', 'oranges.bergamot', 3], result)
        self.assertIn(['-', 'oranges.valencia.pears', 2], result)
        self.assertIn(['-', 'oranges.valencia.oranges', 4], result)

unittest.main(exit=False)