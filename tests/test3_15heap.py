from graph3 import Graph3
from graph15 import Graph16
import random
# import timeit
import time
import matplotlib.pyplot as plt
import matplotlib
import gc
# import os
import re
import csv


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def run_dijkstra3(num_vertices, num_edges, q, r, results_file):
    graph = Graph3(num_vertices)
    
    # Добавление вершин
    for vertex in range(num_vertices):
        graph.add_node(vertex)
    
    # Добавление ребер
    for vertex in range(num_vertices):
        for to_node in range(num_vertices):
            if vertex != to_node:
                distance = random.randint(q, r)
                graph.add_edge(vertex, to_node, distance)
    
    def run_algorithm():
        initial_node = 0
        start_time = time.time()
        result = graph.dijkstra(initial_node)
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time
    
    result = [
        f"3-куча",
        num_vertices,
        num_edges,
        [q, r],
        toFixed(run_algorithm(), 2)
    ]
    
    with open(results_file, "a", encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(result)
    
    del graph
    gc.collect()


def run_dijkstra15(num_vertices, num_edges, q, r, results_file):
    graph = Graph16(num_vertices)
    
    # Добавление вершин
    for vertex in range(num_vertices):
        graph.add_node(vertex)
    
    # Добавление ребер
    for vertex in range(num_vertices):
        for to_node in range(num_vertices):
            if vertex != to_node:
                distance = random.randint(q, r)
                graph.add_edge(vertex, to_node, distance)
    
    def run_algorithm():
        initial_node = 0
        start_time = time.time()
        result = graph.dijkstra(initial_node)
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time
    
    result = [
        f"15-куча",
        num_vertices,
        num_edges,
        [q, r],
        toFixed(run_algorithm(), 2)
    ]
    
    with open(results_file, "a", encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(result)
    
    del graph
    gc.collect()


def first_test_a():
    results_file = "res_1a.csv"
    for n in range(1, 10001, 250):
        m = int(n ** 2 / 10)
        run_dijkstra3(n, m, 1, 1000000, results_file)
        run_dijkstra15(n, m, 1, 1000000, results_file)
        gc.collect()  # Вручную вызывается сборщик мусора после каждого запуска

def first_test_b():
    results_file = "res_1b.csv"
    for n in range(1, 10001, 250):
        m = n**2
        run_dijkstra3(n, m, 1, 1000000, results_file)
        run_dijkstra15(n, m, 1, 1000000, results_file)
        gc.collect()  # Manually invoke the garbage collector after each run

def second_test_a():
    results_file = "res_2a.csv"
    for n in range(1, 10001, 250):
        m = 100*n
        run_dijkstra3(n, m, 1, 1000000, results_file)
        run_dijkstra15(n, m, 1, 1000000, results_file)
        # results.append({'n': n, 'm': m, 'result': result})
        gc.collect()
    

def second_test_b():
    results_file = "res_2b.csv"
    for n in range(1, 10001, 250):
        m = 1000*n
        run_dijkstra3(n, m, 1, 1000000, results_file)
        run_dijkstra15(n, m, 1, 1000000, results_file)
        gc.collect()
    

def third_test():
    results_file = "res_3.csv"
    n = 10000 + 1
    for m in range(0, 10000000, 100000):
        run_dijkstra3(n, m, 1, 1000000, results_file)
        run_dijkstra15(n, m, 1, 1000000, results_file)
        gc.collect()
    

def fourth_test_a():
    results_file = "res_4a.csv"
    n = 10000 + 1
    for r in range(1, 200, 1):
        m = n**2
        run_dijkstra3(n, m, 1, 1000000, results_file)
        run_dijkstra15(n, m, 1, 1000000, results_file)
        gc.collect()

    

def fourth_test_b():
    results_file = "res_4b.csv"
    n = 10000 + 1
    for r in range(1, 200, 1):
        m = 1000*n
        run_dijkstra3(n, m, 1, r, results_file)
        run_dijkstra15(n, m, 1, r, results_file)
        gc.collect()


def parse_csv_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 5:
                algorithm = row[0]
                edge_count = int(row[1])
                vertex_count = int(row[2])
                range_values = eval(row[3])
                time = float(row[4])
                data.append((algorithm, edge_count, vertex_count, range_values, time))
    return data


def plot_graph(data, algorithm):
    x = [item[1] for item in data if item[0] == algorithm]
    y = [item[4] for item in data if item[0] == algorithm]
    plt.plot(x, y)
    plt.xlabel('Number of Edges and Vertices')
    plt.ylabel('Time')
    plt.title(f'Graph for {algorithm}')
    plt.show()

# def get_execution_time_from_file(results_file, search_string):
#     with open(results_file, "r", encoding='utf-8') as file:
#         for line in file:
#             if search_string in line:
#                 execution_time_str = line.split(": ")[1].strip()  # Проверьте, что правильно парсите время выполнения из строки
#                 return float(execution_time_str)
#     return 0.0  # Верните значение по умолчанию, если не удалось найти время выполнения



# def plot_graph(num_vertices_list, execution_time_3_list, execution_time_15_list):
#     plt.plot(num_vertices_list, execution_time_3_list, label="3-куча")
#     plt.plot(num_vertices_list, execution_time_15_list, label="15-куча")
#     plt.xlabel("Количество вершин")
#     plt.ylabel("Время выполнения (с)")
#     plt.title("График времени выполнения алгоритма Дейкстры")
#     plt.legend()
#     plt.show()
    

