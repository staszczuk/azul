from azul.tile import Tile


class Wall:
    def __init__(self) -> None:
        self._rows: list[list[Tile]] = []

        for _ in range(5):
            self._rows.append([])

            for _ in range(5):
                self._rows[-1].append(None)

    @property
    def rows(self) -> list[list[Tile]]:
        return self._rows
