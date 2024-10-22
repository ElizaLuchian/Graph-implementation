import unittest
import timeit
from Graph import Graph, generate_random_graph


class TestGraphMethods(unittest.TestCase):

    def test_edge_existence_and_retrieval(self):
        graph = generate_random_graph(1000, 2000)
        # Add some specific edges for testing
        graph.add_edge(0, 1, 5)
        graph.add_edge(1, 2, 10)

        # Test isEdge method time complexity
        def test_is_edge():
            return graph.has_edge(0, 1), graph.has_edge(1, 2), graph.has_edge(0, 2)

        is_edge_time = timeit.timeit(test_is_edge, number=1000)
        print("isEdge method time:", is_edge_time)

        # Test getCost method time complexity
        def test_get_cost():
            return graph.get_edge_cost(0, 1), graph.get_edge_cost(1, 2)

        get_cost_time = timeit.timeit(test_get_cost, number=1000)
        print("getCost method time:", get_cost_time)

        # Assertions based on expected time complexities
        self.assertLessEqual(is_edge_time, 0.002)  # Assuming O(1)
        self.assertLessEqual(get_cost_time, 0.002)  # Assuming O(1)

    def test_getting_first_or_next_edge(self):
        graph = generate_random_graph(1000, 2000)

        # Test parseNout and parseNin methods time complexity
        def test_parse_n_out_and_in():
            for vertex in graph.parse_vertices():
                for neighbor in graph.parse_outbound_neighbors(vertex):
                    pass
                for neighbor in graph.parse_inbound_neighbors(vertex):
                    pass

        parse_n_out_and_in_time = timeit.timeit(test_parse_n_out_and_in, number=1)
        print("parseNout and parseNin methods time:", parse_n_out_and_in_time)

        # Assertions based on expected time complexities
        self.assertLessEqual(parse_n_out_and_in_time, 0.001)  # Assuming O(1)

    def test_endpoints_and_attached_integer(self):
        graph = generate_random_graph(1000, 2000)

        # Test getVertices, getEdges, and getCost methods time complexity
        def test_get_vertices_edges_cost():
            return graph.get_total_vertices(), graph.get_total_edges(), graph.get_edge_cost(0, 1)

        get_vertices_edges_cost_time = timeit.timeit(test_get_vertices_edges_cost, number=1000)
        print("getVertices, getEdges, and getCost methods time:", get_vertices_edges_cost_time)

        # Test setCost method time complexity
        def test_set_cost():
            graph.set_edge_cost(0, 1, 15)

        set_cost_time = timeit.timeit(test_set_cost, number=1000)
        print("setCost method time:", set_cost_time)

        # Assertions based on expected time complexities
        self.assertLessEqual(get_vertices_edges_cost_time, 0.001)  # Assuming O(1)
        self.assertLessEqual(set_cost_time, 0.001)  # Assuming O(1)

    def test_total_number_of_vertices_or_edges(self):
        graph = generate_random_graph(1000, 2000)

        # Test getVertices and getEdges methods time complexity
        def test_get_vertices_edges():
            return graph.get_total_vertices(), graph.get_total_edges()

        get_vertices_edges_time = timeit.timeit(test_get_vertices_edges, number=1000)
        print("getVertices and getEdges methods time:", get_vertices_edges_time)

        # Assertions based on expected time complexities
        self.assertLessEqual(get_vertices_edges_time, 0.001)  # Assuming O(1)


#if __name__ == '__main__':
    #unittest.main()
