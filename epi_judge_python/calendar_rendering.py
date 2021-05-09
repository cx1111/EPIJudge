import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    """
    COMPLETE!!!
    """
    # Decompose each event into two objects: (starttime, start_type=0), (endtime, end_type=1)
    # Put in ascending order and track the number of open simultaneous events
    # between adjacent objects.
    # print(A)
    flattened_events = []
    for event in A:
        flattened_events.append((event.start, 0))
        flattened_events.append((event.finish, 1))
    # Sort will be done first by the time, then by the type. Event types/nums are chosen
    # such that start events will come before finish events at the same time. ie. If an
    # event finishes the same time as another starts, it counts as an overlap.
    flattened_events.sort()

    max_simul = 0
    n_open_events = 0

    # print(flattened_events)
    for event in flattened_events:
        # print('\nAt', event[0])
        # Actually don't even need the times anymore.
        if event[1] == 0:
            # print('here')
            n_open_events += 1
            # print(f'Open to {n_open_events}')
            max_simul = max(max_simul, n_open_events)
        else:
            n_open_events -= 1
            # print(f'Close to {n_open_events}')

    # print(flattened_events)
    return max_simul


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
