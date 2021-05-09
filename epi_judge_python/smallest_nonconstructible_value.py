from typing import List

from test_framework import generic_test


def seek_next_ind(nums, i):
    original = nums[i]
    while i < len(nums) and nums[i] == original:
        i += 1
    return i


def smallest_nonconstructible_value(A: List[int]) -> int:
    A.sort()
    if A[0] != 1:
        return 1

    i = 0
    cumsum = 0

    while i < len(A):
        if A[i] - cumsum > 1:
            return cumsum + 1

        j = seek_next_ind(A, i)
        count = j - i
        cumsum += count * A[i]
        i = j

    # print(cumsum)
    return cumsum + 1


if __name__ == '__main__':
    # print(smallest_nonconstructible_value([1, 2, 3, 4]))
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
