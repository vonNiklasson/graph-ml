from GraphTools import Tools

import math
import networkx as nx


class EnvTools:

    @staticmethod
    def create_action_set(node_count: int) -> [(int, int)]:
        """
        Creates a set of actions for adding edges in a graph with node_count nodes.
        Will result in a n(n-1)/2 number of actions.

        :param node_count: The number of nodes to create actions of.
        :return: A list of tuples, representing actions to take.
        """
        # Creates an empty list of actions
        actions: [(int, int)] = []
        # Iterate through all nodes, representing <origin>
        for origin in range(0, node_count):
            # Iterate through all nodes larger than origin, representing <destination>.
            for dest in range(origin+1, node_count):
                # Add edge to actions
                actions.append((origin, dest))

        return actions

    @staticmethod
    def get_state(nxgraph: nx.Graph):
        """
        Converts a networkx bi-directional graph into the current state of the environment.

        :param nxgraph: A bi-directional networkx object
        :return state: [
            connected components,
            edges left to place,
            convergence rate,
            total edge cost
            stochastic adjacency matrix
        ]
        """

        connected_components = nx.algorithms.components.number_connected_components(nxgraph)
        a = Tools.get_neighbour_matrix(nxgraph)
        return [
            # Number of connected components
            connected_components,
            # Number of edges left to assign
            nxgraph.number_of_edges(),
            math.inf,   # Convergence rate
            0,          # Total edge cost
            a           # Stochastic adjacency matrix
        ]

    @staticmethod
    def is_final_state(state):
        """
        Function to see if the current state is the final state of the environment. This occurrs when there are no more edges to be added.

        :param state: State of the environment
        :return: Returns true/false depending on if the state is final
        """
        connected_components, edges_left, convergence_rate, edge_cost, adjacency_matrix = state

        if edges_left == 0:
            return True
        
        raise NotImplementedError

        pass

    @staticmethod
    def calculate_reward(state, previous_state):
        """
        Function to calculate the reward from a step taken depending on the change of state in the environment.

        :param state: The current state resulted from making a step.
        :param previous_state: The previously existing state before the step.
        
        return: Reward based on x,y,z
        """

        raise NotImplementedError
        pass
