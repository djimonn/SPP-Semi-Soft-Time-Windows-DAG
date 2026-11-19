from typing import NamedTuple

from models.vertex import Vertex


class Arc(NamedTuple):
    tail: Vertex
    head: Vertex
