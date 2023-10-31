from graph3 import Graph3
from graph15 import Graph15
import random
import timeit
import matplotlib.pyplot as plt
import matplotlib
import gc
import os


def run_dijkstra3(num_vertices, num_edges, q, r, results_file):
    graph = Graph3(num_vertices)
    
    # Добавление вершин
    for vertex in range(num_vertices):
        graph.add_node(vertex)
    
    # Добавление ребер
    for vertex in range(num_vertices):
        for _ in range(num_edges):
            to_node = random.randint(0, num_vertices-1)
            distance = random.randint(q, r)
            graph.add_edge(vertex, to_node, distance)
    
    # Замер времени выполнения
    def run_algorithm():
        initial_node = 0
        return graph.dijkstra(initial_node)
    
    execution_time = timeit.timeit(run_algorithm, number=1)
    formatted_execution_time = "{:.2f}".format(execution_time)
    result = f"3-куча {num_vertices} вершин, {num_edges} ребер, диапазон мощности [{q}, {r}]:\n    Время выполнения: {formatted_execution_time} с\n"
    
    with open(results_file, "a", encoding='utf-8') as file:
        file.write(result)
    
    del graph  # Удаление объекта графа
    gc.collect()  # Вручную вызывается сборщик мусора для освобождения памяти


def run_dijkstra15(num_vertices, num_edges, q, r, results_file):
    graph = Graph15(num_vertices)
    
    # Добавление вершин
    for vertex in range(num_vertices):
        graph.add_node(vertex)
    
    # Добавление ребер
    for vertex in range(num_vertices):
        for _ in range(num_edges):
            to_node = random.randint(0, num_vertices-1)
            distance = random.randint(q, r)
            graph.add_edge(vertex, to_node, distance)
    
    # Замер времени выполнения
    def run_algorithm():
        initial_node = 0
        return graph.dijkstra(initial_node)
    
    execution_time = timeit.timeit(run_algorithm, number=1)
    formatted_execution_time = "{:.2f}".format(execution_time)
    result = f"15-куча {num_vertices} вершин, {num_edges} ребер, диапазон мощности [{q}, {r}]:\n    Время выполнения: {formatted_execution_time} с\n"
    
    with open(results_file, "a", encoding='utf-8') as file:
        file.write(result)
    
    del graph  # Удаление объекта графа
    gc.collect()  # Вручную вызывается сборщик мусора для освобождения памяти


def first_test_a(results_file):
    num_vertices_list = []
    execution_time_3_list = []
    execution_time_15_list = []

    for n in range(1750, 10000, 250):
        m = int(n ** 2 / 10)
        run_dijkstra3(n, m, 1, 1000000, results_file)
        run_dijkstra15(n, m, 1, 1000000, results_file)
        gc.collect()  # Вручную вызывается сборщик мусора после каждого запуска

        num_vertices_list.append(n)
        execution_time_3 = get_execution_time_from_file(results_file, f"3-куча {n} вершин")
        execution_time_15 = get_execution_time_from_file(results_file, f"15-куча {n} вершин")
        execution_time_3_list.append(execution_time_3)
        execution_time_15_list.append(execution_time_15)

    plot_graph(num_vertices_list, execution_time_3_list, execution_time_15_list)

    

def first_test_b(results_file):
    num_vertices_list = []
    execution_time_3_list = []
    execution_time_15_list = []
    for n in range(1, 10000, 250):
        m = n**2
        run_dijkstra15(n, m, 1, 1000000)
        run_dijkstra15(n, m, 1, 1000000)
        gc.collect()  # Manually invoke the garbage collector after each run

        num_vertices_list.append(n)
        execution_time_3 = get_execution_time_from_file(results_file, f"3-куча {n} вершин")
        execution_time_15 = get_execution_time_from_file(results_file, f"15-куча {n} вершин")
        execution_time_3_list.append(execution_time_3)
        execution_time_15_list.append(execution_time_15)

    plot_graph(num_vertices_list, execution_time_3_list, execution_time_15_list)
    

