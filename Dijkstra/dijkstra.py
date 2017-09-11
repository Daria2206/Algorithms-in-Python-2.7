"""
Python implementation of Dijkstra's shortest path algorithm. It was written for
the programming assignment for 'Graph Search, Shortest Paths, and Data
Structures' by Stanford University on Coursera.
"""
from heapq import heappush, heappop
import heapq
import time

def load_graph(file_name):
    """
    Takes the name of the file containing representation of a directed, weighted
    graph. Loads graph from a given file. Returns dictionary that models a graph.

    Input format is the following:
    Each row consists of the node tuples that are adjacent to that particular
    vertex along with the length of that edge. For example, the 1th row has 1 as
    the first entry indicating that this row corresponds to the vertex labeled 1.
    The next entry of this row "2,1" indicates that there is an edge between
    vertex 1 and vertex 2 that has length 1. The rest of the pairs of this row
    indicate the other vertices adjacent to vertex 1 and the lengths of the
    corresponding edges.
    """

    graph = {}
    opened = open(file_name)
    for dummy_line in opened:
        line = dummy_line.split()
        node = int(line[0])
        graph[node] = {}
        edges = line[1:]
        for edge in edges:
            head = int(edge.split(',')[0])
            weigth = int(edge.split(',')[1])
            graph[node][head] = weigth
    return graph


def dijkstra(digraph, source= 1):
    """
    Takes a weighted, directed graph and a source vertex. Runs Dijkstra's
    shortest-path algorithm on the input graph, by default using 1 (the first
    vertex) as the source vertex. Computes the shortest-path distances between
    the source vertex and every other vertex of the input graph.

    Assumptions:
    *there's a path from S to every other vertex;
    *every edge of the graph has a non-negative edge length;
    """
    start = time.clock()
    sp_estimate = {source:0}
    predecessors = {}
    min_priority_queue = [(0,source)]
    computed = dict.fromkeys(digraph.keys(), False)
    while min_priority_queue:
        _, shortest = heappop(min_priority_queue)
        if computed[shortest] == True:
            continue
        computed[shortest] = True
        for adj_vertex in digraph[shortest]:
            relax(digraph, shortest, adj_vertex, sp_estimate, predecessors)
            heappush(min_priority_queue, (sp_estimate[adj_vertex], adj_vertex))
    print "Shortest-path computed in ", time.clock() - start
    return sp_estimate, predecessors


def relax(min_priority_queue, shortest, adj_vertex, sp_estimate, predecessors):
    """
    Tests whether the shortest path may be improved to adj_vertex by going
    through shortest, If yes, updates sp_estimate[adj_vertex] and
    predecessors[adj_vertex].
    """
    inf = float('inf')
    dist = sp_estimate.get(shortest, inf) + min_priority_queue[shortest][adj_vertex] # Possible shortcut estimate
    if dist < sp_estimate.get(adj_vertex, inf):
        sp_estimate[adj_vertex], predecessors[adj_vertex] = dist, shortest
    return True


if __name__ == "__main__":
    file_name = "dijkstra.txt"
    digraph = load_graph(file_name)
    shortest_paths = dijkstra(digraph, 1)[0]
    print shortest_paths
