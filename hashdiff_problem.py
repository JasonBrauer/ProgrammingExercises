expected = {
  id: 9876,
  first_name: 'Tony',
  last_name: 'Soprano',
  account: {
    bank_name: 'Bank Of America',
    account_number: 12345
  }
}
'''
But the actual result of the calculation was:
'''

actual = {
  id: 20,
  first_name: 'Tony',
  account: {
    account_number: 12345,
    balance: 500
  }
}

'''
We would like to be able to compare the two structures in our tests, and know what were the specific differences between them. Write a helper, which is given two inputs (actual and expected), and outputs a list of all the diffs between them, using the following github-esque format:
'''

[
  [ '-', 'id',                  9876              ],
  [ '-', 'last_name',           'Soprano'         ],
  [ '-', 'account.bank_name',   'Bank Of America' ],
  [ '+', 'id',                  20                ],
  [ '+', 'account.balance',     500               ]
]

'''
UNIT TESTS
'''
import unittest

#####################
# Implement me!
#####################
def diff(actual, expected):
    return []


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