from abc import ABC, abstractmethod
from typing import List, Set, Dict, Any, Tuple, Type
from inputs  import GraphInput
from outputtypes import OutputType
import heapq
from mst_collector import MSTCollector

# class MSTAlgorithm(ABC):
#     @classmethod
#     @abstractmethod
#     def compute(cls, graph_input: GraphInput) -> Tuple[List[Tuple[int, int, float]], float]:
#         pass


class MSTAlgorithm(ABC):
    @classmethod
    @abstractmethod
    def compute(cls, graph_input: GraphInput, input_data: Any, collector: MSTCollector):
        pass

class MSTAlgorithm(ABC):
    @staticmethod
    @abstractmethod
    def compute(cls, edges: list[tuple[int, int, float]], collector: 'MSTCollector'):
        pass
    
# version 1
# class KruskalMST(MSTAlgorithm):
#     @classmethod
#     def compute(cls, graph_input: GraphInput, input_data: Any) -> Tuple[List[Tuple[int, int, float]], float]:
#         edges = graph_input.get_edges(input_data)  # Use the data directly
#         edges.sort(key=lambda edge: edge[2])  # Sort edges by weight

#         # Initialize the parent and rank dictionaries
#         parent = {}
#         rank = {}

#         # Initialize parent and rank for each node
#         for edge in edges:
#             u, v, _ = edge
#             if u not in parent:
#                 parent[u] = u
#                 rank[u] = 0
#             if v not in parent:
#                 parent[v] = v
#                 rank[v] = 0

#         def find(u):
#             if parent[u] != u:
#                 parent[u] = find(parent[u])  # Path compression
#             return parent[u]

#         def union(u, v):
#             root_u = find(u)
#             root_v = find(v)
#             if root_u != root_v:
#                 if rank[root_u] > rank[root_v]:
#                     parent[root_v] = root_u
#                 elif rank[root_u] < rank[root_v]:
#                     parent[root_u] = root_v
#                 else:
#                     parent[root_v] = root_u
#                     rank[root_u] += 1

#         mst_edges = []
#         total_weight = 0
#         for u, v, weight in edges:
#             if find(u) != find(v):
#                 union(u, v)
#                 mst_edges.append((u, v, weight))
#                 total_weight += weight

#         return mst_edges, total_weight

# version 2
# class KruskalMST(MSTAlgorithm):
#     @classmethod
#     def compute(cls, graph_input: GraphInput, input_data: Any, collector: MSTCollector):
#         edges = graph_input.get_edges(input_data)
#         edges.sort(key=lambda edge: edge[2])

#         parent = {}
#         rank = {}

#         for u, v, _ in edges:
#             if u not in parent:
#                 parent[u] = u
#                 rank[u] = 0
#             if v not in parent:
#                 parent[v] = v
#                 rank[v] = 0

#         def find(u):
#             if parent[u] != u:
#                 parent[u] = find(parent[u])
#             return parent[u]

#         def union(u, v):
#             root_u = find(u)
#             root_v = find(v)
#             if root_u != root_v:
#                 if rank[root_u] > rank[root_v]:
#                     parent[root_v] = root_u
#                 elif rank[root_u] < rank[root_v]:
#                     parent[root_u] = root_v
#                 else:
#                     parent[root_v] = root_u
#                     rank[root_u] += 1

#         # Collecting edges and weight
#         for u, v, weight in edges:
#             if find(u) != find(v):
#                 union(u, v)
#                 collector.add_edge((u, v, weight), weight)

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






# version 1
# class PrimMST(MSTAlgorithm):
#     @classmethod
#     def compute(cls, graph_input: GraphInput, input_data: Any) -> Tuple[List[Tuple[int, int, float]], float]:
#         mst_edges = []
#         total_weight = 0
#         visited = set()

#         # Use a priority queue for Prim's algorithm (min-heap)
#         start_node = next(iter(graph_input.get_edges(input_data)))[0]  # Pick the first node from edges
#         min_heap = [(0, start_node)]  # (weight, node)

#         while min_heap:
#             weight, u = heapq.heappop(min_heap)  # Get the node with the minimum edge weight
#             if u in visited:
#                 continue
#             visited.add(u)
#             total_weight += weight

#             # Add the edge to the MST if it's not visited yet
#             if weight > 0:
#                 mst_edges.append((u, weight))

#             # Process the neighbors of the current node u
#             for u, v, edge_weight in graph_input.get_edges(input_data):  # Unpack into u, v, and edge_weight
#                 if v not in visited:
#                     heapq.heappush(min_heap, (edge_weight, v))  # Add the edge to the priority queue

#         return mst_edges, total_weight

# version 2
# class PrimMST(MSTAlgorithm):
#     @classmethod
#     def compute(cls, graph_input: GraphInput, input_data: Any, collector: MSTCollector):
#         import heapq
#         visited = set()
#         min_heap = []
#         start_node = next(iter(graph_input.get_edges(input_data)))[0]
#         heapq.heappush(min_heap, (0, start_node))

#         while min_heap:
#             weight, u = heapq.heappop(min_heap)
#             if u in visited:
#                 continue
#             visited.add(u)
#             collector.add_edge((u, weight), weight)

#             # Add neighbors to heap
#             for _, v, edge_weight in graph_input.get_edges(input_data):
#                 if v not in visited:
#                     heapq.heappush(min_heap, (edge_weight, v))



class PrimMST(MSTAlgorithm):
    @staticmethod
    def compute(edges: List[Tuple[int, int, float]], collector: 'MSTCollector'):
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



# def compute_mst(algorithm: Type[MSTAlgorithm], input_data: Any, output_type: Type[OutputType]):
#     # Auto-detect input type
#     graph_input = GraphInput.detect_and_parse(input_data)  # Get the correct input class

#     # Compute MST using the selected algorithm
#     mst_edges, total_weight = algorithm.compute(graph_input, input_data)  # Pass the data to the compute method

#     # Extract output using the selected output type
#     return output_type.extract_output(mst_edges, total_weight)


# def compute_mst(algorithm: Type[MSTAlgorithm], input_data: Any, output_type: Type[OutputType]):
#     graph_input = GraphInput.detect_and_parse(input_data)
    
#     # Get the appropriate collector for the requested output type
#     collector = output_type.create_collector()
    
#     # Compute MST using the selected algorithm
#     algorithm.compute(graph_input, input_data, collector)  # Pass the collector to the algorithm
    
#     # Extract the output from the collector
#     return output_type.extract_output_from_collector(collector.result())


def compute_mst(
    algorithm: Type['MSTAlgorithm'],
    graph_input: 'GraphInput',
    output_type: Type['OutputType']
):
    # Step 1: Get edges from the graph input
    edges = graph_input.get_edges()

    # Step 2: Create a collector based on desired output type
    collector = output_type.create_collector()

    # Step 3: Run the MST algorithm, collecting results into the collector
    algorithm.compute(edges, collector)

    # Step 4: Return final formatted result
    return output_type.extract_output_from_collector(collector.result())




# def compute_mst(algorithm: Type[MSTAlgorithm], graph_input: GraphInput, output_type: Type[OutputType]):
#     # Get edges from the input object
#     edges = graph_input.get_edges()  # No need to check input type, polymorphism handles it

#     # Compute MST using the selected algorithm
#     mst_edges, total_weight = algorithm.compute(edges)  # Algorithm works with edges directly

#     # Extract output using the selected output type
#     return output_type.extract_output(mst_edges, total_weight)