import pytest

from models.arc import Arc
from models.graph import Graph
from models.objective_component import ObjectiveComponent
from models.ssp_semi_soft_time_windows import SSPSemiSoftTimeWindows


@pytest.fixture
def trivial_ssp_semi_soft_time_windows() -> SSPSemiSoftTimeWindows:
    """A trivial graph (see attachments/trivial_dag_late_penalty_example)"""
    s, a, t_1, t_2, t = range(5)

    s_a = Arc(s, a)
    a_t_1 = Arc(a, t_1)
    s_t_2 = Arc(s, t_2)
    t_1_t = Arc(t_1, t)
    t_2_t = Arc(t_2, t)

    cost = {s_a: 1, a_t_1: 1, s_t_2: 4, t_1_t: 0, t_2_t: 0}
    duration = {s_a: 1, a_t_1: 4, s_t_2: 2, t_1_t: 1, t_2_t: 1}

    group = ObjectiveComponent(
        alternativeTargets=[t_1, t_2], threshold=3, delayCoefficient=2.0
    )

    graph = Graph(
        vertices=[s, a, t_1, t_2, t],
        arcs=[s_a, a_t_1, s_t_2, t_1_t, t_2_t],
        cost=lambda arc: cost[arc],
        duration=lambda arc: duration[arc],
        startTime=0,
        earliestArrival=lambda v: 0,
        objectiveComponents=[group],
    )
    return SSPSemiSoftTimeWindows(graph=graph, source=s, target=t)


def test_solve_dp(trivial_ssp_semi_soft_time_windows: SSPSemiSoftTimeWindows) -> None:
    # Calculation (assumption: penalty = c * max(0, arrival_time - threshold)
    # at the chosen alternative target; here c = 2, threshold = 3, start time 0):
    #
    #   Path                 Cost   Arrival at group   Penalty           Total
    #   s -> a -> t1 -> t      2    t1 at time 5       2 * (5 - 3) = 4     6
    #   s -> t2 -> t           4    t2 at time 2       0                   4
    #
    # Without the penalty, the upper path wins (2 < 4); with it, the lower one
    # does (4 < 6).

    assert trivial_ssp_semi_soft_time_windows.solve_dp() == (0, 3, 4)
