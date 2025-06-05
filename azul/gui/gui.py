import tkinter as tk
import ttkbootstrap as ttk

from azul.game import Game
from azul.gui.bagwidget import BagWidget
from azul.gui.playerboardwidget import PlayerBoardWidget
from azul.gui.tablewidget import TableWidget


class GUI:
    def __init__(self, game: Game) -> None:
        self._game: Game = game

        self._root: tk.Tk = tk.Tk()
        self._root.title("Azul")

        self._style: ttk.Style = ttk.Style()
        self._style.configure("Tile.TButton", background="#000000")

        self._left_notebook: ttk.Notebook = ttk.Notebook(padding=(8, 8, 4, 8))
        self._left_notebook.grid(column=0, row=0, sticky="n")

        self._playerboardwidgets: list[PlayerBoardWidget] = []

        for player in self._game.players:
            self._playerboardwidgets.append(
                PlayerBoardWidget(self._left_notebook, player.playerboard)
            )
            self._left_notebook.add(
                self._playerboardwidgets[-1], text=f"Player {player.id}"
            )

        self._right_notebook: ttk.Notebook = ttk.Notebook(padding=(4, 8, 8, 8))
        self._right_notebook.grid(column=1, row=0, sticky="n")

        self._tablewidget: TableWidget = TableWidget(self._right_notebook, game.table)
        self._right_notebook.add(self._tablewidget, text="Table")

        self._bagwidget: BagWidget = BagWidget(self._right_notebook, game.table.bag)
        self._right_notebook.add(self._bagwidget, text="Bag")

        self._root.mainloop()
