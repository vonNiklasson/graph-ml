import networkx as nx
import numpy
from random import randint


class Creator:

    def __init__(self, netx):
        pass

    @classmethod
    def from_node_count(cls, node_count):
        area_dimension = node_count
        netx = nx.Graph()  # type: nx.Graph

        node_set = {}

        for n in range(0, node_count):
            coordinates = None
            while coordinates is None or coordinates in node_set:
                coordinates = (
                    randint(0, area_dimension),
                    randint(0, area_dimension)
                )
            netx.add_node(n, coordinates=coordinates)

        return netx



    @classmethod
    def from_dict(cls, g):
        """

        :param g:
        :return:
        :rtype: networkx.Graph
        """
        netx = nx.Graph()  # type: nx.Graph
        nodes = g["V"]
        edges = g["E"]

        for node_id, node in nodes.items():
            netx.add_node(node_id, value=node[0], coordinates=node[1])

        for origin, destinations in edges.items():
            for destination in destinations:
                Creator.add_edge(netx, origin, destination)
                #print origin, destination

        return netx

    @staticmethod
    def add_edge(g, start, destination):
        # find start & end coordinates
        start_cord = g.node[start]['coordinates']
        destination_cord = g.node[destination]['coordinates']

        # subtract the coordinate values of the two points
        delta = tuple(numpy.subtract(destination_cord, start_cord))
        # the difference in position is squared
        delta = numpy.square(delta)
        # extract values from delta tuple
        deltax, deltay = delta
        # cost is the summation of the difference in x and y
        weight = deltax + deltay

        #add edge to graph
        g.add_edge(start, destination, weight=weight)

