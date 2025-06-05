import tkinter as tk
import ttkbootstrap as ttk

from azul.gui.tilewidget import TileWidget
from azul.patternlines import PatternLines


class PatternLinesWidget(ttk.Frame):
    def __init__(self, master: tk.Misc, patternlines: PatternLines) -> None:
        super().__init__(master=master, padding=8)

        self._tilewidgets: list[TileWidget] = []

        for i, line in enumerate(patternlines.lines):
            for j, tile in enumerate(line):
                self._tilewidgets.append(TileWidget(self, tile=tile))
                self._tilewidgets[-1].grid(column=5 - j, row=i)
