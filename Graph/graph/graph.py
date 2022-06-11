class Vertex:
    """
    this class is used to create a vertex.
    
    """
    def __init__(self, value):
        self.value = value
class Edge:
    """
    this class is used to create an edge.
    """
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
class Graph():
    """
    this class is used to create a graph.
    """
    def __init__(self):
        self.adjacency_list = {}
        
    def add_node(self,value):
        """
        A method to add a node to the graph.
        Input:the value of the node.
        Output: the node.
        """
        vertex=Vertex(value)
        self.adjacency_list[vertex]=[]
        return vertex
    
    def add_edge(self,node1,node2,weight=0):
        """
        A method to add an edge to the graph.
        Input: the nodes and the weight of the edge.
        Output: Nothing.
        """
        if (node1 in self.adjacency_list.keys()) or (node2 in self.adjacency_list.keys()):
            edge = Edge(node2, weight=weight)
            self.adjacency_list[node1].append(edge)
        else:
            raise ValueError("Node not in graph")  
         
    def get_nodes(self):
        """
        A method to get all the nodes in the graph.
        Input: Nothing.
        Output: A list of all the nodes in the graph.
        """
        nodes=[]
        [nodes.append(node.value) for node in self.adjacency_list.keys()]   
        return nodes
    
    def size(self):
        """
        A method to get the size of the graph.
        Input: Nothing.
        Output: The size of the graph.
        """
        return len(self.adjacency_list.keys())
    
    def get_neighbors(self,node):
        if not (node in self.adjacency_list.keys()):
            raise Exception("The node is not in the graph")
        else:
            output=[]
            [output.append([edge.value.value,edge.weight]) for edge in self.adjacency_list[node]] 
            return output
        
    def __str__(self):
        output = ''
        for node in self.adjacency_list.keys():
            output += f"{node.value} -> "

            for edge in self.adjacency_list[node]:
                output += f' {edge.value.value} -> '
            
            output += 'Null\n'
        return output    
    
if __name__ == '__main__':
    graph = Graph()
    a=graph.add_node('A')
    b=graph.add_node('B')
    c=graph.add_node('C')
    d=graph.add_node('D')
    e=graph.add_node('E')
    f=graph.add_node('F')
    g=graph.add_node('G')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, e)
    graph.add_edge(b, f)
    graph.add_edge(c, g)


    print(graph.get_nodes())
    print(graph)    