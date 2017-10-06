"""
Python 2.7 implementation of Prim's algorithm for finding minimum spanning tree
of a graph.
"""
import time
import sys
from collections import defaultdict
from heapq import heappush, heappop

def load_graph(inp=sys.argv[1]):
    """
    Takes name of the file containing representation of a undirected, weighted
    graph. Loads graph from a given file. Returns dictionary that models a graph.

    Input format: This file describes an undirected graph with integer edge costs.
    It has the following format:
    [number_of_nodes] [number_of_edges]
    [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
    [one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
    For example, the third line of the file is "2 3 -8874", indicating that
    there is an edge connecting vertex #2 and vertex #3 that has cost -8874.
    The edge costs may be positive or negative and do not have to be distinct.
    """
    graph = defaultdict(list)
    for line in open(inp):
        line = line.strip().split()
        if len(line) > 2:
            graph[int(line[0])].append((int(line[1]), int(line[2])))
            graph[int(line[1])].append((int(line[0]), int(line[2])))
    return graph

def mst_prim(graph, root=1):
    """
    Takes graph and starting vertex and performs Prim's algorithm for finding
    minimum spanning tree. Returns dictionary of nodes with corresponding costs
    of adding them to the tree (indicators) and dictionary of parents of each of
    the nodes in the tree.
    During the execution of the algorithm, vertices that are not already in the
    tree are put in a min-priority queue based on a key attribute. The key
    attribute is the minimum weight of any edge connecting verex not in the tree
    to a vertex in the tree.
    Supposed to run in O(E + V lg V).
    """

    indicators = dict.fromkeys(graph.keys(), float('inf'))
    predecessors = dict.fromkeys(graph.keys(), None)
    # Keeps track of what has been sucked into the MS tree.
    tree = dict.fromkeys(graph.keys(), False)
    indicators[root] = 0
    pq = [(0, root)]
    while pq:
        popped = heappop(pq)
        tree[popped[1]] = True
        for vertex in graph[popped[1]]:
            if tree[vertex[0]] == False and vertex[1] < indicators[vertex[0]]:
                indicators[vertex[0]] = vertex[1]
                predecessors[vertex[0]] = popped[1]
                heappush(pq, (vertex[1], vertex[0]))
    return indicators, predecessors

def overall_cost(indicators):
    """
    Calculates the overall cost of a minimum spanning tree: an integer, which
    may or may not be negative.
    """
    return sum(indicators.values())


def main():
    start = time.clock()
    graph = load_graph()
    indicators, predecessors = mst_prim(graph)
    cost = overall_cost(indicators)
    print cost # Correct answer: 37
    print "Time: ", time.clock()-start

if __name__ == "__main__":
    main()
