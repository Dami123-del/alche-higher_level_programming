#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            # The final combination followed by a newline
            print("{}{}".format(i, j))
        else:
            # All other combinations followed by a comma and space
            print("{}{}".format(i, j), end=", ")
