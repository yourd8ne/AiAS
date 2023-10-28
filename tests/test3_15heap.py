from graph3 import Graph3
from graph15 import Graph15
import random
import timeit
import time
import matplotlib.pyplot as plt
import matplotlib

# def run_graph3_test(num_vertices, num_edges, weight_range):
#     graph = Graph3(num_vertices)

#     # Создаем вершины
#     for i in range(num_vertices):
#         node = str(i)
#         graph.add_node(node)

#     # Создание ребер
#     edges = set()  # Множество для хранения уже добавленных ребер

#     while len(edges) < num_edges:
#         node1 = str(random.randint(0, num_vertices - 1))
#         node2 = str(random.randint(0, num_vertices - 1))

#         # Убедимся, что ребро (node1, node2) или (node2, node1) еще не добавлено
#         if (node1, node2) in edges or (node2, node1) in edges:
#             continue

#         weight = random.randint(weight_range[0], weight_range[1])

#         graph.add_edge(node1, node2, weight)

#         edges.add((node1, node2))

#     # shortest_paths = graph.dijkstra('0')

#     # print(f"Кратчайшие пути в графе с {num_vertices}-кучей:")
#     # for node, distance in shortest_paths.items():
#     #     print(f"{node}: {distance}")

#     time = timeit.timeit(lambda: graph.dijkstra('0'), number=1)

#     print(f"3-куча: {num_vertices} вершин, {num_edges} ребер, вес {weight_range}: {time:.4f} сек.")
#     # graph.visualize_graph()

# def run_graph15_test(num_vertices, num_edges, weight_range):
#     graph = Graph15(num_vertices)

#     # Создаем вершины
#     for i in range(num_vertices):
#         node = str(i)
#         graph.add_node(node)

#     # Создание ребер
#     edges = set()  # Множество для хранения уже добавленных ребер

#     while len(edges) < num_edges:
#         node1 = str(random.randint(0, num_vertices - 1))
#         node2 = str(random.randint(0, num_vertices - 1))

#         # Убедимся, что ребро (node1, node2) или (node2, node1) еще не добавлено
#         if (node1, node2) in edges or (node2, node1) in edges:
#             continue

#         weight = random.randint(weight_range[0], weight_range[1])

#         graph.add_edge(node1, node2, weight)

#         edges.add((node1, node2))

#     shortest_paths = graph.dijkstra('0')

#     # print(f"Кратчайшие пути в графе с {num_vertices}-кучей:")
#     # for node, distance in shortest_paths.items():
#     #     print(f"{node}: {distance}")

#     time = timeit.timeit(lambda: graph.dijkstra('0'), number=1)

#     print(f"15-куча: {num_vertices} вершин, {num_edges} ребер, вес {weight_range}: {time:.4f} сек.")
#     # graph.visualize_graph()

# def run_combined_test(num_vertices, num_edges, weight_range):
#     print(f"Тест для графа с {num_vertices} вершинами и {num_edges} ребрами:")

#     # Граф на троичной куче
#     graph3 = Graph3(num_vertices)
#     graph15 = Graph15(num_vertices)
#     # Создаем вершины
#     for i in range(num_vertices):
#         node = str(i)
#         graph3.add_node(node)
#         graph15.add_node(node)

#     # Создание ребер
#     edges3 = set()  # Множество для хранения уже добавленных ребер
#     edges15 = set()

#     while len(edges3) < num_edges:
#         node1 = str(random.randint(0, num_vertices - 1))
#         node2 = str(random.randint(0, num_vertices - 1))

#         # Убедимся, что ребро (node1, node2) или (node2, node1) еще не добавлено
#         if (node1, node2) in edges3 or (node2, node1) in edges3:
#             continue

#         weight = random.randint(weight_range[0], weight_range[1])

#         graph3.add_edge(node1, node2, weight)

#         edges3.add((node1, node2))

#     # Создаем вершины
#     for i in range(num_vertices):
#         node = str(i)
#         graph15.add_node(node)


#     while len(edges15) < num_edges:
#         node3 = str(random.randint(0, num_vertices - 1))
#         node4 = str(random.randint(0, num_vertices - 1))

#         # Убедимся, что ребро (node1, node2) или (node2, node1) еще не добавлено
#         if (node3, node4) in edges15 or (node4, node3) in edges15:
#             continue

#         weight2 = random.randint(weight_range[0], weight_range[1])

#         graph15.add_edge(node3, node4, weight2)

#         edges15.add((node3, node4))

#     # Тест с троичной кучей
#     time1 = timeit.timeit(lambda: graph3.dijkstra('0'), number=10)

