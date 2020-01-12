#!/usr/bin/python3
"""Function that divides all elements of a matrix """
def matrix_divided(matrix, div):
    """
    div all elements of a matrix
    """
    new_matrix = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for idx in range(len(matrix)):
        if type(matrix[idx]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            lista = []
            for data_of_list in range(len(matrix[idx])):
                if type(matrix[idx][data_of_list]) is not int and type(matrix[idx][data_of_list]) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                else:
                    result = round(matrix[idx][data_of_list]/div, 2)
                    lista.append(result)
            new_matrix.append(lista)
    return new_matrix
