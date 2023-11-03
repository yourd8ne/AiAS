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
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, source, destination, weight):
        if source in self.vertices:
            self.vertices[source].append(destination)
        else:
            self.vertices[source] = [destination]

        self.edges[(source, destination)] = weight

    def dijkstra(self, source):
        # Инициализация расстояний до всех вершин как бесконечность
        distance = {vertex: float('inf') for vertex in self.vertices}
        # Расстояние до исходной вершины равно 0
        distance[source] = 0

        # Создание и инициализация пирамиды
        heap = TernaryHeap(len(self.vertices))
        for vertex in self.vertices:
            heap.push((distance[vertex], vertex))

        while heap.current_size > 0:
            # Извлечение вершины с наименьшим расстоянием из пирамиды
            _, current_vertex = heap.pop()

            # Проход по смежным вершинам
            for neighbor in self.vertices[current_vertex]:
                # Расчет нового расстояния до смежной вершины
                new_distance = distance[current_vertex] + self.edges[(current_vertex, neighbor)]
                # Если новое расстояние меньше текущего расстояния,
                if new_distance < distance[neighbor]:
                    # обновляем расстояние
                    distance[neighbor] = new_distance
                    # и добавляем вершину в пирамиду
                    heap.push((new_distance, neighbor))

        return distance

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

    def generate_graph(self, num_vertices, num_edges, weight_range, results_file):
        for i in range(num_vertices):
            self.add_vertex(i)

        for i in range(num_edges):
            source = random.randint(0, num_vertices - 1)
            destination = random.randint(0, num_vertices - 1)
            distance = random.randint(weight_range[0], weight_range[1])
            if destination != 0 and destination != 1:
                while source == destination:
                    destination = random.randint(0, num_vertices - 1)
            self.add_edge(source, destination, distance)

        initial_node = 0
        time = float(timeit.timeit(lambda: self.dijkstra(initial_node), number=1))

        result = [
            f"3-куча",
            num_vertices,
            num_edges,
            weight_range[0], weight_range[1],
            toFixed(time, 6)
        ]

        with open(results_file, "a", encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(result)
        