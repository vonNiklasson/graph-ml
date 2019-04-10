from typing import List, Tuple

from tf_agents.environments import py_environment

from Environment import EnvTools
from GraphTools import Creator, Tools
import networkx as nx
import math


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
        self._allowed_actions = EnvTools.create_action_set(self._node_count)

    def observation_spec(self):
        pass

    def action_spec(self):
        return self._allowed_actions

    def _step(self, action):

        """
        Step action for the machine learning algorithm.

        :param action: Tuple containing two integers, representing an edge to be added.
        :return reward: The reward for the suggested action.
        """

        reward = 0.0
        x, y = action

        if not Creator.add_edge(self.nxgraph, x+1, y+1):
            reward = 0.0
            # TODO: do we return here?
            raise NotImplementedError
        else:
            reward = 1.0
            new_state = EnvTools.get_state(self.nxgraph)
            EnvTools.evaluate_state()
            raise NotImplementedError



        pass

    def _reset(self):
        # Creates a new networkx graph structure
        self.nxgraph = Creator.from_node_count(self._node_count)
        return EnvTools.get_state(self.nxgraph)