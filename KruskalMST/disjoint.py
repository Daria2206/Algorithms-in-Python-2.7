
"""Disjoint-set data structure

Implementation based on the pseudocode from "Intoduction to Algorithms" by
T.H. Cormen et al. In this implementation, sets are represented by rooted trees.
Two heuristics, that is "union by rank" and "path compression", are used to
for optimization. Runs in time O(m alpha(n)) for m disjoint-set operation on
n elements.

A disjoint-set data structure maintains a collection S = {S1, S2, S3 ... Sk} of
disjoint dynamic sets.

Supported operations:

make_set(x)  # creates a new set whose only member (and thus representative) is
               x -  x must not be in any other set (sets are disjoint)
union(x, y)  # unites sets that contain x and y (ex. Sx and Sy) into a new set
               that is a union of these two sets - the representative of the
               resulting set is any member of Sx U S
find_set(x)  # returns a pointer to the representative of the (unique) set
               containing x.
"""

from collections import Counter

class SetMember():
    """
    Models a node with one member in a tree representing one set.
    """
    def __init__(self, value):
        self.value = value
        self.parent = value
        self.rank = 0

    def __str__(self):
        return 'Value: %s Parent: %s Rank: %s' % (self.value, self.parent, self.rank)


class DSets(dict):
    """
    Implements disjoint-set data structure. Sets are represented as rooted trees
    with each node containinig one member and each tree representing one set. It's
    optimized by use of "union-by-rank" and "path compression" heuristics.
    """

    def makeset(self, member):
        """
        Creates a new tree with just one node with initial rank "0" and pointer
        to itself as a root.
        Rank is an upper bound on the height of the node.
        """
        self.member = SetMember(member)
        self[member] = self.member


    def findset(self, member):
        """
        Finds the root of the tree. The find path is compressed during operation
        of findset.
        """
        if self[member].parent != member:
            self[member].parent = self.findset(self[member].parent)
        return self[member].parent


    def link(self, root_x, root_y):
        """
        A subroutine called by union. Takes pointers to two roots as inputs.
        """
        if self[root_x].rank > self[root_y].rank:
            self[root_y].parent = self[root_x].parent
        else:
            self[root_x].parent = self[root_y].parent
            if self[root_x].rank ==  self[root_y].rank:
                self[root_y].rank += 1


    def union(self, x, y):
        """
        Causes the root of one tree to point to the root of the other. It has
        two cases depending of whether the roots of the trees have equal rank.If
        they don't, the root with a higher rank is made the parent of the root
        with lower rank, but ranks themselver remains unchanged. If they are one
        root is arbitratly chosen as the parent and its rank is incremented.
        """
        self.link(self.findset(x), self.findset(y))


    def __str__(self):
        representation = ''
        for dset in self.items():
            representation += '%s: %s' % (dset[0], dset[1]) + '\n'
        return representation
