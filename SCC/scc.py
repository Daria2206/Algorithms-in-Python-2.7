"""
Python implementation of the Kosaraju's algorithm for computing strongly
connected components (SCCs) using iterative DFS. It was written for the programming
assignment for 'Graph Search, Shortest Paths, and Data Structures' by Stanford
University on Coursera. Therefore it contains some specific solutions tailored
for the given task (for ex. function loadgraph loads graph from the file in
which a graph is represented in a specific way).
"""

import time, sys
from collections import deque, Counter

def loadgraph(textfile, nodes_num = 875714):
    """
    Takes name of the file containing representation of a graph and total number
    of nodes in a graph. Loads graph and its transpose from a given file.
    Returns dictionaries that model both a graph and its transpose. Time
    necessery to load the graph with 875714 nodes (and its reverse) was on
    avrage 11 secs (Python 2.7.12|Anaconda 4.2.0 (64-bit)|[MSC v.1500 64 bit
    (AMD64)]).

    Input format: the file contains the edges of a directed graph. Vertices are
    labeled as positive integers from 1 to n. Every row indicates an edge, the
    vertex label in first column is the tail and the vertex label in second
    column is the head (the graph is directed, and the edges are directed from
    the first column vertex to the second column vertex). For example, the row
    in the file may look like this: "1 4" which means that the vertex with label
    1 has an outgoing edge to the vertex with label 4.
    """
    graph, graph_reversed = {}, {}
    for dummy_node in xrange(1, nodes_num + 1):
        graph[dummy_node], graph_reversed[dummy_node] = [], []
    opened = open(graph_file)
    for dummy_line in opened:
        line = dummy_line.split()
        node = int(line[0])
        edge = int(line[1])
        graph[node].append(edge)
        graph_reversed[edge].append(node)
    return graph, graph_reversed

def dfs_order(graph):
    """
    Searches a given directed graph and timestamps each vertex with its
    finishing time.
    """
    nodes_num = len(graph.keys())
    explored = {dummy: 0 for dummy in xrange(1, nodes_num + 1)}
    ftime = 0
    order = deque([])
    magic_order = {}
    for node in xrange(nodes_num, 0, -1):
        if explored[node] == 0:
            unexplored = True
            stack = deque([node])
            order = deque([])
        else:
            unexplored = False
        while stack:
            vertex = stack.pop()
            if explored[vertex] == 0:
                explored[vertex] = 1
                order.append(vertex)
                stack.extend(graph[vertex])
        if unexplored == True:
            while len(order) > 0:
                ftime += 1
                to_be_timed = order.pop()
                magic_order[ftime] = to_be_timed

    return magic_order

def dfs_leaders(graph, order):
    """
    Run a dfs on a given graph processing nodes	in decreasing order of finishing
    times. Returns list of leaders in the graph - each leader appears on the
    list the number of times equal to the number of nodes in the strongly connected
    component. So for ex. if a graph has 3 sccs with 3 nodes each the output
    list will look like that: [8, 8, 8, 9, 9, 9, 7, 7, 7].
    """
    nodes_num = len(graph.keys())
    explored = {dummy: 0 for dummy in xrange(1, nodes_num + 1)}
    leaders = []
    nodegetter = len(order.keys())
    while nodegetter > 0:
        node = order[nodegetter]
        if explored[node] == 0:
            stack = deque([node])
            leader = node
        while stack:
            vertex = stack.pop()
            if explored[vertex] == 0:
                explored[vertex] = 1
                stack.extend(graph[vertex])
                leaders.append(node)
        nodegetter -= 1
    return leaders


def scc(graph_file, nodes_num = 875714, leaders_num = 5):
    """
    Takes file name from which it loads graph and its transpose, the number of
    nodes in the graph (defaults to 875714 which was the number of nodes in
    a graph given for the programming assignment) and number of strongly
    connected components to be returned (based on their size, in decreasing
    order) (defaults to 5 to be tailored for the programming assignment).
    Returns list of tuples [(leader, number_of_components)].
    """

    start_for_total = start = time.clock()
    print "Loading graphs..."
    graph, graph_rev = loadgraph(graph_file, nodes_num)
    print "Graphs loaded in ", time.clock() - start
    start = time.clock()
    print "Computing finishing times..."
    magic_order = dfs_order(graph_rev)
    print "Finishing times computed in ", time.clock() - start
    start = time.clock()
    print "Finding strongly conected components..."
    leaders = dfs_leaders(graph, magic_order)
    cnt = Counter()
    for dummy_leader in leaders:
        cnt[dummy_leader] += 1
    scc = cnt.most_common(leaders_num)
    print "Scc calculated in ", time.clock() - start
    print "Total computing time %s on Python %s " % (time.clock() - start_for_total, sys.version)
    for dummy_component in scc:
        print "Leader: %s. Number of components: %s. " % (dummy_component[0], dummy_component[1])
    print "Strongly connected components ", scc
    return scc


if __name__ == "__main__":
    print "************************** Test case no. 1 **************************"
    graph_file = "scc_test_1.txt"  # should return  [(8, 3), (9, 3), (7, 3)]
    scc(graph_file, 9)
