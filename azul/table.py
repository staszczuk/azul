from azul.bag import Bag
from azul.factory import Factory


class Table:
    def __init__(self, n_players: int) -> None:
        self._bag: Bag = Bag()

        self._factories: list[Factory] = []
        n_factories: int = None

        match (n_players):
            case 2:
                n_factories = 5
            case 3:
                n_factories = 7
            case 4:
                n_factories = 9

        for i in range(n_factories):
            self._factories.append(Factory(i, self._bag))

    @property
    def bag(self) -> Bag:
        return self._bag

    @property
    def factories(self) -> list[Factory]:
        return self._factories
