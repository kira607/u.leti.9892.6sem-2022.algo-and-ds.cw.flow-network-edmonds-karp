from .vertex import Vertex


class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, capacity: int, flow: int = 0) -> None:
        self.v1 = v1
        self.v2 = v2
        self._capacity = capacity
        self._flow = flow
        self._test_flow()

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} ({self.v1.name}, {self.v2.name}) ({self.flow}/{self._capacity})>'

    @property
    def residual_capacity(self) -> int:
        return self._capacity - self.flow

    @property
    def flow(self) -> int:
        return self._flow

    @flow.setter
    def flow(self, value: int):
        self._flow = value
        self._test_flow()

    def get_dot_string(self) -> str:
        src = f'"{self.v1.name}"'
        arrw = ' -> '
        tgt = f'"{self.v2.name}"'
        attrs = f'[label="{self.flow}/{self._capacity}"]'
        return f'{src}{arrw}{tgt}{attrs}\n'

    def _test_flow(self) -> None:
        if self.flow > self._capacity:
            raise ValueError(f'Flow ({self.flow}) must be <= capacity ({self._capacity})')