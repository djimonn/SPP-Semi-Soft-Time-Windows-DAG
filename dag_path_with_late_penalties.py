from graph import Graph
from path import Path
from vertex import Vertex


class DagPathWithLatePenalties:
    Graph: Graph
    Source: Vertex
    Target: Vertex

    def solve_dp(self) -> Path:
        pass
