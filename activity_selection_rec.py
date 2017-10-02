"""
Python implementation of greedy algorithm that recursively solves the activity
selection problem.
The activivity selection problem: scheduling several competing activities that
require the use of a common resource, with the goal of selecting a maximum-size
set of mutually compatible activities. Two activities are compatibile if the
intervals of their operation do not overlap.
"""

def order_by_ftime(tasks_lst):
    """
    Preprocessing step before calling the recursive activity selection algorithm.
    Orders activities by monotonically increasing finish times, breaking ties
    arbitraly.
    """
    return sorted(tasks_lst, key=lambda task: task[1])

def select_activity(tasks, subproblem, org_size):
    """
    Recursive procedure to solve the activity-selection problem in O(n). Takes a list of
    tasks as tuples (where tup[0] is start time of the activitie and tup[1] is its
    finish time), the index of subproblem to solve and the size of orginal
    problem.
    It assumes tasks to be scheduled are already ordered by monotonically
    increasing finish time.
    """
    subseq = subproblem + 1
    while subseq <= org_size and tasks[subseq][0] < tasks[subproblem][1]:
        subseq += 1
    if subseq <= org_size:
        scheduled = select_activity(tasks, subseq, org_size)
        scheduled.insert(0, tasks[subseq])
        return scheduled
    else:
        return []

def main(to_be_scheduled):
    """
    Takes list of activities that are represented as tuples. Tup[0] contains
    start time of activity and tup[1] its finish time. Adds the fictitious
    activity with finish time 0 so that the subproblem S0 is the entire set of
    activities S. Sorts activities so they come in monotonically increasing
    order. Runs recursive activity selection algorithm.
    """
    to_be_scheduled.append((0, 0))
    tasks = order_by_ftime(to_be_scheduled)
    print select_activity(tasks, 0, 11)


if __name__ == "__main__":
    to_schedule = [(5, 9), (1, 4), (2, 14), (0, 6), (6, 10), (3, 9), (5, 7), (12, 16),
           (3, 5), (8, 12), (8, 11)]
    main(to_schedule)
