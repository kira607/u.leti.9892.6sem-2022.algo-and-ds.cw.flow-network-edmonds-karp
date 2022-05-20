import pytest
from ..flow_network import FlowNetwork


@pytest.mark.parametrize(
    'graph_data, expected_max_flow',
    (
        (
            (
                ('S', 'O', 3),
                ('S', 'P', 3),
                ('O', 'Q', 3),
                ('O', 'P', 2),
                ('P', 'R', 2),
                ('Q', 'R', 4),
                ('Q', 'T', 2),
                ('R', 'T', 3),
            ),
            5,
        ),
        (
            (
                ('S', 'A', 8),
                ('S', 'B', 5),
                ('S', 'C', 3),
                ('A', 'B', 6),
                ('A', 'C', 4),
                ('A', 'D', 5),
                ('B', 'C', 5),
                ('B', 'E', 3),
                ('B', 'F', 5),
                ('C', 'D', 5),
                ('C', 'E', 4),
                ('D', 'E', 5),
                ('D', 'T', 3),
                ('E', 'T', 8),
                ('F', 'E', 3),
                ('F', 'T', 9),
            ),
            16,
        ),
        (
            (
                ('S', 'A', 5),
                ('S', 'D', 10),
                ('S', 'G', 5),
                ('A', 'B', 10),
                ('B', 'C', 10),
                ('B', 'E', 25),
                ('C', 'T', 5),
                ('D', 'A', 15),
                ('D', 'E', 20),
                ('E', 'G', 5),
                ('E', 'F', 30),
                ('F', 'B', 15),
                ('F', 'T', 15),
                ('F', 'I', 5),
                ('G', 'H', 5),
                ('H', 'I', 5),
                ('H', 'F', 5),
                ('I', 'T', 5),
            ),
            20,
        ),
        (
            (
                ('S', 'A', 8),
                ('S', 'B', 12),
                ('S', 'C', 26),
                ('S', 'D', 9),
                ('A', 'E', 3),
                ('B', 'E', 4),
                ('B', 'F', 6),
                ('C', 'G', 11),
                ('D', 'G', 2),
                ('D', 'H', 3),
                ('E', 'I', 9),
                ('E', 'J', 5),
                ('F', 'J', 7),
                ('G', 'J', 9),
                ('G', 'K', 2),
                ('H', 'K', 12),
                ('I', 'T', 8),
                ('J', 'I', 11),
                ('J', 'K', 20),
                ('K', 'T', 16),
            ),
            24,
        ),
    ),
)
def test_flow_network(graph_data, expected_max_flow):
    g = FlowNetwork('S', 'T', *graph_data)
    assert g.max_flow == expected_max_flow