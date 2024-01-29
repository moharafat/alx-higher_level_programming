#!/usr/bin/python3
"""

contains matrix_divided function
divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
    result_matrix = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
            new_elment = round(element / div, 2)
            new_row.append(new_elment)
        result_matrix.append(new_row)
    return result_matrix
