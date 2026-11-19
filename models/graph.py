from collections.abc import Callable
from dataclasses import dataclass

from models.arc import Arc
from models.objective_component import ObjectiveComponent
from models.vertex import Vertex

type ArcFunction = Callable[[Arc], float]
type VertexFunction = Callable[[Vertex], float]


@dataclass
class Graph:
    vertices: list[Vertex]
    arcs: list[Arc]
    cost: ArcFunction
    duration: ArcFunction
    startTime: int
    earliestArrival: VertexFunction
    objectiveComponents: list[ObjectiveComponent]
