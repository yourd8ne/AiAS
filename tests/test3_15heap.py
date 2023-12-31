from graph3 import Graph3
from graph15 import Graph15
import gc
import random
import time
import csv
import matplotlib.pyplot as plt
import numpy as np

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def first_test_a():
    results_file = "res_1a.csv"
    for n in range(1, 10001, 100):
        g3 = Graph3()
        g15 = Graph15()
        m = int(n ** 2 / 10)
        g3.generate_graph(n, m, (1, 1000000), results_file)
        g15.generate_graph(n, m, (1, 1000000), results_file)
    gc.collect()  # Вручную вызывается сборщик мусора после каждого запуска


def first_test_b():
    results_file = "res_1b.csv"
    for n in range(7501, 10001, 100):
        g3 = Graph3()
        g15 = Graph15()
        m = n ** 2
        g3.generate_graph(n, m, (1, 1000000), results_file)
        g15.generate_graph(n, m, (1, 1000000), results_file)
    gc.collect()  # Вручную вызывается сборщик мусора после каждого запуска


def second_test_a():
    results_file = "res_2a.csv"
    for n in range(1, 10001, 100):
        g3 = Graph3()
        g15 = Graph15()
        m = 100 * n
        g3.generate_graph(n, m, (1, 1000000), results_file)
        g15.generate_graph(n, m, (1, 1000000), results_file)
    gc.collect()


def second_test_b():
    results_file = "res_2b.csv"
    for n in range(3701, 10001, 100):
        g3 = Graph3()
        g15 = Graph15()
        m = 1000 * n
        g3.generate_graph(n, m, (1, 1000000), results_file)
        g15.generate_graph(n, m, (1, 1000000), results_file)
    gc.collect()


def third_test():
    results_file = "res_3.csv"
    n = 10000 + 1
    for m in range(9500000, 10000000, 100000):
        g3 = Graph3()
        g15 = Graph15()
        g3.generate_graph(n, m, (1, 1000000), results_file)
        g15.generate_graph(n, m, (1, 1000000), results_file)


def fourth_test_a():
    def update_edge_weights(graph, r):
        for source, destinations in graph.edges.items():
            for destination, weight in destinations.items():
                graph.edges[source][destination] = random.randint(1, r)

    g3 = Graph3()
    g15 = Graph15()
    results_file = "res_4a.csv"
    n = 10000 + 1
    m = n ** 2

    # Создаем вершины графа
    for i in range(n):
        g3.add_vertex(i)
        g15.add_vertex(i)

    # Создаем ребра графа
    for i in range(m):
        source = random.randint(0, n - 1)
        destination = random.randint(0, n - 1)
        distance = random.randint(1, 1)  # Здесь временно используем 1 в качестве дефолтного значения веса

        if destination != 0 and destination != 1:
            while source == destination or destination == 0:
                destination = random.randint(0, n - 1)

        g3.add_edge(source, destination, distance)
        g15.add_edge(source, destination, distance)

    initial_node = 0

    for r in range(60, 200, 1):
        # Обновляем веса ребер
        update_edge_weights(g3, r)
        update_edge_weights(g15, r)

        start_time = time.time()
        shortest_path3 = g3.dijkstra(initial_node)
        end_time = time.time()
        execution_time3 = end_time - start_time

        start_time = time.time()
        shortest_path15 = g15.dijkstra(initial_node)
        end_time = time.time()
        execution_time15 = end_time - start_time

        result3 = [
            f"3-куча",
            n,
            m,
            1, r,
            toFixed(execution_time3, 6)
        ]

        result15 = [
            f"15-куча",
            n,
            m,
            1, r,
            toFixed(execution_time15, 6)
        ]

        with open(results_file, "a", encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(result3)
            writer.writerow(result15)


def fourth_test_b():
    g3 = Graph3()
    g15 = Graph15()
    results_file = "res_4b.csv"
    n = 10000 + 1
    m = 1000 * n
    for r in range(42, 67, 1):
        for i in range(n):
            g3.add_vertex(i)
            g15.add_vertex(i)

        for i in range(m):
            source = random.randint(0, n - 1)
            destination = random.randint(0, n - 1)
            distance = random.randint(1, r)
            if destination != 0 and destination != 1:
                while source == destination or destination == 0:
                    destination = random.randint(0, n - 1)
            g3.add_edge(source, destination, distance)
            g15.add_edge(source, destination, distance)

        initial_node = 0
        start_time = time.time()
        shortest_path3 = g3.dijkstra(initial_node)
        end_time = time.time()
        execution_time3 = end_time - start_time

        start_time = time.time()
        shortest_path15 = g15.dijkstra(initial_node)
        end_time = time.time()
        execution_time15 = end_time - start_time
        # print(shortest_path)
        result3 = [
            f"3-куча",
            n,
            m,
            1, r,
            toFixed(execution_time3, 6)
        ]
        result15 = [
            f"15-куча",
            n,
            m,
            1, r,
            toFixed(execution_time15, 6)
        ]

        with open(results_file, "a", encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(result3)
            writer.writerow(result15)
