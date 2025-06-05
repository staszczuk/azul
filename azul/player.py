from azul.playerboard import PlayerBoard


class Player:
    def __init__(self, id: int) -> None:
        self._id: int = id
        self._playerboard: PlayerBoard = PlayerBoard()

    @property
    def id(self) -> int:
        return self._id

    @property
    def playerboard(self) -> PlayerBoard:
        return self._playerboard
