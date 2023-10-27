from graph3 import Graph3
from graph15 import Graph15
import random
import timeit
import matplotlib.pyplot as plt
import matplotlib

def run_graph3_test(num_vertices, num_edges, weight_range):
    graph = Graph3(num_vertices)

    # Создаем вершины
    for i in range(num_vertices):
        node = str(i)
        graph.add_node(node)

    # Создание ребер
    edges = set()  # Множество для хранения уже добавленных ребер

    while len(edges) < num_edges:
        node1 = str(random.randint(0, num_vertices - 1))
        node2 = str(random.randint(0, num_vertices - 1))

        # Убедимся, что ребро (node1, node2) или (node2, node1) еще не добавлено
        if (node1, node2) in edges or (node2, node1) in edges:
            continue

        weight = random.randint(weight_range[0], weight_range[1])

        graph.add_edge(node1, node2, weight)

        edges.add((node1, node2))

    # shortest_paths = graph.dijkstra('0')

    # print(f"Кратчайшие пути в графе с {num_vertices}-кучей:")
    # for node, distance in shortest_paths.items():
    #     print(f"{node}: {distance}")

    time = timeit.timeit(lambda: graph.dijkstra('0'), number=1)

    print(f"3-куча: {num_vertices} вершин, {num_edges} ребер, вес {weight_range}: {time:.4f} сек.")
    # graph.visualize_graph()

def run_graph15_test(num_vertices, num_edges, weight_range):
    graph = Graph15(num_vertices)

    # Создаем вершины
    for i in range(num_vertices):
        node = str(i)
        graph.add_node(node)

    # Создание ребер
    edges = set()  # Множество для хранения уже добавленных ребер

    while len(edges) < num_edges:
        node1 = str(random.randint(0, num_vertices - 1))
        node2 = str(random.randint(0, num_vertices - 1))

        # Убедимся, что ребро (node1, node2) или (node2, node1) еще не добавлено
        if (node1, node2) in edges or (node2, node1) in edges:
            continue

        weight = random.randint(weight_range[0], weight_range[1])

        graph.add_edge(node1, node2, weight)

        edges.add((node1, node2))

    shortest_paths = graph.dijkstra('0')

    # print(f"Кратчайшие пути в графе с {num_vertices}-кучей:")
    # for node, distance in shortest_paths.items():
    #     print(f"{node}: {distance}")

    time = timeit.timeit(lambda: graph.dijkstra('0'), number=1)

    print(f"15-куча: {num_vertices} вершин, {num_edges} ребер, вес {weight_range}: {time:.4f} сек.")
    # graph.visualize_graph()

def run_combined_test(num_vertices, num_edges, weight_range):
    print(f"Тест для графа с {num_vertices} вершинами и {num_edges} ребрами:")

    # Граф на троичной куче
    graph3 = Graph3(num_vertices)
    graph15 = Graph15(num_vertices)
    # Создаем вершины
    for i in range(num_vertices):
        node = str(i)
        graph3.add_node(node)
        graph15.add_node(node)

    # Создание ребер
    edges3 = set()  # Множество для хранения уже добавленных ребер
    edges15 = set()

    while len(edges3) < num_edges:
        node1 = str(random.randint(0, num_vertices - 1))
        node2 = str(random.randint(0, num_vertices - 1))

        # Убедимся, что ребро (node1, node2) или (node2, node1) еще не добавлено
        if (node1, node2) in edges3 or (node2, node1) in edges3:
            continue

        weight = random.randint(weight_range[0], weight_range[1])

        graph3.add_edge(node1, node2, weight)

        edges3.add((node1, node2))

    # Создаем вершины
    for i in range(num_vertices):
        node = str(i)
        graph15.add_node(node)


    while len(edges15) < num_edges:
        node3 = str(random.randint(0, num_vertices - 1))
        node4 = str(random.randint(0, num_vertices - 1))

        # Убедимся, что ребро (node1, node2) или (node2, node1) еще не добавлено
        if (node3, node4) in edges15 or (node4, node3) in edges15:
            continue

        weight2 = random.randint(weight_range[0], weight_range[1])

        graph15.add_edge(node3, node4, weight2)

        edges15.add((node3, node4))

    # Тест с троичной кучей
    time1 = timeit.timeit(lambda: graph3.dijkstra('0'), number=10)

    print(f"3-куча: {num_vertices} вершин, {num_edges} ребер, вес {weight_range}: {time1:.4f} сек.")

    # Тест с пятнадцатиричной кучей
    time2 = timeit.timeit(lambda: graph15.dijkstra('0'), number=10)

    print(f"15-куча: {num_vertices} вершин, {num_edges} ребер, вес {weight_range}: {time2:.4f} сек.\n")
    # print(graph3.dijkstra('0'))
    # print(graph15.dijkstra('0'))
    # graph3.visualize_graph()
    # graph15.visualize_graph()

