expected = {
  'id': 9876,
  'first_name': 'Tony',
  'last_name': 'Soprano',
  'account': {
    'bank_name': 'Bank Of America',
    'account_number': 12345
  }
}
'''
But the actual result of the calculation was:
'''

actual = {
  'id': 20,
  'first_name': 'Tony',
  'account': {
    'account_number': 12345,
    'balance': 500
  }
}

'''
We would like to be able to compare the two structures in our tests, and know what were the specific differences between them. 
Write a helper, which is given two inputs (actual and expected), and outputs a list of all the diffs between them, using the following github-esque format:
'''

[
  [ '-', 'id',                  9876              ],
  [ '-', 'last_name',           'Soprano'         ],
  [ '-', 'account.bank_name',   'Bank Of America' ],
  [ '+', 'id',                  20                ],
  [ '+', 'account.balance',     500               ]
]

#####################
# Implement me!
#####################
def diff(actual, expected):
    missing_items = _compare_dicts(expected, actual)
    additional_items = _compare_dicts(actual, expected)

    print(missing_items, '\n', additional_items)

    print(_create_listed_comparison(missing_items, additional_items))

    return []


# check if each expected key and value is in actual
#   if a key or value is missing, then add to a dict

# check if each actual key and value is in expected
#   if not, then add to dict

# function_0(expected_values, actual_values): above should be the same, just swap inputs for comparison

# function_1(missing_items, additional_items): 
# takes missing itesm and additional items to format git-esque comparison output

def _compare_dicts(expected_values, actual_values):
    '''
    '''
    discrepancies = {}
    for key in expected_values:
        if key not in actual_values.keys():
            discrepancies[key] = expected_values[key]
        elif isinstance(expected_values[key], dict):
            discrepancies[key] = _compare_dicts(expected_values[key], actual_values[key])
        elif expected_values[key] != actual_values[key]:
            discrepancies[key] = expected_values[key]

    return discrepancies


def _create_listed_comparison(missing_items, additional_items):
    '''
    [
        [ '-', 'id',                  9876              ],
        [ '-', 'last_name',           'Soprano'         ],
        [ '-', 'account.bank_name',   'Bank Of America' ],
        [ '+', 'id',                  20                ],
        [ '+', 'account.balance',     500               ]
    ]
    '''
    comparison_list = []

    for key in _crawl_dicts_for_non_dict_keys(missing_items):
        if not isinstance(key, list):
            comparison_list.append(['-', key, missing_items[key]])
        else:
            comparison_list.append(['-', '.'.join(key), _crawl_dict_for_value(key, missing_items)])

    for key in _crawl_dicts_for_non_dict_keys(additional_items):
        if not isinstance(key, list):
            comparison_list.append(['+', key, additional_items[key]])
        else:
            comparison_list.append(['+', '.'.join(key), _crawl_dict_for_value(key, additional_items)])
        
    return comparison_list


def _crawl_dict_for_value(key_list, dict_of_items):
    '''
    '''
    current_layer = dict_of_items[key_list[0]]
    for key in key_list[1:]:
        if key in current_layer:
            return current_layer[key]
        else:
            current_layer = current_layer[key]


def _crawl_dicts_for_non_dict_keys(dict_of_items):
    '''
    '''
    output_list = []
    for key in dict_of_items:
        if isinstance(dict_of_items[key], dict):
            stacked_keys = _crawl_dicts_for_non_dict_keys(dict_of_items[key])
            stacked_keys.insert(0, key)
            output_list.append(stacked_keys)
        else:
            output_list.append(key)

    return output_list

diff(actual, expected)