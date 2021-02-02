#!/MinOddPath/venv/bin python3.6
# -*- coding: utf-8 -*-
from collections import defaultdict
import heapq


def create_graph():
    edges = defaultdict(list)
    weights = {}

    num_vertices, num_edges = (map(int, input().split(" ")))
    vertices = [x for x in range(1, num_vertices+1)]

    while True:
        try:
            u, v, w = (map(int, input().split(" ")))
            add_edge(u, v, w, edges, weights)
        except EOFError:
            break

    return vertices, edges, weights


def add_edge(u, v, w, edges, weights):
    edges[even(u)].append(odd(v))
    edges[odd(u)].append(even(v))
    edges[odd(v)].append(even(u))
    edges[even(v)].append(odd(u))

    weights[(even(u), odd(v))] = w
    weights[(odd(u), even(v))] = w
    weights[(even(v), odd(u))] = w
    weights[(odd(v), even(u))] = w


def Dijkstra(lvertices, ledges, lweights):
    dist = {vertex: float('infinity') for vertex in range(0, size(len(lvertices)))}
    dist[even(1)] = 0

    stack = [(0, even(1))]
    while stack:
        current_dist, u = heapq.heappop(stack)

        if current_dist > dist[u]:
            continue

        for v in ledges[u]:
            distance = current_dist + lweights[(u, v)]

            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(stack, (distance, v))

    answer = dist[odd(lvertices[-1])]
    if answer == float('infinity'):
        print(':(')
    else:
        print(answer)


def odd(a):
    return (a * 10) + 1


def even(a):
    return (a * 10) + 2


def size(a):
    return a * 10 + 3


if __name__ == "__main__":
    vertices, edges, weights = create_graph()
    Dijkstra(vertices, edges, weights)
