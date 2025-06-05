import random

from azul.tile import Tile
from azul.tilecolor import TileColor


class Bag:
    def __init__(self) -> None:
        self._tiles: list[Tile] = []

        for i, color in enumerate(TileColor):
            for j in range(20):
                self._tiles.append(Tile(20 * i + j, color))

    @property
    def tiles(self) -> list[Tile]:
        return self._tiles

    def get_random_tile(self) -> Tile:
        return self._tiles.pop(random.randint(0, len(self._tiles) - 1))
