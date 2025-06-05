from azul.tilecolor import TileColor


class Tile:
    def __init__(self, id: int, color: TileColor) -> None:
        self._id: int = id
        self._color: TileColor = color

    @property
    def id(self) -> int:
        return self._id

    @property
    def color(self) -> TileColor:
        return self._color
