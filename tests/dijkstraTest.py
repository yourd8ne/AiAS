from graph3 import Graph3
from graph15 import Graph15

def first_test():
    g3 = Graph3(8)
    g3.add_node('A')
    g3.add_node('B')
    g3.add_node('C')
    g3.add_node('D')
    g3.add_node('E')
    g3.add_node('F')
    g3.add_node('G')
    g3.add_node('H')
    g3.add_edge('A', 'B', 8)
    g3.add_edge('A', 'C', 2)
    g3.add_edge('A', 'D', 7)
    g3.add_edge('B', 'E', 2)
    g3.add_edge('B', 'F', 2)
    g3.add_edge('C', 'F', 6)
    g3.add_edge('C', 'G', 7)
    g3.add_edge('D', 'E', 2)
    g3.add_edge('D', 'F', 4)
    g3.add_edge('E', 'H', 4)
    g3.add_edge('F', 'H', 9)
    g3.add_edge('G', 'H', 6)
    shortest_paths = g3.dijkstra('A')
    print(shortest_paths)
    
    g15 = Graph15(8)
    g15.add_node('A')
    g15.add_node('B')
    g15.add_node('C')
    g15.add_node('D')
    g15.add_node('E')
    g15.add_node('F')
    g15.add_node('G')
    g15.add_node('H')
    g15.add_edge('A', 'B', 8)
    g15.add_edge('A', 'C', 2)
    g15.add_edge('A', 'D', 7)
    g15.add_edge('B', 'E', 2)
    g15.add_edge('B', 'F', 2)
    g15.add_edge('C', 'F', 6)
    g15.add_edge('C', 'G', 7)
    g15.add_edge('D', 'E', 2)
    g15.add_edge('D', 'F', 4)
    g15.add_edge('E', 'H', 4)
    g15.add_edge('F', 'H', 9)
    g15.add_edge('G', 'H', 6)
    shortest_paths = g15.dijkstra('A')
    print(shortest_paths)

def second_test():
    g3 = Graph3(26)
    g15 = Graph15(26)
    g3.add_node('A')
    g15.add_node('A')
    
    for i in range(1, 26):
        g3.add_node(chr(ord('A') + i))
        #print(chr(ord('A') + i))
    
    for i in range(1, 26):
        g15.add_node(chr(ord('A') + i))
    
    g3.add_node('AA')
    g15.add_node('AA')
    g3.add_node('AB')
    g15.add_node('AC')
    g3.add_node('AD')
    g15.add_node('AD')
    g3.add_node('AE')
    g15.add_node('AE')
    g3.add_node('AF')
    g15.add_node('AF')
    g3.add_node('AG')
    g15.add_node('AG')
    g3.add_node('AH')
    g15.add_node('AH')
    g3.add_node('AI')
    g15.add_node('AI')
    g3.add_node('AJ')
    g15.add_node('AJ')
    g3.add_node('AK')
    g15.add_node('AK')
    g3.add_node('AL')
    g15.add_node('AL')
    g3.add_node('AM')
    g15.add_node('AM')
    g3.add_edge('A', 'B', 3)
    g3.add_edge('A', 'C', 4)
    g3.add_edge('A', 'D', 3)
    g3.add_edge('A', 'E', 6)
    g3.add_edge('B', 'F', 5)
    g3.add_edge('B', 'G', 5)
    g3.add_edge('C', 'G', 1)
    g3.add_edge('C', 'H', 5)
    g3.add_edge('D', 'K', 9)
    g3.add_edge('D', 'I', 3)
    g3.add_edge('E', 'L', 7)
    g3.add_edge('F', 'J', 2)
    g3.add_edge('F', 'K', 1)
    g3.add_edge('G', 'K', 3)
    g3.add_edge('H', 'L', 5)
    g3.add_edge('I', 'O', 4)
    g3.add_edge('I', 'M', 3)
    g3.add_edge('J', 'N', 7)
    g3.add_edge('K', 'N', 6)
    g3.add_edge('K', 'O', 3)
    g3.add_edge('L', 'P', 4)
    g3.add_edge('M', 'Q', 4)
    g3.add_edge('N', 'R', 2)
    g3.add_edge('O', 'S', 8)
    g3.add_edge('P', 'T', 5)
    g3.add_edge('Q', 'T', 5)
    g3.add_edge('Q', 'U', 5)
    g3.add_edge('R', 'V', 3)
    g3.add_edge('S', 'V', 3)
    g3.add_edge('T', 'V', 4)
    g3.add_edge('U', 'V', 2)
    g3.add_edge('U', 'X', 6)
    g3.add_edge('V', 'W', 4)
    g3.add_edge('V', 'Y', 3)
    g3.add_edge('V', 'X', 4)
    g3.add_edge('W', 'Z', 4)
    g3.add_edge('Y', 'Z', 6)
    g3.add_edge('X', 'Z', 4)
    
    g15.add_edge('A', 'B', 3)
    g15.add_edge('A', 'C', 4)
    g15.add_edge('A', 'D', 3)
    g15.add_edge('A', 'E', 6)
    g15.add_edge('B', 'F', 5)
    g15.add_edge('B', 'G', 5)
    g15.add_edge('C', 'G', 1)
    g15.add_edge('C', 'H', 5)
    g15.add_edge('D', 'K', 9)
    g15.add_edge('D', 'I', 3)
    g15.add_edge('E', 'L', 7)
    g15.add_edge('F', 'J', 2)
    g15.add_edge('F', 'K', 1)
    g15.add_edge('G', 'K', 3)
    g15.add_edge('H', 'L', 5)
    g15.add_edge('I', 'O', 4)
    g15.add_edge('I', 'M', 3)
    g15.add_edge('J', 'N', 7)
    g15.add_edge('K', 'N', 6)
    g15.add_edge('K', 'O', 3)
    g15.add_edge('L', 'P', 4)
    g15.add_edge('M', 'Q', 4)
    g15.add_edge('N', 'R', 2)
    g15.add_edge('O', 'S', 8)
    g15.add_edge('P', 'T', 5)
    g15.add_edge('Q', 'T', 5)
    g15.add_edge('Q', 'U', 5)
    g15.add_edge('R', 'V', 3)
    g15.add_edge('S', 'V', 3)
    g15.add_edge('T', 'V', 4)
    g15.add_edge('U', 'V', 2)
    g15.add_edge('U', 'X', 6)
    g15.add_edge('V', 'W', 4)
    g15.add_edge('V', 'Y', 3)
    g15.add_edge('V', 'X', 4)
    g15.add_edge('W', 'Z', 4)
    g15.add_edge('Y', 'Z', 6)
    g15.add_edge('X', 'Z', 4)
    shortest_paths = g3.dijkstra('A')
    print(shortest_paths)