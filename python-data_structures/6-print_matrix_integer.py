#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Check if it is the last element in the row
            if i == len(row) - 1:
                # Print the integer without a space at the end
                print("{:d}".format(row[i]), end="")
            else:
                # Print the integer followed by a space
                print("{:d}".format(row[i]), end=" ")

        # After each row, print a newline
        print("")
