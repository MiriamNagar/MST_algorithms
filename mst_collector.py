from abc import ABC, abstractmethod


class MSTCollector(ABC):
    """
    Abstract class for collecting results from MST algorithms.
    Each subclass defines how to collect and return specific output formats from the MST computation.
    """

    def __init__(self):
        self.total_weight = 0

    @abstractmethod
    def add_edge(self, edge, weight):
        """
        Adds an edge to the collector, updating the collected data.
        """
        pass

    @abstractmethod
    def result(self):
        """
        Returns the final result collected by the MST algorithm.
        """
        pass


# Collector for MST edges only
class CollectMSTEdges(MSTCollector):
    """
    Collects only the edges of the MST.
    """

    def __init__(self):
        super().__init__()
        self.edges = []

    def add_edge(self, edge, weight):
        self.total_weight += weight
        self.edges.append(edge)

    def result(self):
        return self.edges


# Collector for MST weight only
class CollectMSTWeightOnly(MSTCollector):
    """
    Collects only the total weight of the MST.
    """

    def __init__(self):
        super().__init__()

    def add_edge(self, edge, weight):
        self.total_weight += weight

    def result(self):
        return self.total_weight


# Collector for both MST weight and edges
class CollectMSTWeightAndEdges(MSTCollector):
    """
    Collects both the total weight and the edges of the MST.
    """

    def __init__(self):
        super().__init__()
        self.edges = []

    def add_edge(self, edge, weight):
        self.total_weight += weight
        self.edges.append(edge)

    def result(self):
        return (self.total_weight, self.edges)


# Collector for a pretty-printed MST with weight and edges
class CollectPrettyMSTWeightAndEdges(MSTCollector):
    """
    Collects a nicely formatted MST with weight and edges, intended for pretty printing.
    """

    class Struct:
        """
        Helper structure for representing the MST with weight and edges in a human-readable format.
        """

        def __init__(self, weight: float, edges: list[tuple[int, int, float]]):
            self.weight = weight
            self.edges = edges

        def __repr__(self):
            edge_lines = "\n".join(
                f"{u} -- {v} (weight: {w})" for u, v, w in self.edges
            )
            return f"Total Weight: {self.weight}\nEdges:\n{edge_lines}"

    def __init__(self):
        super().__init__()
        self.edges = []

    def add_edge(self, edge, weight):
        self.total_weight += weight
        u, v = edge
        self.edges.append((u, v, weight))  # Now store with weight

    def result(self):
        return self.Struct(self.total_weight, self.edges)


# Collector for a list of MST edge weights
class CollectMSTWeightsList(MSTCollector):
    """
    Collects only the weights of the MST edges.
    """

    def __init__(self):
        super().__init__()
        self.weights = []

    def add_edge(self, edge, weight):
        self.weights.append(weight)

    def result(self):
        return self.weights
