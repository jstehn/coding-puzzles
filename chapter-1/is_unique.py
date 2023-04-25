# Is Unique: Determines if a string has an repeated characters.

import unittest


def unique(string: str) -> bool:
    """Returns true if there are no duplicate characters in a given string.

    Examples
    --------
    >>> unique('abcd')
    True
    >>> unique('23ds2')
    False
    """
    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True


# Tests
class test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

    if __name__ == "__main__":
        unittest.main()
