#!/MinOddPath/venv/bin python3.6
# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
import heapq


def create_graph():
    vertices = []

    edges = defaultdict(list)
    weights = {}

    try:
        with open(sys.argv[1]) as file:
            for v in range(0, int(file.readline()[0])):
                v = v + 1
                vertices.append(v)

            for line in file.readlines()[0:]:
                try:
                    values = line.split(" ")
                    u = int(values[0])
                    v = int(values[1])
                    w = int(values[2])

                    edges[even(u)].append(odd(v))
                    edges[odd(u)].append(even(v))
                    edges[odd(v)].append(even(u))
                    edges[even(v)].append(odd(u))

                    weights[(even(u), odd(v))] = w
                    weights[(odd(u), even(v))] = w
                    weights[(even(v), odd(u))] = w
                    weights[(odd(v), even(u))] = w
                except ValueError:
                    continue
    except FileNotFoundError:
        print("File not found, please try another filename.")

    Dijkstra(vertices, edges, weights)


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
    create_graph()
