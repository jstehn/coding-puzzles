# Given two strings, check if one is a permutation of the other

import unittest
from collections import Counter


def check_permutation(str1, str2):
    """Checks to see if two strings are permutations of one another with O(N)
    runtime

    Examples
    --------
    >>> check_permutation('abcd', 'bacd')
    True
    >>> check_permutation('abcd, 'd2cba')
    False
    """
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
