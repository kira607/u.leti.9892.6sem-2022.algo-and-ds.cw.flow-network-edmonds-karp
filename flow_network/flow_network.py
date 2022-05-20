from typing import Any, Dict, Optional, Tuple

from .edge import Edge
from .vertex import Vertex
from ._missing import _missing


class FlowNetwork:
    def __init__(self, source: str = 'S', sink: str = 'T', *edges: Tuple[str, str, int]):
        self._vertices: Dict[str, Vertex] = {}
        self._edges: Dict[Tuple[Vertex, Vertex], Edge] = {}
        self._source = source
        self._sink = sink
        for a, b, cap in edges:
            self.add_edge(a, b, cap, 0)
        self._max_flow = self._get_max_flow()

    def __len__(self):
        return len(self._vertices)

    @property
    def source(self):
        return self._vertices[self._source]

    @property
    def sink(self):
        return self._vertices[self._sink]

    @property
    def max_flow(self) -> int:
        return self._max_flow

    def vertex(self, vertex_name: str, default: Any = _missing) -> Vertex:
        v = self._vertices.get(vertex_name, default)
        if v is _missing:
            raise KeyError(f'Vertex {vertex_name} is not present in the graph.')
        return v

    def edge(self, v1: str, v2: str, default: Any = _missing) -> Edge:
        e = self._edges.get((self.vertex(v1), self.vertex(v2)), default)
        if e is _missing:
            raise KeyError(f'Edge ({v1}, {v2}) is not present in the graph.')
        return e

    def vertices(self) -> Tuple[Vertex]:
        return tuple(self._vertices.values())

    def edges(self, start_vertex: str = None) -> Tuple[Edge]:
        if not start_vertex:
            return tuple(self._edges.values())
        start_vertex = self.vertex(start_vertex)
        edges = []
        for (v1, _), edge in self._edges.items():
            if v1 == start_vertex:
                edges.append(edge)
        return tuple(edges)

    def add_vertex(self, name: str) -> Vertex:
        existing = self._vertices.get(name)
        if existing:
            return existing
        vertex = Vertex(name)
        self._vertices[name] = vertex
        return vertex

    def add_edge(self, v1: Vertex, v2: Vertex, capacity: int, flow: int) -> Edge:
        v1, v2 = self.add_vertex(v1), self.add_vertex(v2)
        key = (v1, v2)
        existing = self._edges.get(key)
        if existing:
            return existing
        edge = Edge(v1, v2, capacity, flow)
        self._edges[key] = edge
        return edge

    def get_dot_string(self) -> str:
        s = 'digraph {\nrankdir="LR";\n'
        for e in self._edges.values():
            s += e.get_dot_string()
        s += '}'
        return s

    def _get_max_flow(self) -> int:
        ap = self._get_augmenting_path()
        while ap:
            bottleneck = min(ap, key=lambda x: x.residual_capacity).residual_capacity
            for edge in ap:
                edge.flow = edge.flow + bottleneck
            ap = self._get_augmenting_path()
        return sum(e.flow for e in self.edges(self.source))

    def _get_augmenting_path(self) -> Optional[Tuple[Edge]]:
        queue = [self.source]
        paths = {self.source: []}
        while queue:
            u = queue.pop(0)
            for v in self.vertices():
                rc = self._get_residual_capacity(u.name, v.name)
                edge = self.edge(u.name, v.name, None)
                if not (rc and edge):
                    continue
                if rc > 0 and v not in paths:
                    paths[v] = paths[u] + [edge]
                    if v == self.sink:
                        return paths[v]
                    queue.append(v)
        return None

    def _get_residual_capacity(self, v1: str, v2: str) -> Optional[int]:
        edge = self.edge(v1, v2, None)
        if edge:
            return edge.residual_capacity
        edge = self.edge(v2, v1, None)
        if edge:
            return -edge.residual_capacity
        return None
