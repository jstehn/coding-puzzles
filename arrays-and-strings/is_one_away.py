# Write a function that returns True if the Levenshtein distance between two
# strings is 1 or less

import unittest


def one_away(str1: str, str2: str) -> bool:
    """Returns True if the strings can be made equal by adding, removing, or
    replacing a character."""
    if len(str1) == len(str2):
        # If true, there must be 0 or 1 replacement.
        return one_edit_replace(str1, str2)
    elif len(str1) + 1 == len(str2):
        # If true, there must be one character that needs to be added
        return one_edit_insert(str1, str2)
    elif len(str2) + 1 == len(str1):
        # If true, there must be one character that is subtracted.
        return one_edit_insert(str2, str1)
    return False


def one_edit_replace(str1: str, str2: str) -> bool:
    """Returns true if replacing one letter will make two strings the same."""
    return sum(str1[i] != str2[i] for i in range(len(str1))) <= 1


def one_edit_insert(str1: str, str2: str) -> bool:
    """Returns true if adding one letter will make two strings the same."""
    edited = False
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
