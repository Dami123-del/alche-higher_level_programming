#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # The outer loop creates a new row
    # The inner loop squares each element in that row
    return [[num ** 2 for num in row] for row in matrix]
