"""
Define the various available output formats for MST algorithms.

For file 50-FlyWeight.
"""

from abc import ABC
from mst_collector import MSTCollector, CollectMSTEdges, CollectMSTWeightOnly, CollectMSTWeightAndEdges, CollectPrettyMSTWeightAndEdges, CollectMSTWeightsList

CollectorResult = any

class OutputType(ABC):
    @classmethod
    def create_collector(cls) -> MSTCollector:
        """
        Create and return an MSTCollector instance.
        """
        raise NotImplementedError("Choose a specific output type.")

    @classmethod
    def extract_output_from_collector(cls, result: CollectorResult) -> any:
        """
        Extract the desired output format from the collector's result.
        """
        raise NotImplementedError("Choose a specific output type.")


# ---- Output: Only total MST weight ----

class MSTWeight(OutputType):
    """ Output only the total weight of the MST. """

    @classmethod
    def create_collector(cls) -> MSTCollector:
        return CollectMSTWeightOnly()

    @classmethod
    def extract_output_from_collector(cls, result: float) -> float:
        return result


# ---- Output: List of MST edges ----

class MSTEdges(OutputType):
    """ Output only the list of MST edges. """

    @classmethod
    def create_collector(cls) -> MSTCollector:
        return CollectMSTEdges()

    @classmethod
    def extract_output_from_collector(cls, result: list[tuple[int, int]]) -> list:
        return result


# ---- Output: (Total weight, Edge list) ----

class MSTWeightAndEdges(OutputType):
    """ Output a tuple of (total_weight, list_of_edges). """

    @classmethod
    def create_collector(cls) -> MSTCollector:
        # return cls.Collector()
        return CollectMSTWeightAndEdges()

    @classmethod
    def extract_output_from_collector(cls, result: tuple[float, list[tuple[int, int]]]) -> tuple:
        return result


# ---- Output: Pretty-printed MST structure ----

class MSTPrettyPrintStruct(OutputType):
    """ Output an object with fields: weight and edges, with a nice __repr__. """

    @classmethod
    def create_collector(cls) -> MSTCollector:
        return CollectPrettyMSTWeightAndEdges()

    @classmethod
    def extract_output_from_collector(cls, result: 'CollectPrettyMSTWeightAndEdges.Struct') -> 'CollectPrettyMSTWeightAndEdges.Struct':
        return result
    

class MSTWeightsList(OutputType):
    """ Output a list of weights from the MST edges. """

    @classmethod
    def create_collector(cls) -> MSTCollector:
        return CollectMSTWeightsList()

    @classmethod
    def extract_output_from_collector(cls, result: list) -> list:
        return result
