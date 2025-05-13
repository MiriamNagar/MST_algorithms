from mst_algorithms import compute_mst, KruskalMST, PrimMST
from outputtypes import (
    MSTEdges,
    MSTWeight,
    MSTWeightAndEdges,
    MSTPrettyPrintStruct,
    MSTWeightsList,
)
from inputs import AdjacencyListInput, WeightMatrixInput

# Sample data
adjacency_list_input = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)],
}

weight_matrix_input = [
    [0, 10, 6, 5],
    [10, 0, 0, 15],
    [6, 0, 0, 4],
    [5, 15, 4, 0],
]


# Input instances
inputs = [
    AdjacencyListInput(adjacency_list_input),
    WeightMatrixInput(weight_matrix_input),
]

# Algorithms
algorithms = [KruskalMST, PrimMST]

# Output types
output_types = [
    MSTWeight,
    MSTEdges,
    MSTWeightAndEdges,
    MSTPrettyPrintStruct,
    MSTWeightsList,
]

# Run all combinations: 2 inputs × 2 algorithms × 5 output types = 20 total
for graph_input in inputs:
    for algorithm in algorithms:
        for output_type in output_types:
            print(
                f"--- {type(graph_input).__name__} | {algorithm.__name__} | {output_type.__name__} ---"
            )
            try:
                result = compute_mst(algorithm, graph_input, output_type)
                print(result, end="\n\n")
            except Exception as e:
                print(f"Error: {e}", end="\n\n")


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
