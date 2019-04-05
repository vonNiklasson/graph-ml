from tf_agents.environments import py_environment


class GraphEnv(py_environment.PyEnvironment):

    _node_count: int = None
    """
    """
    state = [
        # Components,
        # Edges left,
        # Convergence rate,
        # Total cost,
        # Neighbour matrix
    ]

    _allowed_actions = []

    def __init__(self, node_count):
        super(GraphEnv, self).__init__()

        self._node_count = node_count

    @staticmethod
    def create_actions(node_count):
        actions = []
        for origin in range(0, node_count):
            for dest in range(origin+1, node_count):
                actions.append((origin, dest))

        return actions

    def observation_spec(self):
        pass

    def action_spec(self):
        return self._allowed_actions

    def _step(self, action):
        pass

    def _reset(self):
        self._allowed_actions = GraphEnv.create_actions(self._node_count)
        pass
