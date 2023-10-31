import networkx as nx
import json
import matplotlib.pyplot as plt

def dependency_graph(filepath: str) -> nx.DiGraph:
    """
    Function to take the file path of a JSON file containing package dependencies and constructs a directed graph of the dependencies.
    
    Parameters
    ---------- 
    filepath: str
              The file path of the JSON file

    Returns
    -------
    G: nx.DiGraph
       the directed graph of the package dependencies
    """

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

def traverse_graph(graph: nx.DiGraph, pkg: str, level: int):
    """
    Recursive function to traverse the directed graph of package dependencies and print the package names to stdout.
    
    Parameters
    ----------
    graph: nx.DiGraph
           The directed graph of the package dependencies
    pkg: str
         The package name
    level: int 
           The level of indentation for printing
    """
    
    print("  " * level + pkg)
    for item in graph[pkg]:
        traverse_graph(graph, item, level + 1)

if __name__ == "__main__":

    # Load the dependencies from the JSON file and construct the directed graph
    graph = dependency_graph("tmp/deps.json")

    for node in graph.nodes:
        traverse_graph(graph, node, 1)

    nx.draw(graph, with_labels=True)
    plt.show()
