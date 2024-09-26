# Undirectional Graph to be precise

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        try:
            _ = self.adj_list[vertex]
            return False 
        except KeyError:
            self.adj_list[vertex] = []
            return True
    
    def add_edge(self, vertex1, vertex2):
        try:
            v1_edges = self.adj_list[vertex1]
            v2_edges = self.adj_list[vertex2]
            for edge in v1_edges:
                if edge == vertex2:
                    return False 
            for edge in v2_edges:
                if edge == vertex1:
                    return False 
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        except KeyError:
            return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
            return False
        try:
            self.adj_list[vertex1].remove(vertex2)
            self.adj_list[vertex2].remove(vertex1)
        except ValueError:
            return False
        return True
    
    def remove_vertex(self, vertex):
        if vertex not in self.adj_list:
            return False 
        for v in self.adj_list[vertex]:
            self.adj_list[v].remove(vertex)
        
        del self.adj_list[vertex]
        return True





my_graph = Graph()

my_graph.add_vertex('A')

my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    A : []

"""