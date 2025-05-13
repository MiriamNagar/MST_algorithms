from abc import ABC, abstractmethod
from typing import List, Set, Dict, Any, Tuple


class GraphInput(ABC):
    """
    GraphInput is an abstract class for different graph input formats.
    It defines the methods for getting edges and nodes, which are
    implemented by the subclasses for specific input types.
    """

    def __init__(self, data: Any):
        self.data = data

    @abstractmethod
    def get_edges(self) -> List[Tuple[int, int, float]]:
        """
        Abstract method to return the edges of the graph in a tuple format (u, v, weight).
        """
        pass

    @abstractmethod
    def get_nodes(self) -> Set[int]:
        """
        Abstract method to return the set of nodes in the graph.
        """
        pass


class AdjacencyListInput(GraphInput):
    """
    AdjacencyListInput handles the graph input represented as an adjacency list.
    The adjacency list is a dictionary where keys are node IDs and values are lists of tuples (neighbor, weight).
    """

    def get_edges(self) -> List[Tuple[int, int, float]]:
        """
        Extracts edges from the adjacency list format.
        Each edge is a tuple (u, v, weight).
        """
        edges = []
        seen = set()
        for u, neighbors in self.data.items():
            for v, weight in neighbors:
                if (v, u) not in seen:  # Avoid duplicates in undirected graph
                    edges.append((u, v, weight))
                    seen.add((u, v))
        return edges

    def get_nodes(self) -> Set[int]:
        """
        Returns the set of nodes in the graph (keys from the adjacency list).
        """
        return set(self.data.keys())


class WeightMatrixInput(GraphInput):
    """
    WeightMatrixInput handles the graph input represented as a weight matrix.
    The matrix is a 2D array where element [i][j] represents the weight of the edge between nodes i and j.
    """

    def get_edges(self) -> List[Tuple[int, int, float]]:
        """
        Extracts edges from the weight matrix.
        Each edge is a tuple (i, j, weight), where weight is the matrix element between nodes i and j.
        """
        edges = []
        matrix = self.data
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):  # Avoid duplicates
                if matrix[i][j] > 0:
                    edges.append((i, j, matrix[i][j]))
        return edges

    def get_nodes(self) -> Set[int]:
        """
        Returns the set of nodes in the graph (from 0 to len(matrix)-1).
        """
        return set(range(len(self.data)))