def second_test_a(results_file):
    num_vertices_list = []
    execution_time_3_list = []
    execution_time_15_list = []
    for n in range(1, 10000, 250):
        m = 100*n
        run_dijkstra3(n, m, 1, 1000000)
        run_dijkstra15(n, m, 1, 1000000)
        # results.append({'n': n, 'm': m, 'result': result})
        gc.collect()

        num_vertices_list.append(n)
        execution_time_3 = get_execution_time_from_file(results_file, f"3-куча {n} вершин")
        execution_time_15 = get_execution_time_from_file(results_file, f"15-куча {n} вершин")
        execution_time_3_list.append(execution_time_3)
        execution_time_15_list.append(execution_time_15)

    plot_graph(num_vertices_list, execution_time_3_list, execution_time_15_list)
    

def second_test_b(results_file):
    num_vertices_list = []
    execution_time_3_list = []
    execution_time_15_list = []
    for n in range(1, 10000, 250):
        m = 1000*n
        run_dijkstra3(n, m, 1, 1000000)
        run_dijkstra15(n, m, 1, 1000000)
        # results.append({'n': n, 'm': m, 'result': result})
        gc.collect()

        num_vertices_list.append(n)
        execution_time_3 = get_execution_time_from_file(results_file, f"3-куча {n} вершин")
        execution_time_15 = get_execution_time_from_file(results_file, f"15-куча {n} вершин")
        execution_time_3_list.append(execution_time_3)
        execution_time_15_list.append(execution_time_15)

    plot_graph(num_vertices_list, execution_time_3_list, execution_time_15_list)
    

def third_test(results_file):
    num_vertices_list = []
    execution_time_3_list = []
    execution_time_15_list = []
    for n in range(1, 10000, 250):
        for m in range(0, 10000000, 100000):
            run_dijkstra3(n, m, 1, 1000000)
            run_dijkstra15(n, m, 1, 1000000)
            # results.append({'n': n, 'm': m, 'result': result})
            gc.collect()

            num_vertices_list.append(n)
            execution_time_3 = get_execution_time_from_file(results_file, f"3-куча {n} вершин")
            execution_time_15 = get_execution_time_from_file(results_file, f"15-куча {n} вершин")
            execution_time_3_list.append(execution_time_3)
            execution_time_15_list.append(execution_time_15)

    plot_graph(num_vertices_list, execution_time_3_list, execution_time_15_list)
    

def fourth_test_a(results_file):
    num_vertices_list = []
    execution_time_3_list = []
    execution_time_15_list = []
    for n in range(1, 10000, 250):
        for r in range(1, 200, 1):
            m = n**2
            run_dijkstra3(n, m, 1, 1000000)
            run_dijkstra15(n, m, 1, 1000000)
            # results.append({'n': n, 'm': m, 'result': result})
            gc.collect()

            num_vertices_list.append(n)
            execution_time_3 = get_execution_time_from_file(results_file, f"3-куча {n} вершин")
            execution_time_15 = get_execution_time_from_file(results_file, f"15-куча {n} вершин")
            execution_time_3_list.append(execution_time_3)
            execution_time_15_list.append(execution_time_15)

    plot_graph(num_vertices_list, execution_time_3_list, execution_time_15_list)
    

def fourth_test_b(results_file):
    num_vertices_list = []
    execution_time_3_list = []
    execution_time_15_list = []
    for n in range(1, 10000, 250):
        for r in range(1, 200, 1):
            m = 1000*n
            run_dijkstra3(n, m, 1, r)
            run_dijkstra15(n, m, 1, r)
            gc.collect()

            num_vertices_list.append(n)
            execution_time_3 = get_execution_time_from_file(results_file, f"3-куча {n} вершин")
            execution_time_15 = get_execution_time_from_file(results_file, f"15-куча {n} вершин")
            execution_time_3_list.append(execution_time_3)
            execution_time_15_list.append(execution_time_15)

    plot_graph(num_vertices_list, execution_time_3_list, execution_time_15_list)
        
def get_execution_time_from_file(results_file, search_string):
    with open(results_file, "r", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith(search_string):
                execution_time_str = line.split(":")[1].strip().split(" ")[0]
                return float(execution_time_str)

def plot_graph(num_vertices_list, execution_time_3_list, execution_time_15_list):
    plt.plot(num_vertices_list, execution_time_3_list, label="3-куча")
    plt.plot(num_vertices_list, execution_time_15_list, label="15-куча")
    plt.xlabel("Количество вершин")
    plt.ylabel("Время выполнения (с)")
    plt.title("График времени выполнения алгоритма Дейкстры")
    plt.legend()
    plt.show()