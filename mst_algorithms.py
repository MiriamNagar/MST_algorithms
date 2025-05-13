from abc import ABC, abstractmethod
from typing import List, Set, Dict, Any, Tuple, Type
from inputs import GraphInput
from outputtypes import OutputType
import heapq
from mst_collector import MSTCollector

from outputtypes import (
    MSTWeight,
    MSTEdges,
    MSTWeightAndEdges,
    MSTPrettyPrintStruct,
    MSTWeightsList,
)
from inputs import AdjacencyListInput, WeightMatrixInput


class MSTAlgorithm(ABC):
    @classmethod
    @abstractmethod
    def compute(cls, graph_input: GraphInput, input_data: Any, collector: MSTCollector):
        pass


class MSTAlgorithm(ABC):
    @staticmethod
    @abstractmethod
    def compute(cls, edges: list[tuple[int, int, float]], collector: "MSTCollector"):
        pass


class KruskalMST(MSTAlgorithm):
    @staticmethod
    def compute(edges, collector):
        parent = {}

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u, v):
            parent[find(u)] = find(v)

        # Initialize union-find
        nodes = {u for u, v, _ in edges} | {v for u, v, _ in edges}
        for node in nodes:
            parent[node] = node

        for u, v, w in sorted(edges, key=lambda x: x[2]):
            if find(u) != find(v):
                union(u, v)
                collector.add_edge((u, v), w)


class PrimMST(MSTAlgorithm):
    @staticmethod
    def compute(edges: List[Tuple[int, int, float]], collector: "MSTCollector"):
        from collections import defaultdict

        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        # Step 2: Prim's algorithm
        visited = set()
        min_heap = []

        # Start from an arbitrary node
        start_node = next(iter(graph))
        visited.add(start_node)
        for weight, neighbor in graph[start_node]:
            heapq.heappush(min_heap, (weight, start_node, neighbor))

        while min_heap and len(visited) < len(graph):
            weight, u, v = heapq.heappop(min_heap)
            if v not in visited:
                visited.add(v)
                collector.add_edge((u, v), weight)

                for next_weight, neighbor in graph[v]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (next_weight, v, neighbor))


def compute_mst(
    algorithm: Type["MSTAlgorithm"],
    graph_input: "GraphInput",
    output_type: Type["OutputType"],
):
    """
    Computes the Minimum Spanning Tree (MST) using the specified algorithm, input data, and output type.

    Parameters:
    - algorithm: The MST algorithm to use (KruskalMST, PrimMST)
    - graph_input: The input graph in one of the supported formats (AdjacencyListInput, WeightMatrixInput)
    - output_type: The type of the desired output (MSTWeight, MSTEdges, MSTWeightAndEdges, MSTPrettyPrintStruct, MSTWeightsList)

    Returns:
    - The computed MST in the specified output type.

    Example 1: Kruskal's Algorithm on Adjacency List input, returning the MST weight
    >>> adjacency_list_input = {
    >>>     0: [(1, 10), (2, 6), (3, 5)],
    >>>     1: [(0, 10), (3, 15)],
    >>>     2: [(0, 6), (3, 4)],
    >>>     3: [(0, 5), (1, 15), (2, 4)],
    >>> }
    >>> graph_input = AdjacencyListInput(adjacency_list_input)
    >>> result = compute_mst(KruskalMST, graph_input, MSTWeight)
    >>> print(result)  # Should output the total weight of the MST
    Total Weight: 16

    Example 2: Prim's Algorithm on Weight Matrix input, returning the MST edges
    >>> weight_matrix_input = [
    >>>     [0, 10, 6, 5],
    >>>     [10, 0, 0, 15],
    >>>     [6, 0, 0, 4],
    >>>     [5, 15, 4, 0],
    >>> ]
    >>> graph_input = WeightMatrixInput(weight_matrix_input)
    >>> result = compute_mst(PrimMST, graph_input, MSTEdges)
    >>> print(result)  # Should output the list of MST edges
    [(0, 3), (2, 3), (0, 1)]

    Example 3: Kruskal's Algorithm on Adjacency List input, returning the MST edges and weights
    >>> result = compute_mst(KruskalMST, graph_input, MSTWeightAndEdges)
    >>> print(result)  # Should output the MST edges and total weight
    ([(0, 3), (0, 2), (1, 2)], 16)

    Example 4: Prim's Algorithm on Weight Matrix input, returning a pretty-printed structure
    >>> result = compute_mst(PrimMST, graph_input, MSTPrettyPrintStruct)
    >>> print(result)  # Should output a nicely formatted MST with edges and total weight
    Total Weight: 16
    Edges:
    0 -- 3
    2 -- 3
    0 -- 1

    Example 5: Kruskal's Algorithm on Weight Matrix input, returning a list of MST weights
    >>> result = compute_mst(KruskalMST, graph_input, MSTWeightsList)
    >>> print(result)  # Should output a list of MST weights
    [16]

    """
    # Step 1: Get edges from the graph input
    edges = graph_input.get_edges()

    # Step 2: Create a collector based on desired output type
    collector = output_type.create_collector()

    # Step 3: Run the MST algorithm, collecting results into the collector
    algorithm.compute(edges, collector)

    # Step 4: Return final formatted result
    return output_type.extract_output_from_collector(collector.result())
