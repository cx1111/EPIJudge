import heapq
from typing import Iterator, List

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    """
    Idea: Use a maxheap and a minheap. Put the large items in the minheap
    and the small items in the maxheap. The median can be made from their
    top values.

    """
    ans = []
    maxheap = []
    minheap = []

    for val in sequence:
        # Add the new value to minheap, and then pop the smallest value
        # from minheap and add it to maxheap. This is because we want
        # the small items in maxheap and large values in minheap.
        heapq.heappush(maxheap, -heapq.heappushpop(minheap, val))

        # Keep minheap larger or the same size for odd sized medians.
        if len(maxheap) > len(minheap):
            heapq.heappush(minheap, -heapq.heappop(maxheap))

        # Even number of elements. Get median from both
        if len(maxheap) == len(minheap):
            ans.append((-maxheap[0] + minheap[0]) / 2)
        else:
            ans.append(minheap[0])

    return ans


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
