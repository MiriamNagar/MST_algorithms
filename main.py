from mst_algorithms import compute_mst, KruskalMST, PrimMST
from outputtypes import MSTEdges, MSTWeight, MSTWeightAndEdges, MSTStruct, MSTWeightsList
from inputs import AdjacencyListInput, WeightMatrixInput

# input_data = {
#     0: [(1, 10), (2, 6), (3, 5)],
#     1: [(0, 10), (3, 15)],
#     2: [(0, 6), (3, 4)],
#     3: [(0, 5), (1, 15), (2, 4)],
# }

# result = compute_mst(KruskalMST, input_data, MSTEdges)
# print(result)  # List of edges in the MST

# result = compute_mst(KruskalMST, input_data, MSTWeight)
# print(result)  # List of edges in the MST


# input_data = [
#     [0, 10, 6, 5],
#     [10, 0, 15, 4],
#     [6, 15, 0, 4],
#     [5, 4, 4, 0],
# ]

# result = compute_mst(PrimMST, input_data, MSTWeight)
# print(result)  # Total weight of MST

# result = compute_mst(PrimMST, input_data, MSTEdges)
# print(result)  # Total weight of MST

# result = compute_mst(KruskalMST, input_data, MSTEdges)
# print(result)  # List of edges in the MST

# result = compute_mst(KruskalMST, input_data, MSTWeight)
# print(result)  # List of edges in the MST

# # result = compute_mst(PrimMST, input_data, MSTWeights)
# # print(result)  # Total weight of MST

# result = compute_mst(KruskalMST, input_data, MSTWeightList)
# print(result)  # [4, 5, 10]


# input_data = {
#     0: [(1, 10), (2, 6), (3, 5)],
#     1: [(0, 10), (3, 15)],
#     2: [(0, 6), (3, 4)],
#     3: [(0, 5), (1, 15), (2, 4)],
# }

# result = compute_mst(KruskalMST, input_data, MSTWeightList)
# print(result)  # Should print the list of weights in MST, e.g., [5, 6, 10]

# result = compute_mst(KruskalMST, input_data, MSTEdges)
# print(result)  # List of edges in the MST

# result = compute_mst(KruskalMST, input_data, MSTGraph)
# print(result)  # List of edges in the MST

# result = compute_mst(KruskalMST, input_data, MSTEdgeListAndWeight)
# print(result)  # List of edges in the MST


# Assuming these are already defined:
# - KruskalMST
# - MSTWeight, MSTEdges, MSTWeightAndEdges, MSTStruct, MSTWeightsList
# - AdjacencyListInput (which implements GraphInput)
# - compute_mst(algorithm: Type[MSTAlgorithm], graph_input: GraphInput, output_type: Type[OutputType])


# Wrap raw input data with AdjacencyListInput
input_data = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)],
}
graph_input = AdjacencyListInput(input_data)

# Run various output types with KruskalMST
result = compute_mst(KruskalMST, graph_input, MSTWeight)
print(result)  # Should output just the total weight

result = compute_mst(KruskalMST, graph_input, MSTEdges)
print(result)  # Should output the list of MST edges

result = compute_mst(KruskalMST, graph_input, MSTWeightAndEdges)
print(result)  # Should output a tuple of (total weight, edges)

result = compute_mst(KruskalMST, graph_input, MSTStruct)
print(result)  # Should output a pretty-printed structure

result = compute_mst(KruskalMST, graph_input, MSTWeightsList)
print(result)  # Should output the list of edge weights





# # Example adjacency list input data
# input_data_list = {
#     0: [(1, 10), (2, 6), (3, 5)],
#     1: [(0, 10), (3, 15)],
#     2: [(0, 6), (3, 4)],
#     3: [(0, 5), (1, 15), (2, 4)],
# }

# # Create an instance of AdjacencyListInput
# graph_input_list = AdjacencyListInput(input_data_list)

# # Example adjacency matrix input data
# input_data_matrix = [
#     [0, 10, 6, 5],
#     [10, 0, 15, 4],
#     [6, 15, 0, 4],
#     [5, 4, 4, 0],
# ]

# # Create an instance of AdjacencyMatrixInput
# graph_input_matrix = AdjacencyMatrixInput(input_data_matrix)

# # Test with Kruskal's Algorithm and different output types
# result = compute_mst(KruskalMST, graph_input_list, MSTWeightList)
# print(result)  # Should print a list of weights like [4, 5, 10]

# result = compute_mst(PrimMST, graph_input_matrix, MSTWeightList)
# print(result)  # Should print a list of weights like [4, 5, 10]
