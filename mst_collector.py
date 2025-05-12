from abc import ABC, abstractmethod

class MSTCollector(ABC):
    def __init__(self):
        self.total_weight = 0

    @abstractmethod
    def add_edge(self, edge, weight):
        pass

    @abstractmethod
    def result(self):
        pass

class CollectMSTEdges(MSTCollector):
    def __init__(self):
        super().__init__()
        self.edges = []

    def add_edge(self, edge, weight):
        self.total_weight += weight
        self.edges.append(edge)

    def result(self):
        return self.edges


class CollectMSTWeightOnly(MSTCollector):
    def __init__(self):
        super().__init__()

    def add_edge(self, edge, weight):
        self.total_weight += weight

    def result(self):
        return self.total_weight


class CollectMSTWeightAndEdges(MSTCollector):
        def __init__(self):
            super().__init__()
            self.edges = []

        def add_edge(self, edge, weight):
            self.total_weight += weight
            self.edges.append(edge)

        def result(self):
            return (self.total_weight, self.edges)

class CollectPrettyMSTWeightAndEdges(MSTCollector):
    class Struct:
        def __init__(self, weight: float, edges: list[tuple[int, int, float]]):
            self.weight = weight
            self.edges = edges

        def __repr__(self):
            edge_lines = "\n".join(f"{u} -- {v} (weight: {w})" for u, v, w in self.edges)
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



class CollectMSTWeightsList(MSTCollector):
    """ Collector that collects only the weights of the MST edges. """
    
    def __init__(self):
        super().__init__()
        self.weights = []

    def add_edge(self, edge, weight):
        self.weights.append(weight)

    def result(self):
        return self.weights
