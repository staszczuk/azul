from azul.player import Player
from azul.table import Table


class Game:
    def __init__(self, n_players: int) -> None:
        self._players: list[Player] = []

        for i in range(n_players):
            self._players.append(Player(i))

        self._table: Table = Table(n_players)

    @property
    def players(self) -> list[Player]:
        return self._players

    @property
    def table(self) -> Table:
        return self._table
