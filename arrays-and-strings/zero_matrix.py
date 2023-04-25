# An algorithm such that if any element in an M x N matrix is 0,
# the entire row and colum are set to 0.
import unittest


def zero_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Returns a matrix where any rows or columns that have a 0 in it are
    replaced with 0s"""
    null_rows = set()
    null_columns = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                null_rows.add(i)
                null_columns.add(j)

    for i in null_rows:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
    for j in null_columns:
        for i in range(len(matrix)):
            matrix[i][j] = 0
    return matrix


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
