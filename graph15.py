import random
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')


class HexadecimalHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return value

    def _sift_up(self, index):
        parent = (index - 1) // 15
        if parent >= 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)

    def _sift_down(self, index):
        smallest = index
        for i in range(1, 16):
            child = 15 * index + i
            if child < len(self.heap) and self.heap[child][0] < self.heap[smallest][0]:
                smallest = child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)


class Graph15:
    def __init__(self, num_vertices=None):
        self.nodes = set()
        self.edges = {}
        self.distances = {}
        self.num_vertices = num_vertices

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def dijkstra(self, initial_node):
        if initial_node not in self.nodes:
            return f"Узел {initial_node} отсутствует в графе"
        if initial_node not in self.edges:
            return f"Нет ребер, исходящих из узла {initial_node}"
        visited = {initial_node: 0}
        heap = HexadecimalHeap()
        heap.push((0, initial_node))
        while heap.heap:
            current_weight, min_node = heap.pop()
            if current_weight > visited[min_node]:
                continue
            for edge in self.edges[min_node]:
                weight = current_weight + self.distances[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    heap.push((weight, edge))
        return visited



    def generate_random_graph(self, num_nodes, num_edges):
        for i in range(num_nodes):
            self.add_node(str(i))
        
        available_nodes = [str(i) for i in range(num_nodes)]
        
        for _ in range(num_edges):
            if available_nodes:
                index1 = random.randint(0, len(available_nodes) - 1)
                node1 = available_nodes[index1]
                
                if available_nodes:
                    index2 = random.randint(0, len(available_nodes) - 1)
                    node2 = available_nodes[index2]
                    
                    self.add_edge(node1, node2, random.randint(1, 10))




    def generate_complete_graph(self, num_nodes):
        for i in range(num_nodes):
            self.add_node(str(i))
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                distance = random.randint(1, 10)
                self.add_edge(str(i), str(j), distance)

    def visualize_graph(self):
        G = nx.Graph()
        for node in self.nodes:
            G.add_node(node)
        for from_node in self.edges:
            for to_node in self.edges[from_node]:
                G.add_edge(from_node, to_node, weight=self.distances[(from_node, to_node)])
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
        plt.axis('off')
        plt.show()
