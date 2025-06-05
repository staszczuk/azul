import tkinter as tk
import ttkbootstrap as ttk

from azul.gui.patternlineswidget import PatternLinesWidget
from azul.gui.wallwidget import WallWidget
from azul.playerboard import PlayerBoard


class PlayerBoardWidget(ttk.Frame):
    def __init__(self, master: tk.Misc, playerboard: PlayerBoard) -> None:
        super().__init__(master)

        self._patternlineswidget: PatternLinesWidget = PatternLinesWidget(
            self, playerboard.patternlines
        )
        self._patternlineswidget.grid(column=0, row=0)

        self._wallwidget: WallWidget = WallWidget(self, playerboard.wall)
        self._wallwidget.grid(column=1, row=0)
