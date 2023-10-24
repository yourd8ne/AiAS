import random
import networkx as nx
# import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class TernaryHeap:
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
        parent = (index - 1) // 3
        if parent >= 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)
    
    def _sift_down(self, index):
        child1 = 3 * index + 1
        child2 = 3 * index + 2
        child3 = 3 * index + 3
        smallest = index
        if child1 < len(self.heap) and self.heap[child1][0] < self.heap[smallest][0]:
            smallest = child1
        if child2 < len(self.heap) and self.heap[child2][0] < self.heap[smallest][0]:
            smallest = child2
        if child3 < len(self.heap) and self.heap[child3][0] < self.heap[smallest][0]:
            smallest = child3
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)
    
class Graph3:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}
    
    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []
    
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def dijkstra(self, initial_node):
        visited = {initial_node: 0}
        heap = TernaryHeap()
        heap.push((0, initial_node))
        while heap.heap:
            (current_weight, min_node) = heap.pop()
            if current_weight > visited[min_node]:
                continue
            for edge in self.edges[min_node]:
                weight = current_weight + self.distances[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    heap.push((weight, edge))
        return visited
    
    def generate_random_graph(self, num_nodes, num_edges):
        self.add_node('0')
        for i in range(1, num_nodes):
            self.add_node(str(i))
        available_edges = [(str(i), str(j)) for i in range(num_nodes) for j in range(num_nodes) if i != j]
        random.shuffle(available_edges)
        for k in range(num_edges):
            edge = available_edges[k]
            self.add_edge(edge[0], edge[1], random.randint(1, 10))
    
    def generate_complete_graph(self, num_nodes):
        for i in range(num_nodes):
            self.add_node(i)
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                distance = random.randint(1, 10)
                self.add_edge(i, j, distance)
                self.add_edge(j, i, distance)
    
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