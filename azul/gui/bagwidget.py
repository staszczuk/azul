import tkinter as tk
import ttkbootstrap as ttk

from azul.bag import Bag
from azul.gui.tilewidget import TileWidget


class BagWidget(ttk.Frame):
    def __init__(self, master: tk.Misc, bag: Bag) -> None:
        super().__init__(master)

        self._tilewidgets: list[TileWidget] = []

        for i, tile in enumerate(bag.tiles):
            self._tilewidgets.append(TileWidget(self, tile=tile))
            self._tilewidgets[-1].grid(column=i % 10, row=i // 10)
