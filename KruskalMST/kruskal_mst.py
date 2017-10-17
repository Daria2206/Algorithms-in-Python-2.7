"""
Python 2.7 implementation of Kruskal's algorithm for finding minimum spanning tree
of a graph. It uses the disjoint-set data structure implemented as the
disjoint-set-forest imlemenation with the union-by-rank and path compression
heuristics.
"""

from disjoint import DSets
import sys

def load_graph(inp=sys.argv[1]):
    """
    Takes name of the file containing representation of a undirected, weighted
    graph. Loads graph from a given file. Returns a list that models a graph.
    The graph contains each edge and its weight.

    Input format: This file describes an undirected graph with integer edge costs.
    It has the following format:
    [number_of_nodes] [number_of_edges]
    [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
    [one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
    For example, the third line of the file is "2 3 -8874", indicating that
    there is an edge connecting vertex #2 and vertex #3 that has cost -8874.
    The edge costs may be positive or negative and do not have to be distinct.
    """

    graph = []
    for line in open(inp):
        line = line.strip().split()
        if len(line) > 2:
            graph.append(((int(line[0]), int(line[1]), int(line[2]))))
    return graph

def kruskal(unsorted_graph):
    """
    Takes unsorted graph. Performs Kruskal's algorithm for finding
    minimum spanning tree. Returns list of tuples forming minimum spanning tree.
    Each tuple contains an edge with corresponding costs of adding it to the tree.
    """

    MST = []
    diset = DSets()
    graph = sorted(unsorted_graph, key=lambda weight: weight[2])
    vertices_num = len(graph)
    for vertex in range(vertices_num):
        diset.makeset(vertex)
    for edge in graph:
        if diset.findset(edge[0]) != diset.findset(edge[1]):
            MST.append(edge)
            diset.union(edge[0], edge[1])
    return MST

def overall_cost(mst):
    """
    Calculates the overall cost of a minimum spanning tree: an integer, which
    may or may not be negative.
    """
    return sum(weight for _, _, weight in mst)


if __name__ == "__main__":
    unsorted_graph = load_graph()
    mst = kruskal(unsorted_graph)
    print overall_cost(mst) # Should return -3612829.
