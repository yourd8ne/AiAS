import numpy as np
import random
import gc
import timeit
import csv
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


class TernaryHeap:
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
        parent = (index - 1) // 3
        if parent >= 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)

    def _sift_down(self, index):
        smallest = index
        for i in range(1, 4):
            child = 3 * index + i
            if child < self.current_size and self.heap[child][0] < self.heap[smallest][0]:
                smallest = child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)


class Graph3:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = defaultdict(list)
        self.distances = np.zeros((num_vertices, num_vertices))
        self.nodes = set() 
    
    def reset(self):
        self.edges.clear()
        self.distances = None

    def add_vertex(self):
        if self.distances is None:
            self.num_vertices = 1
            self.distances = np.zeros((self.num_vertices, self.num_vertices))
        else:
            new_size = self.num_vertices + 1
            new_distances = np.zeros((new_size, new_size))
            new_distances[:self.num_vertices, :self.num_vertices] = self.distances
            self.distances = new_distances
            self.num_vertices = new_size

    def add_node(self, value):
        self.edges[value] = []
        self.nodes.add(value)
        

    def add_edge(self, from_node, to_node, distance):
        if self.distances is None:
            self.distances = np.zeros((self.num_vertices, self.num_vertices))
            
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance

    def dijkstra(self, initial_node):
        if initial_node not in self.nodes:
            return f"Узел {initial_node} отсутствует в графе"
        if initial_node not in self.edges:
            return f"Нет ребер, исходящих из узла {initial_node}"

        visited = np.inf * np.ones(self.num_vertices)
        visited[initial_node] = 0

        heap = TernaryHeap(size=self.num_vertices)
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

    def clean_up(self):
        self.edges = []
        self.vertices = []

    def run_dijkstra3(self, num_edges, q, r, results_file):
        num_vertices = self.num_vertices
        # Добавление ребер
        # Добавление ребер
        for vertex in range(num_vertices):
            for to_node in range(num_vertices):
                if vertex != to_node:
                    distance = random.randint(q, r)
                    self.add_edge(vertex, to_node, distance)
        initial_node = 0
        time = float(timeit.timeit(lambda: self.dijkstra(initial_node), number=1))
        
        result = [
            f"3-куча",
            num_vertices,
            num_edges,
            [q, r],
            toFixed(time, 6)
        ]
        
        with open(results_file, "a", encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(result)
        self.clean_up()
