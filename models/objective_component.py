from dataclasses import dataclass

from models.vertex import Vertex


@dataclass
class ObjectiveComponent:
    alternativeTargets: list[Vertex]
    threshold: int
    delayCoefficient: float
