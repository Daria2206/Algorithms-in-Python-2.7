'''Python 2.7.12 implementation of quick sort (based on pseudocode given in
"Introduction to Algorithms" - Cormen, Leiserson et al.)'''

import random

def partition(inp, beginning, end):
    '''Takes unsorted array, choses its last element as a pivot and partitions
    input array around it (puts all elements smaller than the pivot on the left
    of the pivot and all greater on the right of it). Returns index of pivot
    after its inserted in its rightful position.'''

    if len(inp) == 0:
        return inp
    pivot = inp[end-1]
    index = beginning - 1
    for dummy_index in xrange(beginning, end-1):
        if inp[dummy_index] <= pivot:
            index += 1
            if dummy_index != index:
                inp[index], inp[dummy_index] = inp[dummy_index], inp[index]
    inp[end-1], inp[index+1] = inp[index+1], inp[end-1]
    return index+1

def quick_sort(inp, beginning, end):
    '''Sorts unsorted array in place.'''
    if beginning < end:
        q = partition(inp, beginning, end)
        quick_sort(inp, beginning, q)
        quick_sort(inp, q+1, end)


# Some tests:
dummy_range = 100
# Creating unordered list of integers in given range to be sorted by quick_sort.
qs_inp = range(dummy_range)
random.shuffle(qs_inp)
#Making a copy of unordered list to be sorted by Python to check quick_sort correctnes.
py_inp = qs_inp[:]
print 'I am unordered list: \n', qs_inp
print
quick_sort(qs_inp, 0, len(qs_inp))
py_inp.sort()
print 'I am list after quick_sort: \n', qs_inp
print
print "Input list is correctly sorted: ", py_inp == qs_inp
