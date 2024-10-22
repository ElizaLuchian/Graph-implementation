from Graph import save_graph_to_file, parse_graph_from_file, generate_random_graph


def print_menu():
    print("\nMenu:")
    print("1. Print graph information")
    print("2. Check if there is an edge between two vertices")
    print("3. Add an edge")
    print("4. Remove a vertex")
    print("5. Get cost of an edge")
    print("6. Set cost of an edge")
    print("7. Print outbound neighbors of a vertex")
    print("8. Print inbound neighbors of a vertex")
    print("9.print vertices")
    print ("12. BFS ------connected components")
    print("13. Find lowest cost walk")
    print("14. Check if graph is a DAG")
    print("15. Perform topological sort")
    print("16. Calculate earliest and latest starting times")
    print("17. Find critical activities")
    print("0. Exit")

def print_graph_info(graph):
    print("Number of vertices: ", graph.get_total_vertices())
    print("Number of edges: ", graph.get_total_edges())

def check_edge(graph):
    x = int(input("From: "))
    y = int(input("To: "))
    if graph.has_edge(x, y):
        print("Exists edge from ", x, " to ", y)
    else:
        print("No edge from ", x, " to ", y)

def add_edge(graph):
    x = int(input("Enter source vertex: "))
    y = int(input("Enter destination vertex: "))
    cost = int(input("Enter cost: "))
    graph.add_edge(x, y, cost)
    print("Edge added from ", x, " to ", y, " with cost ", cost)
    graph.add_edge(y, x, cost)
    print("Edge added from ", y, " to ", x, " with cost ", cost)

def remove_vertex(graph):
    vertex_id = int(input("Enter vertex to remove: "))
    graph.remove_vertex(vertex_id)
    print("Vertex", vertex_id, "removed")

def get_edge_cost(graph):
    x = int(input("Enter source vertex: "))
    y = int(input("Enter destination vertex: "))
    cost = graph.get_edge_cost(x, y)
    if cost is not None:
        print("Cost of edge from", x, "to", y, "is", cost)
    else:
        print("There is no edge from", x, "to", y)

def set_edge_cost(graph):
    x = int(input("Enter source vertex: "))
    y = int(input("Enter destination vertex: "))
    new_cost = int(input("Enter new cost: "))
    graph.set_edge_cost(x, y, new_cost)
    print("Cost of edge from", x, "to", y, "set to", new_cost)

def print_outbound_neighbors(graph):
    vertex_id = int(input("Enter vertex: "))
    neighbors = graph.parse_outbound_neighbors(vertex_id)
    print("Outbound neighbors of", vertex_id, ":", neighbors)

def print_inbound_neighbors(graph):
    vertex_id = int(input("Enter vertex: "))
    neighbors = graph.parse_inbound_neighbors(vertex_id)
    print("Inbound neighbors of", vertex_id, ":", neighbors)


def generate_two_files():
    # Generate random graphs
    random_graph1_filename = 'random_graph1.txt'
    try:
        random_graph1 = generate_random_graph(7, 20)
        save_graph_to_file(random_graph1, random_graph1_filename)
        print("Random graph 1 saved to", random_graph1_filename)
    except Exception as e:
        with open(random_graph1_filename, 'w') as file:
            file.write(f"Error generating random graph 1: {str(e)}")
        print("Error occurred while generating random graph 1:", str(e))

    random_graph2_filename = 'random_graph2.txt'
    try:
        random_graph2 = generate_random_graph(6, 40)
        save_graph_to_file(random_graph2, random_graph2_filename)
        print("Random graph 2 saved to", random_graph2_filename)
    except Exception as e:
        with open(random_graph2_filename, 'w') as file:
            file.write(f"Error generating random graph 2: {str(e)}")
        print("Error occurred while generating random graph 2:", str(e))

def BFSMain(graph):
    graph.BFS()
def BellMannFord(graph, start_vertex, end_vertex):
    graph.find_lowest_cost_walk(start_vertex, end_vertex)

def check_dag(graph):
    if graph.is_dag():
        print("The graph is a DAG")
    else:
        print("The graph is not a DAG")

def perform_topological_sort(graph):
    topo_sort = graph.topological_sort()
    print("Topological sort order:", topo_sort)

def calculate_earliest_latest_times(graph):
    earliest_start, latest_start, total_project_time = graph.calculate_earliest_latest_times()
    print("Earliest starting times:", earliest_start)
    print("Latest starting times:", latest_start)
    print("Total project time:", total_project_time)

def find_critical_activities(graph):
    critical_activities = graph.critical_activities()
    print("Critical activities:", critical_activities)

generate_two_files()
filename = "graphuletz3"
graph = parse_graph_from_file(str(filename) + ".txt")

while True:
    print_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        print_graph_info(graph)
    elif choice == '2':
        check_edge(graph)
    elif choice == '3':
        add_edge(graph)
    elif choice == '4':
        remove_vertex(graph)
    elif choice == '5':
        get_edge_cost(graph)
    elif choice == '6':
        set_edge_cost(graph)
    elif choice == '7':
        print_outbound_neighbors(graph)

    elif choice == '8':
        print_inbound_neighbors(graph)
    elif choice == '13':
        start_vertex = int(input("Enter start vertex: "))
        end_vertex = int(input("Enter end vertex: "))
        BellMannFord(graph, start_vertex, end_vertex)
    elif choice == '14':
        check_dag(graph)
    elif choice == '15':
        perform_topological_sort(graph)
    elif choice == '16':
        calculate_earliest_latest_times(graph)
    elif choice == '17':
        find_critical_activities(graph)
    elif choice == '18':
        print(graph.is_dag())
    elif choice == '19':
        print(graph.topological_sort())


    elif choice == '12':
        BFSMain(graph)

    elif choice == '0':
        save_graph_to_file(graph, str(filename) + "-modified.txt")
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8 or 0.")
