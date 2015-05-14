'''
Created on May 13, 2015

Graph class used for breadth first search.

@author: Derek Dik
'''
from queue import Queue
from pygame.key import get_mods
from math import floor


class Graph(object):
    '''
    Class models a graph
    '''
        
    def _init_(self):
        '''
        Constructor
        '''
        self.vertices = []
        self.edges = []

    def __init__(self, obstacles):
        '''
        Constructor
        '''
        self.vertices = []
        self.edges = []
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                ]
        for obstacle in obstacles:
            grid[floor(obstacle.getY() / 28)][floor(obstacle.getX() / 28)] = 1
        print(grid)
        for row in range(0, 25):
            for column in range(0, 25):
                if grid[row][column] == 0:
                    vertex = Graph.Vertex(row, column)
                    self.vertices.append(vertex)
                    grid[row][column] = vertex
        
        for vertex in self.vertices:
            adjacent_vertices = []
            print("Add adjacencies to vertex:")
            vertex.print()
            if vertex.get_column() > 0:
                left_vertex = grid[vertex.get_row()][vertex.get_column() - 1]
                if left_vertex is not 1:
                    adjacent_vertices.append(left_vertex)
            if vertex.get_column() < 24:
                right_vertex = grid[vertex.get_row()][vertex.get_column() + 1]
                if right_vertex is not 1:
                    adjacent_vertices.append(right_vertex)
            if vertex.get_row() > 0:
                up_vertex = grid[vertex.get_row() - 1][vertex.get_column()]
                if up_vertex is not 1:
                    adjacent_vertices.append(up_vertex)
            if vertex.get_row() < 24:
                down_vertex = grid[vertex.get_row() + 1][vertex.get_column()]
                if down_vertex is not 1:
                    adjacent_vertices.append(down_vertex)       
            for adjacent_vertex in adjacent_vertices:
                if not vertex.has_edge(adjacent_vertex):
                    edge = self.Edge(vertex, adjacent_vertex)
                    print("Found adjacent vertex:")
                    adjacent_vertex.print()
                    vertex.add_edge(edge)
                    adjacent_vertex.add_edge(edge)
                    self.edges.append(edge)
    def copy(self):
        new_graph = Graph()
        new_graph.vertices = self.vertices.copy()
        new_graph.edges = self.vertices.copy()
    
    def BFS(self, current_x, current_y, goal_x, goal_y):
        # Convert x and y into row and column
        current_row = floor(current_y / 28)
        current_column = floor(current_x /28)
        goal_row = floor(goal_y / 28)
        goal_column = floor(goal_x /28)
        print("Goal Row: " + str(goal_row) + "\tGoal Column: " + str(goal_column))
        previous_stack = []
        # Check if the graph contains the requested vertex
        if self.has_vertex(current_row, current_column) and self.has_vertex(goal_row, goal_column):
            # For each vertex
            for vertex in self.vertices:
                # Mark the vertex as unvisited
                vertex.clear()
            # Create a new queue
            queue = Queue()
            # Mark the original vertex as visited
            current_vertex = self.get_vertex(current_row, current_column)
            current_vertex.mark()
            # Add the original vertex to the queue
            queue.put(current_vertex)
            # While the queue is not empty
            print("Breadth first traversal")
            while not queue.empty():
                # Dequeue
                vertex = queue.get()
                print("Vertex removed from queue:")
                vertex.print()
                print(queue.qsize())
                # For each for adjacent vertex
                for next_vertex in vertex.get_adjacent():
                    # If the vertex hasn't been visited
                    if not next_vertex.is_marked():
                        # Mark the vertex as visited
                        next_vertex.mark()
                        # Add the last vertex the stack of visited vertices
                        previous_stack.append(vertex)
                        print("Vertex added to previous stack:")
                        vertex.print()
                        # Add this vertex to the queue of vertices to visit
                        queue.put(next_vertex)
                       
            print("Traversal completed!")
            # Complete the search
            # Create a vertex to represent the goal
            goal_vertex = Graph.Vertex(goal_row, goal_column)
            # Start from the node before the target node and work backwards to the origin
            previous_vertex = previous_stack.pop()
            while (not previous_vertex.equals(goal_vertex)):
                previous_vertex = previous_stack.pop()

            # Continue popping the stack until you find the original vertex
            next_vertex = previous_stack.pop()
            while not next_vertex.equals(current_vertex):
                previous_vertex = next_vertex
                next_vertex = previous_stack.pop()
            return self.get_move(current_vertex, next_vertex)
        # Search cannot be completed
        print("Error! Player not found")
        return 0

    
    def get_move(self, vertex_1, vertex_2):
        if vertex_1.get_row() > vertex_2.get_row() and vertex_1.get_column() == vertex_2.get_column():
            # Return "Up"
            return 2
        elif vertex_1.get_row() < vertex_2.get_row() and vertex_1.get_column() == vertex_2.get_column():
            # Return "Down"
            return 3
        elif vertex_1.get_column() < vertex_2.get_column() and vertex_1.get_row() == vertex_2.get_row():
            # Return "Right"
            return 0
        elif vertex_1.get_column() > vertex_2.get_column() and vertex_1.get_row() == vertex_2.get_row():
            # Return "Left"
            return 1

        
    def has_vertex(self, row, column):
        ''' Function to determine if a given vertex exists within the graph ''' 
        for vertex in self.vertices:
            print("Row: " + str(vertex.get_row()) + "\tColumn: " + str(vertex.get_column()))
            if vertex.get_row() == row and vertex.get_column() == column:
                return True
        return False
    
    def get_vertex(self, row, column):
        ''' Function to access a vertex''' 
        for vertex in self.vertices:
            if vertex.get_row() == row and vertex.get_column() == column:
                return vertex
        return False

    class Vertex():
        _marked = False
        _edges = []
        adjacent_vertices = []
        def __init__(self, row, column):
            self._row = row
            self._column = column
        def mark(self):
            self._marked = True
        
        def is_marked(self):
            return self._marked
        
        def clear(self):
            self._marked = False
        
        def add_edge(self, edge):
            self._edges.append(edge)
            for vertex in edge.get_vertices():
                if vertex is not self:
                    self.adjacent_vertices.append(vertex)
        def get_row(self):
            return self._row
        def get_column(self):
            return self._column
        def has_edge(self, other_vertex):
            return self.adjacent_vertices.count(other_vertex) > 0
        
        def get_adjacent(self):
            return self.adjacent_vertices
        
        def equals(self, other_vertex):
            return self._row == other_vertex.get_row() and self._column == other_vertex.get_column()
        
        def print(self):
            print("Row:" + str(self.get_row()) + "\tColumn: " + str(self.get_column()) )
    class Edge():
        def __init__(self, vertex1, vertex2):
            self._vertices = [vertex1, vertex2]
        def get_vertices(self):
            return self._vertices