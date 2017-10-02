"""
Python implementation of greedy algorithm that iteratively solves the activity
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


def select_activity(tasks):
    """
    Iterative procedure to solve the activity-selection problem in O(n) time.
    Takes a list of tasks as tuples (where tup[0] is start time of the activitie
    and tup[1] is its finish time). It collects selected activities into set
    "scheduled" and returns this set when is done (sorted according to the finish
    time). The variable "recent" indexes the most recent addition to "scheduled".
    It assumes tasks to be scheduled are already ordered by monotonically
    increasing finish time.
    """
    problem_size = len(tasks)
    scheduled = set([tasks[0]])
    recent = 1
    for subproblem in range(2, problem_size):
        if tasks[subproblem][0] >= tasks[recent][1]:
            scheduled.add(tasks[subproblem])
            recent = subproblem
    return order_by_ftime(scheduled)

def main(to_be_scheduled):
    """
    Takes list of activities that are represented as tuples. Tup[0] contains
    start time of activity and tup[1] its finish time. Sorts activities so they
    come in monotonically increasing order. Runs iterative activity selection
    algorithm.
    """

    tasks = order_by_ftime(to_be_scheduled)
    print select_activity(tasks)


if __name__ == "__main__":
    to_schedule = [(5, 9), (1, 4), (2, 14), (0, 6), (6, 10), (3, 9), (5, 7), (12, 16),
           (3, 5), (8, 12), (8, 11)]
    main(to_schedule)
