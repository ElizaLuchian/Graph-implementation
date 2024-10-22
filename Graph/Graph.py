import random
from collections import deque

# Define an iterator for outbound neighbors of a vertex
class OutNeighborIterator:
    def __init__(self, graph, vertex):
        self._graph = graph
        self._vertex = vertex
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._graph._dictOutLength[self._vertex]:
            neighbor = self._graph._dictOut[self._vertex][self._index]
            self._index += 1
            return neighbor
        else:
            raise StopIteration


# Define an iterator for inbound neighbors of a vertex
class InNeighborIterator:
    def __init__(self, graph, vertex):
        self._graph = graph
        self._vertex = vertex
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._graph._dictInLength[self._vertex]:
            neighbor = self._graph._dictIn[self._vertex][self._index]
            self._index += 1
            return neighbor
        else:
            raise StopIteration


# Define a directed graph class
class Graph:
    """A directed graph, represented as two maps,
    one from each vertex to the set of outbound neighbours,
    the other from each vertex to the set of inbound neighbours"""

    def __init__(self, num_vertices):
        """Creates a graph with num_vertices vertices and no edges"""
        self._vertices = num_vertices
        self._edges = 0

        # Initialize dictionaries to store outbound and inbound neighbors
        self._dictOutLength = [0] * num_vertices
        self._dictOut = {i: [] for i in range(num_vertices)}

        self._dictInLength = [0] * num_vertices
        self._dictIn = {i: [] for i in range(num_vertices)}

        self._edge_costs = {}  # Store edge costs

    # Methods for parsing vertices and neighbors
    def parse_vertices(self):
        """Returns an iterable containing all the vertices"""
        return self._dictOut.keys()

    def parse_outbound_neighbors(self, vertex):
        """Returns an iterable containing the outbound neighbors of a vertex"""
        return self._dictOut[vertex]

    def parse_inbound_neighbors(self, vertex):
        """Returns an iterable containing the inbound neighbors of a vertex"""
        return self._dictIn[vertex]

    # Method to check if there is an edge between two vertices
    def has_edge(self, x, y):
        """Returns True if there is an edge from x to y, False otherwise"""
        return y in self._dictOut[x] if self._dictOutLength[x] > 0 and self._dictInLength[y] > 0 else False

    # Method to add an edge between two vertices
    def add_edge(self, x, y, cost):
        """Adds an edge from x to y"""
        if x not in self._dictOut.keys():
            self.add_vertex(x)


        if y in self._dictOut[x]:
            return

        # Update dictionaries and edge count
        self._dictOut[x].append(y)
        self._dictOutLength[x] += 1

        self._dictIn[y].append(x)
        self._dictInLength[y] += 1

        self._edge_costs[(x, y)] = cost
        self._edges += 1

    def in_degree(self, x):
        return self._dictInLength[x]

    def out_degree(self, x):
        return self._dictOutLength[x]

    # Method to get the total number of edges
    def get_total_edges(self):
        return self._edges

    # Method to get the total number of vertices
    def get_total_vertices(self):
        return self._vertices

    # Method to get the cost of an edge
    def get_edge_cost(self, x, y):
        """Returns the cost of the edge from x to y"""
        return self._edge_costs.get((x, y))

    # Method to set the cost of an edge
    def set_edge_cost(self, x, y, new_cost):
        """Updates the cost of the edge from x to y"""
        if self.has_edge(x, y):
            self._edge_costs[(x, y)] = new_cost

    # Method to add a vertex
    def add_vertex(self, vertex_id):
        """Adds a vertex to the graph"""
        if vertex_id not in self._dictOut:
            self._dictOut[vertex_id] = []
            self._dictIn[vertex_id] = []
            self._vertices += 1

    # Method to remove a vertex
    def remove_vertex(self, vertex_id):
        """Removes a vertex from the graph"""
        if vertex_id in self._dictOut:
            for neighbor in self._dictOut[vertex_id]:
                self._dictIn[neighbor].remove(vertex_id)
                del self._edge_costs[(vertex_id, neighbor)]
                self._edges -= 1

            for neighbor in self._dictIn[vertex_id]:
                self._dictOut[neighbor].remove(vertex_id)
                del self._edge_costs[(neighbor, vertex_id)]
                self._edges -= 1

            del self._dictOut[vertex_id]
            del self._dictIn[vertex_id]
            self._vertices -= 1

    # Method to create a copy of the graph
    def copy(self):
        copied_graph = Graph(0)
        for vertex_id in self.parse_vertices():
            copied_graph.add_vertex(vertex_id)
        for x in self.parse_vertices():
            for y in self.parse_outbound_neighbors(x):
                copied_graph.add_edge(x, y, self.get_edge_cost(x, y))
        return copied_graph

    def BFS(self):
        qui = deque()
        frequency = []
        conexe = []
        for it in range(0, self._vertices):
            frequency.append(0)
        for index in range(0, self._vertices):

            if frequency[index] == 0:
                qui.append(index)
                frequency[index] = frequency[index] + 1
                while len(qui) != 0:
                    x = qui.popleft()
                    conexe.append(x)
                    #frequency[x] = frequency[x] + 1
                    for i in self._dictOut[x]:
                        if frequency[i]==0:
                            frequency[i]=frequency[i]+1
                            qui.append(i)

                for ii in conexe:
                    print(ii, end=" ")
                print()
                #print(len(conexe))
                conexe.clear()

    def find_lowest_cost_walk(self, start_vertex, end_vertex):
        num_vertices = self.get_total_vertices()
        d = []
        for i in range(num_vertices):
            row = []
            for j in range(num_vertices + 1):
                row.append(float('inf'))
            d.append(row)


        p = []
        for i in range(num_vertices):
            row = []
            for j in range(num_vertices + 1):
                row.append(None)
            p.append(row)
        d[start_vertex][0] = 0

        for k in range(1, num_vertices + 1):
            for x in self.parse_vertices():
                for y in self.parse_inbound_neighbors(x):
                    if d[y][k - 1] != float('inf'):
                        new_cost = self.get_edge_cost(y, x) + d[y][k - 1]
                        if new_cost < d[x][k]:
                            d[x][k] = new_cost
                            p[x][k] = y

        # Check for negative cost cycles
        for x in self.parse_vertices():
            if d[x][num_vertices] < d[x][num_vertices - 1]:
                print("Negative cost cycle reachable from the starting vertex.")
                return

        # Find the minimum cost and corresponding number of edges used
        min_cost = float('inf')
        min_cost_k = -1
        for k in range(num_vertices + 1):
            if d[end_vertex][k] < min_cost:
                min_cost = d[end_vertex][k]
                min_cost_k = k

        if min_cost == float('inf'):
            print("There is no walk between the given vertices.")
        else:
            print(f"Lowest cost walk between vertices {start_vertex} and {end_vertex}: {min_cost}")
            # Reconstruct the path
            path = []
            current_vertex = end_vertex
            current_k = min_cost_k
            while current_k > 0:
                path.append(current_vertex)
                current_vertex = p[current_vertex][current_k]
                current_k -= 1
            path.append(start_vertex)
            path.reverse()
            print("Path:", path)

    def is_dag(self):
        """Check if the graph is a DAG using Tarjan's algorithm"""
        self._visited = [False] * self._vertices
        self._on_stack = [False] * self._vertices
        self._has_cycle = False
        self._stack = []

        def dfs(v):
            self._visited[v] = True
            self._on_stack[v] = True
            self._stack.append(v)

            for neighbor in self.parse_outbound_neighbors(v):
                if not self._visited[neighbor]:
                    dfs(neighbor)
                elif self._on_stack[neighbor]:
                    self._has_cycle = True

            self._on_stack[v] = False
            self._stack.pop()

        for vertex in self.parse_vertices():
            if not self._visited[vertex]:
                dfs(vertex)

        return not self._has_cycle

    def topological_sort(self):
        visited = set()
        stack = []

        def dfs(vertex):
            visited.add(vertex)
            for neighbor in self.parse_outbound_neighbors(vertex):
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(vertex)

        for v in self.parse_vertices():
            if v not in visited:
                dfs(v)

        stack.reverse()
        return stack

    def calculate_earliest_latest_times(self):
        """Calculate earliest and latest starting times for each activity"""
        topo_sort = self.topological_sort()
        num_vertices = self._vertices
        earliest_end = []
        latest_end = []
        time=0
        total_time=0

        for n in range(num_vertices):
            earliest_end.append([0, 0])
        for n in range(num_vertices):
            latest_end.append([float('inf'), float('inf')])


        # Calculate earliest start times
        for u in topo_sort:
            for v in self.parse_outbound_neighbors(u):
                if earliest_end[v][0] < earliest_end[u][0] + self.get_edge_cost(u, v):
                    earliest_end[v][0] = earliest_end[u][0] + self.get_edge_cost(u, v)
                    earliest_end[v][1] = self.get_edge_cost(u, v)
                    print(u, v, earliest_end[v])


        for el in earliest_end:
            total_time = max(total_time, el[0])

        # Initialize latest end times for vertices with no outbound edges
       # for u in range(num_vertices):
           # if self.out_degree(u) == 0:
        print(total_time)
        latest_start=[0]*num_vertices
        print(num_vertices)
        latest_start[num_vertices-1] = total_time
        print(latest_start)
        #print(latest_end)
        # Calculate latest start times
        for u in reversed(topo_sort):
            for v in self.parse_inbound_neighbors(u):
                    #print(latest_start)
                    #print( self.get_edge_cost(u, v))
                    #print(latest_start[u])
                    print(u)
                    latest_start[v]=latest_start[u]-self.get_edge_cost(u,v)

        earliest_start = [0] * num_vertices
        # Compute starts
        for vertex, el in enumerate(earliest_end):
            earliest_start[vertex] = el[0] - el[1]

        #latest_start = [0] * num_vertices
        # Compute starts
       # for vertex, el in enumerate(latest_end):
            #latest_start[vertex] = el[0]

        return earliest_start, latest_start, total_time

    def find_critical_activities(self):
        """Find the critical activities in the project"""
        earliest_start, latest_start, total_time = self.calculate_earliest_latest_times()
        critical_activities = []
        for u in range(self._vertices):
            for v in self.parse_outbound_neighbors(u):
                if earliest_start[u] == latest_start[v] - self.get_edge_cost(u, v):
                    critical_activities.append((u, v))
        return critical_activities








