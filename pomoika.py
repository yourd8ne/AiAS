import multiprocessing
file_lock = multiprocessing.Lock()
def run_test(test_func):
    with file_lock:
        test_func()


# processes = [
# #     multiprocessing.Process(target=run_test, args=(first_test_a,)),
# #     multiprocessing.Process(target=run_test, args=(first_test_b,)),
# #     multiprocessing.Process(target=run_test, args=(second_test_a,)),
#     multiprocessing.Process(target=run_test, args=(second_test_b,)),
# #     multiprocessing.Process(target=run_test, args=(third_test,)),
#     multiprocessing.Process(target=run_test, args=(fourth_test_a,)),
#     multiprocessing.Process(target=run_test, args=(fourth_test_b,))
# ]

# for process in processes:
#     process.start()

# for process in processes:
#     process.join()

# test_graph()
# file_path = 'res_1a.csv'
# parsed_data = parse_csv_file(file_path)

# algorithm_3_heap = '3-куча'
# algorithm_15_heap = '15-куча'

# plot_graph_vertex(parsed_data, algorithm_3_heap)
# plot_graph_vertex(parsed_data, algorithm_15_heap)



class Graph3:

    def __init__(self):
        self.edges = defaultdict(list)
        self.nodes = set()

    def reset(self):
        self.num_vertices = 0
        self.edges.clear()
        self.distances = None
        self.nodes.clear()

    def add_vertex(self, num_vertices):
        self.num_vertices = num_vertices
        for i in range(num_vertices):
            self.nodes.add(i)


    def add_node(self, value):
        self.edges[value] = []
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        if from_node == to_node:
            return  # Игнорировать добавление ребра для петли

        self.edges[from_node].append(to_node)
        if self.distances is None:
            self.distances = np.zeros((self.num_vertices, self.num_vertices))
        self.distances[from_node, to_node] = distance

    def dijkstra(self, initial_node):
        if initial_node not in self.nodes:
            return f"Узел {initial_node} отсутствует в графе"
        if initial_node not in self.edges:
            return f"Нет ребер, исходящих из узла {initial_node}"

        visited = np.inf * np.ones(self.num_vertices)
        visited[initial_node] = 0

        heap = TernaryHeap(size=self.num_vertices)
        heap.push((0, initial_node))

        while heap.current_size > 0:
            current_weight, min_node = heap.pop()

            if current_weight != visited[min_node]:
                continue

            if min_node not in self.edges:
                continue

            for edge in self.edges[min_node]:
                if edge not in visited:
                    continue

                weight = current_weight + self.distances[min_node, edge]

                if weight < visited[edge]:
                    visited[edge] = weight
                    heap.push((weight, edge))

        return visited

    def run_test(self, num_vertices, num_edges, min_power, max_power):
        # Add vertices
        for _ in range(0, num_vertices):
            self.add_vertex(num_vertices)
    
    # Add edges with random powers
        for _ in range(num_edges):
            to_node = random.randint(0, num_vertices - 1)
            power = random.randint(min_power, max_power)
            self.add_edge(0, to_node, power)  # Add edge from node 0 to random node
    
    # Add remaining random edges between other nodes
        for _ in range(num_edges - 1):  # Subtract 1 to account for edge from node 0
            from_node = random.randint(1, num_vertices - 1)
            to_node = random.randint(1, num_vertices - 1)
            power = random.randint(min_power, max_power)
            self.add_edge(from_node, to_node, power)
        print(f"nodes {self.nodes}")
        print(f"edges {self.edges}")
        # Measure Dijkstra's algorithm
        start_time = timeit.default_timer()
        short_path = self.dijkstra(0)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time

        # Write results to CSV file
        results_file = "results.csv"
        result = [
            "3-куча",
            num_vertices,
            num_edges,
            [min_power, max_power],
            toFixed(execution_time, 6)
        ]
        
        with open(results_file, "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(result)
        print(short_path)
        self.print_graph()
        # Clean up
        self.reset()


    # def clean_up(self):
    #     self.edges = []
    #     self.vertices = []

    # def run_dijkstra3(self, num_edges, q, r, results_file):
    #     num_vertices = self.num_vertices
    #     # Добавление ребер
    #     for vertex in range(num_vertices):
    #         for to_node in range(num_vertices):
    #             if vertex != to_node:
    #                 distance = random.randint(q, r)
    #                 self.add_edge(vertex, to_node, distance)
    #     initial_node = 0
    #     time = float(timeit.timeit(lambda: self.dijkstra(initial_node), number=1))
        
    #     result = [
    #         f"3-куча",
    #         num_vertices,
    #         num_edges,
    #         [q, r],
    #         toFixed(time, 6)
    #     ]
        
    #     with open(results_file, "a", encoding='utf-8', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(result)
    #     self.clean_up()
    def print_graph(self):
        G = nx.Graph()
        G.add_nodes_from(self.nodes)

        for from_node in self.edges:
            for to_node in self.edges[from_node]:
                weight = self.distances[from_node, to_node]
                G.add_edge(from_node, to_node, weight=weight)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()