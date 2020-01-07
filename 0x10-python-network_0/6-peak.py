#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Returns the peak of a list
    """
    if not list_of_integers:
        return None
    list_length = len(list_of_integers)
    return recursion_peak(list_of_integers, list_length)


def recursion_peak(array, length_arr):
    """
    Recurse until it finds a peak
    """
    return recursion_peak_divide(array, 0, length_arr - 1, length_arr)


def recursion_peak_divide(array, lower, higher, length_arr):
    """
    Binary search that returns index of peak element in a list
    """
    middle = lower + (higher - lower) / 2
    middle = int(middle)

    if ((middle == 0 or array[middle - 1] <= array[middle]) and
       (middle == length_arr - 1 or array[middle + 1] <= array[middle])):
        return array[middle]

    elif (middle > 0 and array[middle - 1] > array[middle]):
        return recursion_peak_divide(array, lower, (middle - 1), length_arr)

    else:
        return recursion_peak_divide(array, (middle + 1), higher, length_arr)
