from azul.patternlines import PatternLines
from azul.wall import Wall


class PlayerBoard:
    def __init__(self) -> None:
        self._patternlines: PatternLines = PatternLines()
        self._wall: Wall = Wall()

    @property
    def patternlines(self) -> PatternLines:
        return self._patternlines

    @property
    def wall(self) -> Wall:
        return self._wall
