import numpy as np
import timeit
import random

import csv
from collections import defaultdict


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

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

class Graph15:
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
        heap = HexadecimalHeap(len(self.vertices))
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

    def clean_up(self):
        self.edges = []
        self.vertices = []

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
        time = float(timeit.timeit(lambda: self.dijkstra(initial_node), number=1))

        result = [
            f"15-куча",
            num_vertices,
            num_edges,
            weight_range[0], weight_range[1],
            toFixed(time, 6)
        ]

        with open(results_file, "a", encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(result)

