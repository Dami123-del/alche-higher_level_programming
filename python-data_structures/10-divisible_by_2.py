#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Initialize an empty list to store the True/False results
    results = []

    # Iterate through every number in the provided list
    for num in my_list:
        # Check if the number is divisible by 2
        if num % 2 == 0:
            results.append(True)
        else:
            results.append(False)

    return results
