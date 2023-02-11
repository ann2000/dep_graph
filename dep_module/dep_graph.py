import networkx as nx
import json
import matplotlib.pyplot as plt

def construct_dependency_graph(filepath):
    # Load the JSON file into a Python dictionary
    with open(filepath, "r") as file:
        data = json.load(file)

    # Create a directed graph using networkx
    G = nx.DiGraph()

    # Add nodes for each package
    for pkg in data:
        G.add_node(pkg)

    # Add edges for each dependency
    for pkg in data:
        for dep in data[pkg]:
            G.add_edge(pkg, dep)

    return G

def traverse_graph(graph, pkg, level):
    print("  " * level + pkg)
    for item in graph[pkg]:
        traverse_graph(graph, item, level + 1)

graph = construct_dependency_graph("tmp/deps.json")

for node in graph.nodes:
    traverse_graph(graph, node, 1)

nx.draw(graph, with_labels=True)
plt.show()
