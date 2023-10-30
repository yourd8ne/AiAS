from graph3 import Graph3
from graph15 import Graph15
import random
import timeit
import matplotlib.pyplot as plt
import matplotlib
import csv
import os

def write_to_csv(results, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['n', 'm', 'result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

def write_results_to_csv(results, function_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_dir, f'{function_name}_results.csv')
    write_to_csv(results, filename)

def run_dijkstra3(num_vertices, num_edges, q, r):
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
        formatted_execution_time = f"{num_vertices}, {num_edges}, [{q},{r}] 3-куча "+"{:.2f}".format(execution_time)
        print(f"3-куча {num_vertices},{num_edges}:\n    Execution Time: {formatted_execution_time} seconds")

def run_dijkstra15(num_vertices, num_edges, q, r):
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
        formatted_execution_time = f"{num_vertices}, {num_edges},[{q},{r}] 15-куча "+"{:.2f}".format(execution_time)
        print(f"15-куча {num_vertices},{num_edges}:\n   Execution Time: {formatted_execution_time} seconds")

def first_test_a():
    results = []
    for n in range(1, 10000, 100):
        m = int(n**2/10)
        result = run_dijkstra3(n, m, 1, 1000000)
        results.append({'n': n, 'm': m, 'result': result})
    write_results_to_csv(results, 'function_a')

def first_test_b():
    results = []
    for n in range(1, 10000, 100):
        m = n**2
        result = run_dijkstra15(n, m, 1, 1000000)
        results.append({'n': n, 'm': m, 'result': result})
    write_results_to_csv(results, 'function_b')

def second_test():
    # ;lsgdsgdgks
    print("hi")

def third_test():
    #run_dijkstra3(1000, 10)
    run_dijkstra15(1000, 10, 1, 1000000)

def fourth_test():
     run_dijkstra3(1000, 100)
     run_dijkstra15(1000, 100)

def fifth_test():
    run_dijkstra3(1000, 1000)
    run_dijkstra15(1000, 1000)
    
def sixth_test():
    run_dijkstra3(1000, 500)
    run_dijkstra15(1000, 500)

def seventh_test():
    run_dijkstra3(1000, 1000)
    run_dijkstra15(1000, 1000)

def eighth_test():
    run_dijkstra3(1000, 5000)
    run_dijkstra15(1000, 5000)

def ninth_test():
    run_dijkstra3(1000, 50000)
    run_dijkstra15(1000, 50000)

def tenth_test():
    run_dijkstra3(1000, 50000)
    run_dijkstra15(1000, 50000)

def eleventh_test():
    run_dijkstra3(1000, 25000)
    run_dijkstra15(1000, 25000)

def twelfth_test():
    # run_dijkstra3(1000, 10000)
    run_dijkstra15(1000, 10000)

def thirteenth_test():
    # run_dijkstra3(1000, 75000)
    run_dijkstra15(1000, 75000)
    
def fourteenth_test():
    run_dijkstra15(1000, 75000)
    run_dijkstra3(1000, 75000)

def fifteenth_test():
    run_dijkstra15(1000, 100000)
    run_dijkstra3(1000, 100000)

def test_rand():
    g3 = Graph3()
    g15 = Graph15()
    g3.generate_random_graph(100, 100000)
    g15.generate_random_graph(100, 10000)
    t1 = timeit.timeit(lambda: g3.dijkstra('0'), number=10)
    t2 = timeit.timeit(lambda: g15.dijkstra('0'), number=10)
    print(f"Случайный граф 100 вершин, 1000 ребер\nВремя выполнения алгоритма Дейкстры на троичной куче: {t1:6f} сек.")
    print(f"Время выполнения алгоритма Дейкстры на пятнадцатеричной куче: {t2:6f} сек.")
    #print(g.dijkstra('0'))
    g3.visualize_graph()
    g15.visualize_graph()
def test_poln(vertices):
    g3 = Graph3()
    g15 = Graph15()
    g3.generate_complete_graph(vertices)
    g15.generate_complete_graph(vertices)
    t1 = timeit.timeit(lambda: g3.dijkstra('0'), number=10)
    t2 = timeit.timeit(lambda: g15.dijkstra('0'), number=10)
    print(f"Полный граф\nВремя выполнения алгоритма Дейкстры на троичной куче: {t1:6f} сек.")
    print(f"Время выполнения алгоритма Дейкстры на пятнадцатеричной куче: {t2:6f} сек.")
    #print(g.dijkstra('0'))