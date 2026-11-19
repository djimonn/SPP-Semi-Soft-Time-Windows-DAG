from dataclasses import dataclass

from models.graph import Graph
from models.path import Path
from models.vertex import Vertex


@dataclass
class SSPSemiSoftTimeWindows:
    graph: Graph
    source: Vertex
    target: Vertex

    def solve_dp(self) -> Path:
        pass