# Function to parse graph data from a file
def parse_graph_from_file(filename):
    with open(filename, 'r') as file:
        num_vertices, num_edges = map(int, file.readline().split())
        graph = Graph(num_vertices)
        for _ in range(num_edges):
            x, y, cost = map(int, file.readline().split())
            graph.add_edge(x, y, cost)
           # graph.add_edge(y, x, cost)
    return graph


# Function to save graph data to a file
def save_graph_to_file(graph, filename):
    with open(filename, 'w') as file:
        file.write(f"{graph.get_total_vertices()} {graph.get_total_edges()}\n")
        for vertex in graph.parse_vertices():
            for neighbor in graph.parse_outbound_neighbors(vertex):
                cost = graph.get_edge_cost(vertex, neighbor)
                file.write(f"{vertex} {neighbor} {cost}\n")




def generate_random_graph(num_vertices, num_edges):
    if num_edges > num_vertices * (num_vertices - 1):
        raise ValueError("Number of edges exceeds the maximum possible for the given number of vertices")

    graph = Graph(num_vertices)

    # Generate edges
    edges_generated = 0
    while edges_generated < num_edges:
        x = random.randint(0, num_vertices - 1)
        y = random.randint(0, num_vertices - 1)
        if x != y and not graph.has_edge(x, y):
            cost = random.randint(1, 100)  # Assuming a cost range from 1 to 100
            graph.add_edge(x, y, cost)
            edges_generated += 1

    return graph

