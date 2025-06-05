import tkinter as tk
import ttkbootstrap as ttk

from azul.factory import Factory
from azul.gui.tilewidget import TileWidget


class FactoryWidget(ttk.Frame):
    def __init__(self, master: tk.Misc, factory: Factory) -> None:
        super().__init__(master=master, padding=8)

        self._tilewidgets: list[TileWidget] = []

        for i, tile in enumerate(factory.tiles):
            self._tilewidgets.append(TileWidget(self, tile=tile))
            self._tilewidgets[-1].grid(column=i % 2, row=i // 2)
