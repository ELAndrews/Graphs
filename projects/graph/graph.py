"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex doesn't exist")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        visitedNodes = set()

        while q.size() > 0:
            node = q.dequeue()
            if node not in visitedNodes:
                print(node)
                visitedNodes.add(node)
                for next_vertex in self.get_neighbors(node):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visitedNodes = set()

        while s.size() > 0:
            node = s.pop()
            if node not in visitedNodes:
                print(node)
                visitedNodes.add(node)
                for next_vertex in self.get_neighbors(node):
                    s.push(next_vertex)


    def dft_recursive(self, starting_vertex, visitedNodes=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in visitedNodes:
            print(starting_vertex)
            visitedNodes.add(starting_vertex)
            for v in self.get_neighbors(starting_vertex):
                self.dft_recursive(v, visitedNodes)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        if starting_vertex == destination_vertex:
            print(starting_vertex)
            return

        paths = Queue()
        paths.enqueue([starting_vertex])
        while paths.size():
            path = paths.dequeue()
            node = path[-1]
            if node == destination_vertex:
                return path
            else:
                for a in self.get_neighbors(node):
                    new_path = path+[a]
                    paths.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        path = []
        visitedNodes = set()
        stack = Stack()

        curr = starting_vertex
        stack.push(starting_vertex)

        while stack.size() and curr is not destination_vertex:

            if curr not in visitedNodes:
                visitedNodes.add(curr)
            unvisited_neighbours = [v for v in self.get_neighbors(curr) if v not in visitedNodes]
            if unvisited_neighbours:
                stack.push(curr)
                curr = unvisited_neighbours[0]
            else:
                curr = stack.pop()
        while stack.size():
            path.append(curr)
            curr = stack.pop()
        path.reverse()
        return path

    def dfs_recursive(self, starting_vertex, destination_vertex, visitedNodes=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex == destination_vertex:
            visitedNodes.add(starting_vertex)
            return [starting_vertex]

        if starting_vertex not in visitedNodes:
            visitedNodes.add(starting_vertex)
            for v in self.get_neighbors(starting_vertex):
                path = self.dfs_recursive(v, destination_vertex, visitedNodes)
                if path:
                    return [starting_vertex] + path



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
