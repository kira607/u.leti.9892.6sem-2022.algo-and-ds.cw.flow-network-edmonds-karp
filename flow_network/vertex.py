class Vertex:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} \'{self.name}\'>'

    def __str__(self) -> str:
        return repr(self)

    def __eq__(self, other: 'Vertex') -> bool:
        return hash(self) == hash(other)

    def __hash__(self) -> int:
        return hash(self.name)
