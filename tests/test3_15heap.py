from graph3 import Graph3
from graph15 import Graph15
import random
import timeit
import matplotlib.pyplot as plt
import matplotlib

def third_test():
    g3 = Graph3()
    g15 = Graph15()
    for i in range(60):
        node = str(i)
        g3.add_node(node)
        g15.add_node(node)
    for i in range(60):
        for j in range(i + 1, 60):
            node1 = str(i)
            node2 = str(j)
    weight = random.randint(1, 500)
    for _ in range(120):
        g3.add_edge(node1, node2, weight)
        g15.add_edge(node1, node2, weight)
    t1 = timeit.timeit(lambda: g3.dijkstra('0'), number=1000)
    t2 = timeit.timeit(lambda: g15.dijkstra('0'), number=1000)

    print(f"60,120. 10 :3-куча: {t1:.6f} сек.")
    print("fafsa")
    print(f"15-куча: {t2:.6f} сек.")
    x = ['Троичная куча', 'Пятнадцатеричная куча']
    y = [t1, t2]
    plt.plot(x, y, marker='o')
    plt.title('Сравнение времени выполнения алгоритма Дейкстры на разных кучах')
    plt.xlabel('Куча')
    plt.ylabel('Время выполнения (сек)')
    plt.grid(True)
    plt.show()

# def third_test():
#     g3 = Graph3()
#     g15 = Graph15()
#     for i in range(60):
#         node = str(i)
#         g3.add_node(node)
#         g15.add_node(node)
#     for i in range(60):
#         for j in range(i + 1, 60):
#             node1 = str(i)
#             node2 = str(j)
#             weight = random.randint(1, 500)
#             g3.add_edge(node1, node2, weight)
#             g15.add_edge(node1, node2, weight + 1000)
#             g3.add_edge(node1, node2, weight)
#             g15.add_edge(node1, node2, weight)
#     t1 = timeit.timeit(lambda: g3.dijkstra('0'), number=1000)
#     t2 = timeit.timeit(lambda: g15.dijkstra('0'), number=1000)
#     print(f"⏱️ Время выполнения алгоритма Дейкстры на троичной куче: {t1} сек.")
#     print(f"⏱️ Время выполнения алгоритма Дейкстры на пятнадцатеричной куче: {t2} сек.")
#     x = ['Троичная куча', 'Пятнадцатеричная куча']
#     y = [t1, t2]
#     plt.plot(x, y, marker='o')
#     plt.title('Сравнение времени выполнения алгоритма Дейкстры на разных кучах')
#     plt.xlabel('Куча')
#     plt.ylabel('Время выполнения (сек)')
#     plt.grid(True)
#     plt.show()

def fourth_test():
    g3 = Graph3()
    g15 = Graph15()
    for i in range(80):
        node = str(i)
        g3.add_node(node)
        g15.add_node(node)
    for i in range(80):
        for j in range(i + 1, 80):
            node1 = str(i)
            node2 = str(j)
            weight = random.randint(1, 10)
            g3.add_edge(node1, node2, weight)
            g15.add_edge(node1, node2, weight)
    t1 = timeit.timeit(lambda: g3.dijkstra('0'), number=1000)
    t2 = timeit.timeit(lambda: g15.dijkstra('0'), number=1000)
    print(f"⏱️ Время выполнения алгоритма Дейкстры на троичной куче: {t1} сек.")
    print(f"⏱️ Время выполнения алгоритма Дейкстры на пятнадцатеричной куче: {t2} сек.")
    x = ['Троичная куча', 'Пятнадцатеричная куча']
    y = [t1, t2]
    plt.plot(x, y, marker='o')
    plt.title('Сравнение времени выполнения алгоритма Дейкстры на разных кучах')
    plt.xlabel('Куча')
    plt.ylabel('Время выполнения (сек)')
    plt.grid(True)
    plt.show()


def fifth_test():
    g3 = Graph3()
    g15 = Graph15()
    for i in range(100):
        node = str(i)
        g3.add_node(node)
        g15.add_node(node)
    for i in range(100):
        for j in range(i + 1, 100):
            node1 = str(i)
            node2 = str(j)
            weight = random.randint(1, 10)
            g3.add_edge(node1, node2, weight)
            g15.add_edge(node1, node2, weight)
    t1 = timeit.timeit(lambda: g3.dijkstra('0'), number=1000)
    t2 = timeit.timeit(lambda: g15.dijkstra('0'), number=1000)
    print(f"⏱️ Время выполнения алгоритма Дейкстры на троичной куче: {t1:.2f} сек.")
    print(f"⏱️ Время выполнения алгоритма Дейкстры на пятнадцатеричной куче: {t2:.2f} сек.")
    x = ['Троичная куча', 'Пятнадцатеричная куча']
    y = [t1, t2]
    plt.plot(x, y, marker='o')
    plt.title('Сравнение времени выполнения алгоритма Дейкстры на разных кучах')
    plt.xlabel('Куча')
    plt.ylabel('Время выполнения (сек)')
    plt.grid(True)
    plt.show()