def third_test():
    run_graph3_test(100, 200, [1, 500])
    run_graph15_test(100, 200, [1, 500])
    run_combined_test(100, 200, [1, 500])
    
    # test_poln(30)

def fourth_test():
    run_graph3_test(200, 400, [1, 500])
    run_graph15_test(200, 400, [1, 500])
    run_combined_test(200, 400, [1, 500])

def fifth_test():
    run_graph3_test(600, 200, [1, 500])
    run_graph15_test(600, 200, [1, 500])
    run_combined_test(600, 200, [1, 500])
    

def sixth_test():
    run_graph3_test(600, 600, [1, 500])
    run_graph15_test(600, 600, [1, 500])
    run_combined_test(600, 600, [1, 500])


def seventh_test():
    run_graph3_test(600, 1200, [1, 500])
    run_graph15_test(600, 1200, [1, 500])
    run_combined_test(600, 1200, [1, 500])


def eighth_test():
    run_graph3_test(600, 1500, [1, 500])
    run_graph15_test(600, 1500, [1, 500])
    run_combined_test(600, 1500, [1, 500])

def nineght_test():
    run_graph3_test(600, 1500, [1, 1000])
    run_graph15_test(600, 1500, [1, 1000])
    run_combined_test(600, 1500, [1, 1000])

def tenhth_test():
    run_graph3_test(600, 10000, [1, 500])
    run_graph15_test(600, 10000, [1, 500])
    run_combined_test(600, 10000, [1, 500])

def eleventh_test():
    run_graph3_test(1500, 10000, [1, 1000])
    run_graph15_test(1500, 10000, [1, 1000])
    run_combined_test(1500, 10000, [1, 1000])

def twelv_test():
    run_graph3_test(100, 10000, [1, 10])
    run_graph15_test(100, 10000, [1, 10])
    # run_combined_test(100, 10000, [1, 10])

def test_rand():
    g3 = Graph3()
    g15 = Graph15()
    g3.generate_random_graph(30,50)
    g15.generate_random_graph(30, 50)
    t1 = timeit.timeit(lambda: g15.dijkstra('0'), number=1)
    t2 = timeit.timeit(lambda: g3.dijkstra('0'), number=1)
    print(f"Время выполнения алгоритма Дейкстры на пятнадцатеричной куче: {t1} сек.")
    print(f"Время выполнения алгоритма Дейкстры на троичной куче: {t2} сек.")
    g15.visualize_graph()
    g3.visualize_graph()
    #print(g.dijkstra('0'))
def test_poln(vertices):
    g3 = Graph3()
    g15 = Graph15()
    g3.generate_complete_graph(vertices)
    g15.generate_complete_graph(vertices)
    t1 = timeit.timeit(lambda: g15.dijkstra('0'), number=1)
    t2 = timeit.timeit(lambda: g3.dijkstra('0'), number=1)
    print(f"Время выполнения алгоритма Дейкстры на пятнадцатеричной куче: {t1} сек.")
    print(f"Время выполнения алгоритма Дейкстры на троичной куче: {t2} сек.")
    g15.visualize_graph()
    g3.visualize_graph()
    #print(g.dijkstra('0'))