import heapq
from typing import List

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    """
    A is a heapified list. Get the k largest elements without modifying A.

    Idea: A is a complete binary tree. Easy to add an element and both
    of its children to a new heap.
    """

    newheap = []
    ans = []

    heapq.heappush(newheap, (-A[0], 0))

    while len(ans) < k:
        val, ind = heapq.heappop(newheap)
        ans.append(-val)

        # Add children to the heap. They are candidates for
        # the next largest value.
        ind1, ind2 = 2*ind + 1, 2 * ind + 2
        if len(A) > ind1:
            heapq.heappush(newheap, (-A[ind1], ind1))
        if len(A) > ind2:
            heapq.heappush(newheap, (-A[ind2], ind2))

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
