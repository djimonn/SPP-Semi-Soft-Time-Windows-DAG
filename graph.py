from collections.abc import Callable

from arc import Arc
from objective_component import ObjectiveComponent
from vertex import Vertex

type ArcFunction = Callable[[Arc], float]
type VertexFunction = Callable[[Vertex], float]


class Graph:
    Vertices: list[Vertex]
    Arcs: list[Arc]
    Cost: ArcFunction
    Duration: ArcFunction
    StartTime: int
    EarliestArrival: VertexFunction
    ObjectiveComponents: list[ObjectiveComponent]
