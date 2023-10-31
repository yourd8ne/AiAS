import random
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import timeit
matplotlib.use('Qt5Agg')

class TernaryHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return value

    def _sift_up(self, index):
        parent = (index - 1) // 3
        if parent >= 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)

    def _sift_down(self, index):
        child1 = 3 * index + 1
        child2 = child1 + 1
        child3 = child2 + 1
        smallest = index
        if child1 < len(self.heap) and self.heap[child1][0] < self.heap[smallest][0]:
            smallest = child1
        if child2 < len(self.heap) and self.heap[child2][0] < self.heap[smallest][0]:
            smallest = child2
        if child3 < len(self.heap) and self.heap[child3][0] < self.heap[smallest][0]:
            smallest = child3
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)


class Graph3:
    def __init__(self, num_vertices=None):
        self.nodes = set()
        self.edges = {}
        self.distances = {}
        self.num_vertices = num_vertices

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def dijkstra(self, initial_node):
        if initial_node not in self.nodes:
            return f"Узел {initial_node} отсутствует в графе"
        if initial_node not in self.edges:
            return f"Нет ребер, исходящих из узла {initial_node}"
        visited = {initial_node: 0}
        heap = TernaryHeap()
        heap.push((0, initial_node))
        while heap.heap:
            current_weight, min_node = heap.pop()
            if current_weight != visited[min_node]:
                continue
            if min_node not in self.edges:
                continue
            for edge in self.edges[min_node]:
                if edge not in visited:
                    visited[edge] = float('inf')
                weight = current_weight + self.distances[(min_node, edge)]
                if weight < visited[edge]:
                    visited[edge] = weight
                    heap.push((weight, edge))
        return visited
