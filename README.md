# Python-Package-for-Dependency-Graph
This package can be used to read a JSON file from a fixed filesystem location containing a list of packages and their dependencies, and reconstructs the full dependency graph.

## Installation
Clone the repository and run the following command in the root:
`pip install .`

This will install the dep_graph module along with the dependencies.

## Usage
Run the command 
`python3 -m dep_graph`

The main function `dependency_graph` takes the filepath for the input json file and returns the dependency graph.
The json file is stored at `tmp/deps.json` and structured as:

{
    "package_1": ["dependency_1", "dependency_2"],
    "package_2": ["dependency_3"],
    ...
}

## Testing
The unit tests for the dependency_graph function is written in test_dependency_graph.py in the tests folder.
To run the tests, navigate to tests directory using the command `cd tests` followed by:<br />
`python3 -m unittest discover`
