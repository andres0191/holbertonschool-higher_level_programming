#!/usr/bin/python3
"""Function that divides all elements of a matrix """
def matrix_divided(matrix, div):
    new_matrix = matrix.copy()
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for idx in range(len(matrix)):
        if matrix[idx] is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            for data_of_list in range(matrix[idx]):
                if type(data_of_list) is not int and type(data_of_list) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                else:
                    data_of_list
    return (new_matrix)
