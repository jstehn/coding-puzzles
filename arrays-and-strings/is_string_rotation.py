# Using is_substring only once, check if two strings are a rotation of each.
# other e.g. waterbottle is a rotation of erbottlewat

import unittest


def is_substring(string: str, sub: str) -> bool:
    return sub in string


def string_rotation(s1: str, s2: str) -> bool:
    """If s2 is a rotation of s1, then it is also a substring of s1 + s1.

    e.g.
    s1 = waterbottle
    s2 = erbottlewat
    s1 + s1 = waterbottlewaterbottle
                 ^^^^^^^^^^^
    """
    return is_substring(s1 + s1, s2) and len(s1) == len(s2) != 0


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
