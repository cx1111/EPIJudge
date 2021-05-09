import collections
from typing import Set

from test_framework import generic_test


def differ_by_one(a, b):
    """
    Returns where a and b only differ by at most one char.

    Shouldn't be called with same strings.
    """
    n_diff = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            n_diff += 1
            if n_diff > 1:
                return False

    return True


def transform_string(s_pool: Set[str], s0: str, s1: str) -> int:
    """
    s0, s1 and s_pool items all have the same length.

    Approach: Make a graph, where nodes are strings, and edges connect
    strings that only differ by one.

    Complexity = O(v^2 + v).

    Works but kind of slow.
    """
    # Make adjacency dict, where key is string, val[] contains edges to other
    # strings.

    # Need this for indexing strings to create edges between vertices.
    all_strings = list(s_pool) + [s0, s1]
    adj = {s: [] for s in all_strings}

    for i in range(len(all_strings)):
        for j in range(i, len(all_strings)):
            # Careful with var names
            a, b = all_strings[i], all_strings[j]
            if differ_by_one(a, b):
                adj[a].append(b)
                adj[b].append(a)

    # Use BFS to find shortest path if any.
    # Records final distances. Also doubles as 'visited' array.
    distances = {k: -1 for k in all_strings}  # [-1] * len(all_strings)
    distances[s0] = 0

    dist_from_start = 1
    explore_verts = adj[s0]

    while distances[s1] == -1 and explore_verts:
        next_explore_verts = []

        for u in explore_verts:
            distances[u] = dist_from_start

        for u in explore_verts:
            # Visit neighbors that haven't been visited
            for v in adj[u]:
                if distances[v] == -1:
                    next_explore_verts.append(v)

        explore_verts = next_explore_verts
        dist_from_start += 1

    return distances[s1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
