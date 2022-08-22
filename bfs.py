# Author: Ivy Zhang
# Date: 03/05/2022
# Purpose: Lab 4 Final - BFS Algorithm

from collections import deque


def breadth_first_search(start_vertex, end_vertex):
    frontier = deque()
    backpointer = {}  # all the moves

    frontier.append(start_vertex)
    backpointer[start_vertex] = None

    while len(frontier) != 0:
        vertex = frontier.popleft()
        for v in vertex.adj_list:
            if v not in backpointer:
                frontier.append(v)
                backpointer[v] = vertex
        if end_vertex in backpointer:
            break
    path = []
    current = end_vertex
    while current != None:
        path.append(current)
        if current in backpointer:
            current = backpointer[current]
    return path

