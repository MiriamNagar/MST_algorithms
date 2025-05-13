# MST System Architecture Documentation

## Overview

This system is designed to compute the Minimum Spanning Tree (MST) of a graph, allowing for various output formats, such as the total weight of the MST, a list of the edges in the MST, or a more complex, formatted structure for easier readability. The architecture is modular, utilizing design patterns that enhance extensibility, maintainability, and memory efficiency.


## Architecture Components
The architecture of the system is divided into three primary components:

- Graph Input Handlers:

    This component is responsible for reading and parsing different types of graph representations (Adjacency List and Weight Matrix) and providing an abstraction layer to interact with the graph data.

- MST Computation:

    This core component implements the MST algorithms (Kruskal or Prim) and uses different collectors to store the results in various formats.

- Output Formats:

    The output formats define how the MST result will be presented or used. This layer abstracts the collection and extraction of data into various formats like weight-only, edge-list, and human-readable representations.


## Design Decisions

1. Separation of Concerns:

    The system has been designed to separate concerns between input handling, MST computation, and output formatting. This modular approach makes the system flexible, as each component can evolve independently of the others.

    Example: The GraphInput classes (AdjacencyListInput, WeightMatrixInput) are separate from the MST computation logic, ensuring that any changes to the graph representation do not affect the MST algorithms.

2. Modular Output Formats:

    Each output format is handled by a dedicated class that adheres to the OutputType interface. This modularity allows for the easy addition of new output formats without affecting the existing system.

    Why Important: The need for various output formats (weight only, edges only, pretty print, etc.) is a key requirement, and this approach allows for simple extension of the system when additional formats are needed.

3. Flexibility in Input Handling:

    The system supports multiple graph input formats (Adjacency List and Weight Matrix) to accommodate different types of graph representations that might be encountered in various use cases.

    Why Important: Different use cases and graph data sources may represent graphs in distinct ways, and the ability to handle multiple input formats makes the system more flexible and adaptable.

4. Collector Pattern for Results:

    The MSTCollector classes encapsulate how results are gathered and returned. Each collector is responsible for collecting the relevant data (edges, weight, or both) and returning it in the desired format.

    Why Important: This design ensures that the process of collecting results is consistent and decoupled from the MST algorithm itself, making it easier to implement new result formats without modifying the core MST logic.

5. Abstract Factory for Output Generation:

    The OutputType class is responsible for creating the appropriate collector instance. This abstraction allows the client to choose the output format without having to deal with the implementation details of the collector classes.

    Why Important: This design improves maintainability by hiding the complexity of output formatting behind a simple interface, which allows the system to scale with minimal changes to the core logic.


## Design Patterns Used

### 1. Abstract Factory Pattern

- **Usage**: In the `OutputType` class and its subclasses (`MSTWeight`, `MSTEdges`, etc.), the Abstract Factory pattern is used to create appropriate collector instances depending on the required output format.
- **Why Used**: This pattern ensures that the correct type of collector is instantiated without the need for conditionals or direct class references, making the code more maintainable and easier to extend for additional output formats in the future.

### 2. Strategy Pattern

- **Usage**: The strategy pattern is applied in the form of different `MSTCollector` subclasses (`CollectMSTEdges`, `CollectMSTWeightOnly`, etc.). Each collector encapsulates a different strategy for collecting and processing the MST result.
- **Why Used**: This pattern allows for swapping out different strategies for handling the MST computation results without altering the core MST logic, making the system highly extensible and modular.

### 3. Composite Pattern

- **Usage**: In the `MSTPrettyPrintStruct` class, a composite-like structure is used to manage a group of related data items (edges and weights) for a more structured, formatted output.
- **Why Used**: This pattern allows the easy combination of edges and weights into a single structured output, which can be further processed or printed in a user-friendly way.

### 4. Flyweight Pattern

- **Usage**: The Flyweight pattern is used to minimize memory usage by sharing common graph elements (nodes, edges) across different parts of the system (for example, across partitions or MST results). Shared elements are reused rather than created anew for each instance.
- **Why Used**: This pattern optimizes memory usage and performance, especially when dealing with large graphs or partitioned datasets where many elements are repeated. By sharing common data, the system can handle larger datasets more efficiently and minimize memory overhead.

## Flyweight Pattern in the System Architecture

### Flyweight Pattern Overview

The **Flyweight Pattern** is used to minimize memory usage by sharing common parts of the data among multiple objects. Instead of creating a new object for every element, the Flyweight pattern ensures that shared data is stored in a centralized way, and only the non-shared (or context-specific) data varies between different instances. This pattern is particularly useful when dealing with large numbers of objects that share common data, such as graph structures or partitioned data, where memory efficiency is crucial.

