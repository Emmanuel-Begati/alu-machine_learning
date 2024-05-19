#!/usr/bin/env python3
"""
This module provides a function to add two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1 (list): First input array.
        arr2 (list): Second input array.

    Returns:
        list: New list containing the element-wise sum of arr1 and arr2.
            If arr1 and arr2 are not the same shape, returns None.
    """
    if len(arr1) != len(arr2):
        return None

    return [a + b for a, b in zip(arr1, arr2)]