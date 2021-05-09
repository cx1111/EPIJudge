from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    # 0 <= cap <= vmax
    if target_payroll == 0:
        return 0

    current_salaries.sort()

    # Base case where cap must be below smallest current salary
    if current_salaries[0] * len(current_salaries) > target_payroll:
        return target_payroll / len(current_salaries)

    cumsum = []
    for salary in current_salaries:
        cumsum.append(salary + (cumsum[-1] if cumsum else 0))

    # No need for cap
    if cumsum[-1] < target_payroll:
        return -1

    # Iterate the cap in increasing order
    for i in range(len(current_salaries)):
        val = current_salaries[i]
        total_with_cap = val * (len(current_salaries)-i)
        if i:
            total_with_cap += cumsum[i-1]

        # The cap must lie at an existing salary, or be between two.
        if total_with_cap == target_payroll:
            return val
        elif total_with_cap > target_payroll:
            # Cap must lie between this and previous salary.
            total_prev = cumsum[i-1]
            total_remainder = target_payroll - total_prev
            # Cap * remainder + prev values = target
            return total_remainder / (len(current_salaries) - i)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
