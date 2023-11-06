import numpy as np
import random
import gc
import time
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
        while index > 0:
            parent = (index - 1) // 3
            if self.heap[index][0] >= self.heap[parent][0]:
                break
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent

    def _sift_down(self, index):
        while True:
            smallest = index
            for i in range(1, 4):
                child = 3 * index + i
                if child < self.current_size and self.heap[child][0] < self.heap[smallest][0]:
                    smallest = child
            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest


class Graph3:
    def __init__(self):
        self.vertices = {}
        self.edges = defaultdict(dict)

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, source, destination, weight):
        if source in self.vertices:
            self.vertices[source].append(destination)
        else:
            self.vertices[source] = [destination]

        self.edges[source][destination] = weight

    def dijkstra(self, source):
        distance = {vertex: float('inf') for vertex in self.vertices}
        distance[source] = 0
        heap = TernaryHeap(len(self.vertices))
        for vertex in self.vertices:
            heap.push((distance[vertex], vertex))

        while heap.current_size > 0:
            _, current_vertex = heap.pop()

            for neighbor in self.vertices[current_vertex]:
                if current_vertex not in self.edges or neighbor not in self.edges[current_vertex]:
                    print(f"Ошибка: вершины {current_vertex} и/или {neighbor} отсутствуют в списке смежности")
                    continue
                new_distance = distance[current_vertex] + self.edges[current_vertex][neighbor]
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heap.push((new_distance, neighbor))

        return distance

    def generate_graph(self, num_vertices, num_edges, weight_range, results_file):
        for i in range(num_vertices):
            self.add_vertex(i)

        for i in range(num_edges):
            source = random.randint(0, num_vertices - 1)
            destination = random.randint(0, num_vertices - 1)
            distance = random.randint(weight_range[0], weight_range[1])
            if destination != 0 and destination != 1:
                while source == destination or destination == 0:
                    destination = random.randint(0, num_vertices - 1)
            self.add_edge(source, destination, distance)

        initial_node = 0
        start_time = time.time()
        shortest_path = self.dijkstra(initial_node)
        end_time = time.time()
        execution_time = end_time - start_time
        # print(shortest_path)
        result = [
            f"3-куча",
            num_vertices,
            num_edges,
            weight_range[0], weight_range[1],
            toFixed(execution_time, 6)
        ]

        with open(results_file, "a", encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(result)

    def draw_graph(self):
        G = nx.Graph()

        for vertex, edges in self.vertices.items():
            G.add_node(vertex)

        edge_labels = {}
        for (source, destination), weight in self.edges.items():
            G.add_edge(source, destination, weight=weight)
            edge_labels[(source, destination)] = weight

        pos = nx.spring_layout(G)
        labels = {vertex: vertex for vertex in G.nodes}

        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        nx.draw_networkx_labels(G, pos, labels=labels)

        plt.show()

    def clear(self):
        self.vertices = {}
        self.edges = defaultdict(dict)
