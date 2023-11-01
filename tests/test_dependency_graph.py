import unittest
import json
import networkx as nx

import sys

# Add parent directory to system path
sys.path.insert(0, '..')

from dep_graph import dependency_graph

class TestConstructDependencyGraph(unittest.TestCase):
    def test_dependency_graph(self):
        # Test data
        test_data = {
            "pkg1": ["pkg2", "pkg3"],
            "pkg2": ["pkg3"],
            "pkg3": []
        }

        # Save test data to a file
        with open("test_deps.json", "w") as file:
            json.dump(test_data, file)

        # Construct the graph
        graph = dependency_graph("test_deps.json")

        # Check if all the nodes are present in the graph
        self.assertCountEqual(test_data.keys(), graph.nodes)

        # Check if all the edges are present in the graph
        for pkg in test_data:
            for dep in test_data[pkg]:
                self.assertIn(dep, graph[pkg])

    def test_dependency_graph_empty_file(self):
        # Empty test data
        test_data = {}

        # Save test data to a file
        with open("test_deps.json", "w") as file:
            json.dump(test_data, file)

        # Construct the graph
        graph = dependency_graph("test_deps.json")

        # Check if the graph is empty
        self.assertFalse(graph.nodes)

    def test_dependency_graph_missing(self):
        # Test data with missing dependencies
        test_data = {
            "pkg1": ["pkg2", "pkg3"],
            "pkg2": ["pkg3"]
        }

        # Save test data to a file
        with open("test_deps.json", "w") as file:
            json.dump(test_data, file)

        # Construct the graph
        graph = dependency_graph("test_deps.json")

        # Check if all nodes are present in the graph, including missing dependencies
        self.assertCountEqual(set(test_data.keys()).union(set([dep for pkg in test_data for dep in test_data[pkg]])), graph.nodes)

if __name__ == '__main__':
    unittest.main()
