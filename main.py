from azul.game import Game
from azul.gui.gui import GUI


def main() -> None:
    game: Game = Game(2)
    GUI(game)


if __name__ == "__main__":
    main()
