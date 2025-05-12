from mst_algorithms import compute_mst, KruskalMST, PrimMST
from outputtypes import MSTEdges, MSTWeight, MSTWeightAndEdges, MSTStruct, MSTWeightsList
from inputs import AdjacencyListInput, WeightMatrixInput

input_data = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)],
}

input_data = [
    [0, 10, 6, 5],
    [10, 0, 15, 4],
    [6, 15, 0, 4],
    [5, 4, 4, 0],
]

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


