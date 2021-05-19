import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A: List[int]) -> MinMax:
    """
    Find min and max of a list with fewer than 2n-1 comparisons.
    Basic method is iterate along and compute running min/max.

    Can do better by comparing pairs with each other, then only
    comparing larger one with max, and smaller one with min.
    """
    if len(A) == 1:
        return MinMax(A[0], A[0])
    elif len(A) == 2:
        return MinMax(A[0], A[1]) if A[1] > A[0] else MinMax(A[1], A[0])

    rmin, rmax = (A[0], A[1]) if A[1] > A[0] else (A[1], A[0])

    for i in range(2, len(A), 2):
        # Final odd numbered element
        if i + 1 > len(A) - 1:
            rmin = min(rmin, A[-1])
            rmax = max(rmax, A[-1])
        else:
            if A[i] > A[i+1]:
                rmax = max(A[i], rmax)
                rmin = min(A[i+1], rmin)
            else:
                rmax = max(A[i+1], rmax)
                rmin = min(A[i], rmin)
    # breakpoint()
    return MinMax(rmin, rmax)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
