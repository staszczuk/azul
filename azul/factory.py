from azul.bag import Bag
from azul.tile import Tile


class Factory:
    def __init__(self, id: int, bag: Bag) -> None:
        self._id: int = id
        self._tiles: list[Tile] = []

        for _ in range(4):
            self.tiles.append(bag.get_random_tile())

    @property
    def id(self) -> int:
        return self._id

    @property
    def tiles(self) -> list[Tile]:
        return self._tiles
