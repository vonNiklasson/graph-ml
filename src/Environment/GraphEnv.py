from typing import List, Tuple

import math
from tf_agents.environments import py_environment
from GraphTools import Creator, Tools
import networkx as nx
from networkx import algorithms


class GraphEnv(py_environment.PyEnvironment):

    _node_count: int = None
    """
    Number of nodes to create an environment from.
    """

    _allowed_edge_count: int = None
    """
    Number of allowed edges to assign in the graph.
    """

    nxgraph: nx.Graph = None
    """
    The networkx object representing the current graph we're working on.
    """

    state = [
        0,          # Components,
        0,          # Edges left,
        math.inf,   # Convergence rate,
        0,          # Total cost,
        [[]]        # Stochastic adjacency matrix
    ]

    _allowed_actions: List[Tuple[int, int]] = []
    """
    Contains a list of possible edges to do action on.
    Will be a list of tuples represented by origin and destination.
    Example: (0, 1) represents an edge from node 0 to node 1.
    """

    def __init__(self, node_count: int, allowed_edge_count: int=None):
        """
        Initialises a new environment for a graph.

        :param node_count: The number of nodes for the given graph.
        """
        super(GraphEnv, self).__init__()

        # Stores the node count locally
        self._node_count = node_count
        # Check if the number of allowed edges is empty
        if allowed_edge_count == 0:
            # Set the number of allowed edges to the number of nodes-1 (to create a minimum spanning graph)
            self._allowed_edge_count = node_count - 1
        else:
            # If it's set, we assign it
            self._allowed_edge_count = allowed_edge_count

        # Creates a list of allowed actions to take in the graph
        self._allowed_actions = GraphEnv.create_actions(self._node_count)

    @staticmethod
    def create_actions(node_count: int) -> [(int, int)]:
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

    def observation_spec(self):
        pass

    def action_spec(self):
        return self._allowed_actions

    def _step(self, action):

        """
        Step action for the machine learning algorithm

        :param action: Tuple containing two integers, representing an edge to be added
        :return reward: The reward for the suggested action. 
        """

        x,y = action
        reward


        if not Creator.add_edge(nxgraph,x+1,y+1):
            raise NotImplementedError
        else
            raise NotImplementedError


        pass

    def _reset(self):
        # Creates a new networkx graph structure
        self.nxgraph = Creator.from_node_count(self._node_count)
        return GraphEnv.get_state(self.nxgraph)

    @staticmethod
    def get_state(nxgraph: nx.Graph):
        a = Tools.get_neighbour_matrix(nxgraph)
        return [
            # Number of connected components
            nx.algorithms.components.number_connected_components(nxgraph),
            # Number of edges left to assign
            nxgraph.number_of_edges(),
            math.inf,   # Convergence rate
            0,          # Total edge cost
            a           # Stochastic adjacency matrix
        ]