def sixth_test():
    g3 = Graph3()
    g15 = Graph15()
    for i in range(130):
        node = str(i)
        g3.add_node(node)
        g15.add_node(node)
    for i in range(150):
        for j in range(i + 1, 130):
            node1 = str(i)
            node2 = str(j)
            weight = random.randint(1, 10)
            g3.add_edge(node1, node2, weight)
            g15.add_edge(node1, node2, weight)
    t1 = timeit.timeit(lambda: g3.dijkstra('0'), number=1000)
    t2 = timeit.timeit(lambda: g15.dijkstra('0'), number=1000)
    print(f"⏱️ Время выполнения алгоритма Дейкстры на троичной куче: {t1:.2f} сек.")
    print(f"⏱️ Время выполнения алгоритма Дейкстры на пятнадцатеричной куче: {t2:.2f} сек.")
    x = ['Троичная куча', 'Пятнадцатеричная куча']
    y = [t1, t2]
    plt.plot(x, y, marker='o')
    plt.title('Сравнение времени выполнения алгоритма Дейкстры на разных кучах')
    plt.xlabel('Куча')
    plt.ylabel('Время выполнения (сек)')
    plt.grid(True)
    plt.show()

def seventh_test():
    g3 = Graph3()
    g15 = Graph15()
    for i in range(150):
        node = str(i)
        g3.add_node(node)
        g15.add_node(node)
    for i in range(150):
        for j in range(i + 1, 150):
            node1 = str(i)
            node2 = str(j)
            weight = random.randint(1,10)
            g3.add_edge(node1, node2, weight)
            g15.add_edge(node1, node2, weight)
    t1 = timeit.timeit(lambda: g3.dijkstra('0'), number=1000)
    t2 = timeit.timeit(lambda: g15.dijkstra('0'), number=1000)
    print(f"⏱️ Время выполнения алгоритма Дейкстры на троичной куче: {t1:.2f} сек.")
    print(f"⏱️ Время выполнения алгоритма Дейкстры на пятнадцатеричной куче: {t2:.2f} сек.")
    x = ['Троичная куча', 'Пятнадцатеричная куча']
    y = [t1, t2]
    plt.plot(x, y, marker='o')
    plt.title('Сравнение времени выполнения алгоритма Дейкстры на разных кучах')
    plt.xlabel('Куча')
    plt.ylabel('Время выполнения (сек)')
    plt.grid(True)
    plt.show()

def eighth_test():
    g3 = Graph3()
    g15 = Graph15()
    for i in range(60):
        node = str(i)
        g3.add_node(node)
        g15.add_node(node)
    for i in range(60):
        for j in range(i + 1, 60):
            node1 = str(i)
            node2 = str(j)
            if i % 3 == 0:
                weight = random.randint(1, 20)
                g3.add_edge(node1, node2, weight)
                g15.add_edge(node1, node2, weight + 1000)
                g3.add_edge(node1, node2, weight)
                g15.add_edge(node1, node2, weight)
    t1 = timeit.timeit(lambda: g3.dijkstra('0'), number=1000)
    t2 = timeit.timeit(lambda: g15.dijkstra('0'), number=1000)
    print(f"⏱️ Время выполнения алгоритма Дейкстры на троичной куче: {t1:.2f} сек.")
    print(f"⏱️ Время выполнения алгоритма Дейкстры на пятнадцатеричной куче: {t2:.2f} сек.")
    x = ['Троичная куча', 'Пятнадцатеричная куча']
    y = [t1, t2]
    plt.plot(x, y, marker='o')
    plt.title('Сравнение времени выполнения алгоритма Дейкстры на разных кучах')
    plt.xlabel('Куча')
    plt.ylabel('Время выполнения (сек)')
    plt.grid(True)
    plt.show()

def test_rand():
    g3 = Graph3()
    g15 = Graph15()
    g3.generate_random_graph(30,50)
    g15.generate_random_graph(30, 50)
    t1 = timeit.timeit(lambda: g15.dijkstra('0'), number=1000)
    t2 = timeit.timeit(lambda: g3.dijkstra('0'), number=1000)
    print(f"Время выполнения алгоритма Дейкстры на пятнадцатеричной куче: {t1} сек.")
    print(f"Время выполнения алгоритма Дейкстры на троичной куче: {t2} сек.")
    g15.visualize_graph()
    g3.visualize_graph()
    #print(g.dijkstra('0'))
def test_poln():
    g3 = Graph3()
    g15 = Graph15()
    g3.generate_complete_graph(30)
    g15.generate_complete_graph(30)
    t1 = timeit.timeit(lambda: g15.dijkstra('0'), number=1000)
    t2 = timeit.timeit(lambda: g3.dijkstra('0'), number=1000)
    print(f"Время выполнения алгоритма Дейкстры на пятнадцатеричной куче: {t1} сек.")
    print(f"Время выполнения алгоритма Дейкстры на троичной куче: {t2} сек.")
    g15.visualize_graph()
    g3.visualize_graph()
    #print(g.dijkstra('0'))