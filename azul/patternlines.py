from azul.tile import Tile


class PatternLines:
    def __init__(self) -> None:
        self._lines: list[list[Tile]] = []

        for i in reversed(range(5)):
            self._lines.append([])

            for _ in range(5 - i):
                self._lines[-1].append(None)

    @property
    def lines(self) -> list[list[Tile]]:
        return self._lines