#     print(f"3-куча: {num_vertices} вершин, {num_edges} ребер, вес {weight_range}: {time1:.4f} сек.")

#     # Тест с пятнадцатиричной кучей
#     time2 = timeit.timeit(lambda: graph15.dijkstra('0'), number=10)

#     print(f"15-куча: {num_vertices} вершин, {num_edges} ребер, вес {weight_range}: {time2:.4f} сек.\n")
    # print(graph3.dijkstra('0'))
    # print(graph15.dijkstra('0'))
    # graph3.visualize_graph()
    # graph15.visualize_graph()

# def test_graph(num_vertices, num_edges):
#     graph = Graph3(num_vertices)
#     graph.generate_random_graph(num_vertices, num_edges)

#     distances = graph.dijkstra('0')
    
#     print(f"Количество вершин: {num_vertices}")
#     print(f"Количество ребер: {num_edges}")
#     t = timeit.timeit(lambda: graph.dijkstra('0'), number=100)
#     print(f"timeit: {t:.6f}")
#     # print("Расстояния от вершины '0':")
#     # for node, distance in distances.items():
#     #     print(f"Вершина {node}: {distance}")

# def test_graph():
#     num_vertices = 10
#     num_edges = 100

#     graph = Graph3(num_vertices)
#     # Добавление фиксированных ребер в граф
#     edges = [(0, 1, 5), (0, 2, 10), (1, 3, 8), (2, 3, 2), (2, 4, 6), (3, 5, 3), (4, 6, 1), (5, 6, 7), (5, 7, 12), (6, 8, 9),
#              (7, 8, 4), (8, 9, 11)]
#     graph.add_edge(edges)

#     distances = graph.dijkstra('0')

#     print(f"Количество вершин: {num_vertices}")
#     print(f"Количество ребер: {num_edges}")
#     t = timeit.timeit(lambda: graph.dijkstra('0'), number=100)
#     print(f"timeit: {t:.6f}")
#     # Вывод результатов
#     # print("Расстояния от вершины '0':")
#     # for node, distance in distances.items():
#     #     print(f"Вершина {node}: {distance}")

def run_dijkstra3(num_vertices, num_edges):
        graph = Graph3(num_vertices)
        
        # Добавление вершин
        for vertex in range(num_vertices):
            graph.add_node(vertex)
        
        # Добавление ребер
        for vertex in range(num_vertices):
            for _ in range(num_edges):
                to_node = random.randint(0, num_vertices-1)
                distance = random.randint(1, 10)
                graph.add_edge(vertex, to_node, distance)
        
        # Замер времени выполнения
        def run_algorithm():
            initial_node = 0
            return graph.dijkstra(initial_node)
        
        execution_time = timeit.timeit(run_algorithm, number=10)
        print(f"3-куча {num_vertices},{num_edges}:\n    Execution Time: {execution_time:.6f} seconds".format(execution_time))

def run_dijkstra15(num_vertices, num_edges):
        graph = Graph15(num_vertices)
        
        # Добавление вершин
        for vertex in range(num_vertices):
            graph.add_node(vertex)
        
        # Добавление ребер
        for vertex in range(num_vertices):
            for _ in range(num_edges):
                to_node = random.randint(0, num_vertices-1)
                distance = random.randint(1, 10)
                graph.add_edge(vertex, to_node, distance)
        
        # Замер времени выполнения
        def run_algorithm():
            initial_node = 0
            return graph.dijkstra(initial_node)
        
        execution_time = timeit.timeit(run_algorithm, number=10)
        print(f"15-куча {num_vertices},{num_edges}:\n   Execution Time: {execution_time:.6f} seconds".format(execution_time))

def third_test():
    run_dijkstra3(10, 10)
    run_dijkstra15(10, 10)

def fourth_test():
     run_dijkstra3(10, 100)
     run_dijkstra15(10, 100)

def fiveth_test():
    run_dijkstra3(100, 1000)
    run_dijkstra15(100, 1000)
    
def sixth_test():
    run_dijkstra3(1000, 500)
    run_dijkstra15(1000, 500)

def seventh_test():
    run_dijkstra3(1000, 1000)
    run_dijkstra15(1000, 1000)

def eight_test():
    run_dijkstra3(1000, 5000)
    run_dijkstra15(1000, 5000)

def nineth_test():
    run_dijkstra3(1000, 50000)
    run_dijkstra15(1000, 50000)

def tenth_test():
    run_dijkstra3(10000, 50000)
    run_dijkstra15(10000, 50000)

def eleventh_test():
    run_dijkstra3(10000, 100000)
    run_dijkstra15(10000, 100000)

def twelve_test():
    run_dijkstra3(10000, 500000)
    run_dijkstra15(10000, 500000)

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