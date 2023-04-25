# Given an image represented by an N x N matrix, write a method to rotate the
# image 90 degrees in place.
import unittest


def rotate_matrix(matrix: list[list[int]], layer: int = 0):
    """Uses recurssion to rotate a N x N matrix mutatively."""
    n = len(matrix)
    for layer in range(0, n // 2):
        for i in range(layer, n - layer - 1):
            temp = matrix[layer][i]
            matrix[layer][i] = matrix[-i - 1][layer]
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            matrix[i][-layer - 1] = temp
    return matrix


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
