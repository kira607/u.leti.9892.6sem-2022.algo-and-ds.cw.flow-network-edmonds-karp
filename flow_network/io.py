import os
import graphviz

from .flow_network import FlowNetwork


def load_flow_network(path: str):
    with open(path, 'r') as f:
        lines = f.readlines()

    data = []

    for line in lines:
        source_vertex_name, target_vertex_name, capacity = [s.strip() for s in line.split(' ')]
        capacity = int(capacity)
        data.append((source_vertex_name, target_vertex_name, capacity))

    graph = FlowNetwork('S', 'T', *data)
    return graph


def export_flow_network(fn: FlowNetwork, path: str, name: str = 'graph') -> None:
    file_path = os.path.join(path, f'{name}.dot')
    graphviz.Source(fn.get_dot_string()).render(file_path)
