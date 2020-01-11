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
#        if matrix[idx] is not list:
#            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
#        else:
        for data_of_list in range(len(matrix[idx])):
            if type(data_of_list) is not int and type(data_of_list) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                result = round(data_of_list/div, 2)
                new_matrix[idx][data_of_list] = result
    return new_matrix
