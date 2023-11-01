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
        {num_vertices},
        {num_edges},
        [{q}, {r}],
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
        {num_vertices},
        {num_edges},
        [{q}, {r}],
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
        run_dijkstra15(n, m, 1, 1000000, results_file)
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


def parse_results(results_file):
    data_3 = []
    data_15 = []
    with open(results_file, "r", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            match = re.search(r"\d+-куча (\d+) вершин, (\d+) ребер.*\n.*Время выполнения: ([\d.]+) с", line)
            if match:
                try:
                    vertices = int(match.group(1))
                    edges = int(match.group(2))
                    execution_time = float(match.group(3))
                    if vertices > 0 or edges >= 0:
                        if "3-куча" in line:
                            data_3.append(execution_time)
                        elif "15-куча" in line:
                            data_15.append(execution_time)
                except (ValueError, IndexError):
                    continue
    print(data_3)
    print(data_15)
    return data_3, data_15

def plot_results(results_file):
    data_3, data_15 = parse_results(results_file)
    
    # Генерация входных данных
    x = range(1, len(data_3) + 1)
    
    # Построение графика
    plt.plot(x, data_3, label="3-куча")
    plt.plot(x, data_15, label="15-куча")
    
    # Настройка осей и легенды
    plt.xlabel("Входные данные")
    plt.ylabel("Время выполнения (с)")
    plt.legend()
    
    # Отображение графика
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
    