### How the Flyweight Pattern is Used

1. **Flyweight in Graph Representations (Partitioning)**:
   - **Usage**: In your partitioning code (for example, `GraphInput` classes), rather than creating new objects for every partition or subgraph, the Flyweight pattern ensures that objects that share common data (such as edges with the same weight or nodes) are reused efficiently.
   - **Why Used**: By reusing the same objects for shared data, memory usage is optimized, especially for large graphs with repeated elements. This is crucial when dealing with large datasets where inefficiencies could significantly impact performance.

2. **Flyweight in MST Computation**:
   - **Usage**: In the MST computation process, especially when collecting edges or results, the Flyweight pattern can be used to avoid redundant object creation for edges that are part of the MST but are common across multiple partitions or subgraphs.
   - **Why Used**: The same edge or node might appear in multiple MST results, and instead of duplicating them each time, the Flyweight pattern ensures that shared edges or nodes are referenced in a memory-efficient manner.

### Benefits of Flyweight Pattern

1. **Memory Efficiency**: Since shared data like nodes and edges are reused rather than duplicated, the overall memory footprint is minimized, which is especially useful when working with large graphs or partitioned datasets.
   
2. **Performance Improvement**: By reducing object creation and memory consumption, the system can handle larger datasets more efficiently, speeding up computations and reducing the load on the system.

3. **Cleaner Code**: The Flyweight pattern helps in organizing the code in such a way that shared data is centralized and reused, making the system easier to maintain and extend.

### Flyweight Pattern Design Decisions

- **Reuse of Graph Elements**: Rather than duplicating graph elements such as edges and nodes when dealing with different representations (Adjacency List or Weight Matrix), we use the Flyweight pattern to reference shared elements.
  
- **Memory Optimization**: By utilizing shared references for common elements (edges or nodes), the system ensures that we do not waste memory duplicating large or complex graph structures. This is particularly helpful in scenarios where graphs can be very large or contain repeated subgraphs or edges.

- **Performance Consideration**: The Flyweight pattern was chosen because the system might need to compute MSTs on very large graphs, and memory efficiency is key to handling such datasets without running into performance bottlenecks.

## Conclusion

This system incorporates several design patterns to ensure scalability, efficiency, and maintainability. The **Flyweight Pattern**, in particular, plays a crucial role in optimizing memory usage when handling large graphs and repeated elements. By utilizing shared objects for common data, the system can process large datasets without compromising on performance or memory efficiency.

## Installation

To get started with the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Install dependencies:
    pip install -r requirements.txt

3. Run the system:
    python main.py


## Use Guide

### 1. Creating a Graph Input

The first step is to provide a graph input to the system. There are two primary ways to input a graph:

#### a. Adjacency List
    An adjacency list represents a graph using a dictionary where each key is a node, and the associated value is a list of tuples representing the neighboring nodes and the edge weights.

    Example:

    ```python
    graph_data = {
        0: [(1, 1), (2, 4)],
        1: [(0, 1), (2, 2)],
        2: [(0, 4), (1, 2)]
    }
    ```

    graph_input = AdjacencyListInput(graph_data)

#### b. Weight Matrix

    A weight matrix represents a graph using a 2D matrix where each element (i, j) represents the weight of the edge between nodes i and j.

    Example:

    ```python
    graph_data = [
        [0, 1, 4],
        [1, 0, 2],
        [4, 2, 0]
    ]
    ```

    graph_input = WeightMatrixInput(graph_data)

### 2. Selecting the MST Algorithm
    You can use either Kruskal's or Prim's algorithm to compute the MST. The output format can be customized to your needs, and you can select from various formats such as the total MST weight, list of edges, or formatted output.

    Example:

    ```python
    from mst_algorithm import kruskal, prim
    ```

    mst_result = kruskal(graph_input)
    # or
    mst_result = prim(graph_input)

### 3. Choosing the Output Format
    After computing the MST, select the output format. For example, to extract only the MST weight:

    ```python
    output_type = MSTWeight()
    collector = output_type.create_collector()
    # Assuming 'mst_result' is the result from Kruskal or Prim
    for edge, weight in mst_result:
        collector.add_edge(edge, weight)

    result = output_type.extract_output_from_collector(collector.result())
    print(result)
    ```

    This will print the total MST weight.

### 4. Other Output Formats
    You can also choose other formats like the MST edges, or a pretty-printed structure:

    ```python
    output_type = MSTPrettyPrintStruct()
    collector = output_type.create_collector()
    for edge, weight in mst_result:
        collector.add_edge(edge, weight)

    result = output_type.extract_output_from_collector(collector.result())
    print(result)
    ```

    This will print the MST in a user-friendly format with the edges and total weight.

