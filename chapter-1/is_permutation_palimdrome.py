# Checks to see if a string is a permutation of a palindrome. Note that this
# is not a check to see if it is a palindrome itself, but can be permuted into
# one.

import unittest
from collections import Counter


def pal_perm(phrase: str) -> bool:
    """Returns true if a phrase can be a permutation of a palindrome."""
    # It can be a palindrome if each letter shows up an even number of times if
    # the string has an even number of letters OR, if it's a string with an odd
    # number of letters, one letter will show up an odd number of times.
    phrase = ''.join(filter(str.isalpha, phrase)).upper()
    counter = Counter(phrase)
    return sum(counter[element] % 2 for element in counter) <= 1


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
