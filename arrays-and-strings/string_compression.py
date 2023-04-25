# Implements a basic string compression that counts repreated characters.
# If the string is not shorter, do not use the counted format.
# abbcccdddd -> a1b2c3d4
# abc -> abc
# abbccc -> abbccc

# O(N)
import unittest


def string_compression(string: str) -> str:
    compressed = []
    counter = 0
    last_char = string[0]  # Empty string breaks this, but ignoring it for now.

    for c in string:
        if c != last_char:
            compressed.append(last_char + str(counter))
            counter = 0
            last_char = c
        counter += 1
    compressed.append(last_char + str(counter))
    return min(string, ''.join(compressed), key=len)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef'),
        ('abc', 'abc'),
        ('abbccc', 'abbccc')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
