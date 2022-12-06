class Graph:

    class Edge:

        def __init__(self, node1, node2, weight, directed=False):
            self._node1 = node1
            self._node2 = node2
            self._weight = weight
            self._directed = directed

        def get_node1(self):
            return self._node1

        def get_node2(self):
            return self._node2

        def __str__(self):
            return str(self._node1) + " - " + str(self._node2)

    class Node:

        def __init__(self, data):
            self._data = data
            self._edges = []

        def __str__(self):
            return str(self._data)

        def get_data(self):
            return self._data

        def get_edges(self):
            return self._edges

        def add_edge(self, edge):
            self._edges.append(edge)

        def remove_edge(self, edge):
            self._edges.remove(edge)

        def __eq__(self, other):
            return self._data == other.get_data()

    def __init__(self):
        self._nodes = []

    def add_node(self, node):
        self._nodes.append(node)

    def remove_node(self, node):
        self._nodes.remove(node)

    def get_nodes(self):
        return self._nodes

    def connect(self, node1, node2, weight=1, directed=False):
        edge = self.Edge(node1, node2, weight, directed)
        node1.add_edge(edge)
        node2.add_edge(edge)
    
    def disconnect(self, node1, node2):
        for edge in node1.get_edges():
            if edge.get_node1() == node2 or edge.get_node2() == node2:
                node1.remove_edge(edge)
                node2.remove_edge(edge)
                return
    
    def __str__(self):
        string = ""
        for node in self._nodes:
            string += str(node) + ":\n"
            for edge in node.get_edges():
                string += "  " + str(edge) + "\n"
        
        return string
