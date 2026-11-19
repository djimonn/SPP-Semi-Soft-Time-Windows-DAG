from vertex import Vertex


class ObjectiveComponent:
    AlternativeTargets: list[Vertex]
    Threshold: int
    DelayCoefficient: float
