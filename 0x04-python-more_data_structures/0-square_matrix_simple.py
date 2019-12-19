#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = matrix.copy()
    if not matrix:
        return(None)
    for i in range(len(matrix)):
        square[i] = (list(map(lambda x: x**2, matrix[i])))
    return(square)
