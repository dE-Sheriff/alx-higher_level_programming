#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    points = list_of_integers

    if points is None or points == []:
        return None
    lo = 0
    hi = len(points)
    mid = int(((hi - lo) // 2) + lo)
    if hi == 1:
        return points[0]
    if hi == 2:
        return max(points)
    if points[mid] >= points[mid - 1] and points[mid] >= points[mid + 1]:
        return points[mid]
    if mid > 0 and points[mid] < points[mid + 1]:
        return find_peak(points[mid:])
    if mid > 0 and points[mid] < points[mid - 1]:
        return find_peak(points[:mid])
