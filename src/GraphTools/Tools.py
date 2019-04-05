import numpy as np
from numpy import linalg as LA


class Tools:

    @staticmethod
    def get_neighbour_matrix(g):
        """

        :type g: networkx
        """
        # Sort the nodes in the graph
        s_nodes = list(g.nodes())
        s_nodes.sort()
        # Get the dimension of each row
        dim = len(s_nodes)

        # Create an empty row
        row = [0] * dim
        A = []
        for node in g.nodes():
            row = [0] * dim
            # Get the index of the current node
            node_index = s_nodes.index(node)
            row[node_index] = 1
            # Get the number of neighbours
            neighbour_count = 0
            for neighbour in g.neighbors(node):
                node_index = s_nodes.index(neighbour)
                row[node_index] = 1
                neighbour_count += 1
            row_divide = float(neighbour_count + 1)
            row = map(lambda x: x / row_divide, row)
            A.append(row)
        return A

    @staticmethod
    def get_eigenvalues(a):
        A = np.array(a)
        w, _ = LA.eig(A)
        return w

    @staticmethod
    def second_largest(numbers):
        count = 0
        m1 = m2 = float('-inf')
        for x in numbers:
            count += 1
            if x > m2:
                if x >= m1:
                    m1, m2 = x, m1
                else:
                    m2 = x
        return m2 if count >= 2 else None

    @staticmethod
    def convergence_rate(g):
        A = Tools.get_neighbour_matrix(g)
        ev = Tools.get_eigenvalues(A)
        return Tools.second_largest(ev)

    @staticmethod
    def total_edge_cost(g):
        """
        Calculates the total cost of all edges in the given graph.

        :param g: A networkx object with nodes and edges.
        :return: The total cost of all edges in the graph.
        """
        raise NotImplementedError
