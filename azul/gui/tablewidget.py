import tkinter as tk
import ttkbootstrap as ttk

from azul.gui.factorywidget import FactoryWidget
from azul.table import Table


class TableWidget(ttk.Frame):
    def __init__(self, master: tk.Misc, table: Table) -> None:
        super().__init__(master)

        self._factorywidgets: list[FactoryWidget] = []

        for i, factory in enumerate(table.factories):
            self._factorywidgets.append(FactoryWidget(self, factory))
            self._factorywidgets[-1].grid(column=i % 3, row=i // 3)
