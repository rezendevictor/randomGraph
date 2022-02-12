# {
#	A:
#	{
#		connect: B , C , D
#		value:  1 , 2 , 3
#	},	D:
# }

from random_word import RandomWords
from random import random

r = RandomWords()


def genDict(
        connections: [],
        values: []):
    return {
        "connect": connections,
        "values": values,
    }


def generateConnections(nodes: []):
    list_of_connections = []
    print(nodes)
    for node in nodes:
        nodeConnections = []
        for secondNode in nodes:
            if node == secondNode:
                continue
            rand = random()
            if rand > 0.54:
                nodeConnections.append(secondNode)
        list_of_connections.append(nodeConnections[:])

    return list_of_connections


def generateConnectionsValues(connections: [[]]):
    list_of_all_values = []
    for node in connections:
        values = []
        for secondNode in node:
            rand = int(random() * 10)
            values.append(rand)
        list_of_all_values.append(values[:])

    return list_of_all_values


def randomDataset():
    data = {}
    node_count = int(random() * 100) + 2
    print(node_count)
    nodes = None
    while nodes is None:
        nodes = r.get_random_words(limit=node_count)
    node_connection = generateConnections(nodes)
    all_values = generateConnectionsValues(node_connection)
    for i in range(node_count):
        data[nodes[i]] = genDict(node_connection, all_values)

    return data
