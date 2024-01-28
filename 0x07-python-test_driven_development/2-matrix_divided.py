#!/usr/bin/python3
"""

contains matrix_divided function
divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):    
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(matrix[i]) != len(matrix[i+1])
                raise TypeError("Each row of the matrix must have the same size")
            if not isinstance(div,(int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            for i in matrix:
                return matrix[i] / div
