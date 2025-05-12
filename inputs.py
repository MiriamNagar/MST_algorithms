from abc import ABC, abstractmethod
from typing import List, Set, Dict, Any, Tuple


class GraphInput(ABC):
    def __init__(self, data: Any):
        self.data = data

    @abstractmethod
    def get_edges(self) -> List[Tuple[int, int, float]]:
        pass

    @abstractmethod
    def get_nodes(self) -> Set[int]:
        pass


class AdjacencyListInput(GraphInput):
    def get_edges(self) -> List[Tuple[int, int, float]]:
        edges = []
        seen = set()
        for u, neighbors in self.data.items():
            for v, weight in neighbors:
                if (v, u) not in seen:  # Avoid duplicates in undirected graph
                    edges.append((u, v, weight))
                    seen.add((u, v))
        return edges

    def get_nodes(self) -> Set[int]:
        return set(self.data.keys())


class WeightMatrixInput(GraphInput):
    def get_edges(self) -> List[Tuple[int, int, float]]:
        edges = []
        matrix = self.data
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):  # Avoid duplicates
                if matrix[i][j] > 0:
                    edges.append((i, j, matrix[i][j]))
        return edges

    def get_nodes(self) -> Set[int]:
        return set(range(len(self.data)))
