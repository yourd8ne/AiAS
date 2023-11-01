import numpy as np
import scipy.sparse as sp


class HexadecimalHeap:
    def __init__(self, size):
        self.heap = [None] * size
        self.size = size
        self.current_size = 0

    def push(self, value):
        if self.current_size >= self.size:
            return "Куча заполнена"
        
        self.heap[self.current_size] = value
        self._sift_up(self.current_size)
        self.current_size += 1

    def pop(self):
        if self.current_size == 0:
            return None
        
        value = self.heap[0]
        self.current_size -= 1
        self.heap[0] = self.heap[self.current_size]
        self.heap[self.current_size] = None
        self._sift_down(0)
        return value

    def _sift_up(self, index):
        parent = (index - 1) // 16
        if parent >= 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)

    def _sift_down(self, index):
        smallest = index
        for i in range(1, 17):
            child = 16 * index + i
            if child < self.current_size and self.heap[child][0] < self.heap[smallest][0]:
                smallest = child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)

class Graph16:
    def __init__(self, num_vertices=None):
        self.nodes = set()
        self.edges = {}
        self.distances = None
        self.num_vertices = num_vertices

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)

        if self.distances is None:
            self.distances = sp.lil_matrix((self.num_vertices, self.num_vertices))
        self.distances[from_node, to_node] = distance

    def dijkstra(self, initial_node):
        if initial_node not in self.nodes:
            return f"Узел {initial_node} отсутствует в графе"
        if initial_node not in self.edges:
            return f"Нет ребер, исходящих из узла {initial_node}"

        visited = np.inf * np.ones(self.num_vertices)
        visited[initial_node] = 0

        heap = HexadecimalHeap(size=self.num_vertices)
        heap.push((0, initial_node))

        while heap.current_size > 0:
            current_weight, min_node = heap.pop()

            if current_weight != visited[min_node]:
                continue

            if min_node not in self.edges:
                continue

            for edge in self.edges[min_node]:
                if edge not in visited:
                    continue

                weight = current_weight + self.distances[min_node, edge]

                if weight < visited[edge]:
                    visited[edge] = weight
                    heap.push((weight, edge))

        return visited
