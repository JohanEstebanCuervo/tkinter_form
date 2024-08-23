"""
Module logical form field

Programmed By Johan Esteban Cuervo Chica
"""

import tkinter as tk
from tkinter import ttk
from typing import Any


class FieldForm:
    """
    form field
    contains all the objects required for a form field.

    Args:
        master (Form): Form
        label (ttk.Label): primer texto del campo
        widget (ttk.Widget): interactive part of the field
        variable (Any): tkinter variable field
        value (Any): initial value
        description (ttk.Label, optional): description of the field. Defaults to None.
    """

    def __init__(
        self,
        master,
        label: ttk.Label,
        widget: ttk.Widget,
        variable: Any,
        value: Any,
        description: ttk.Label = None,
    ):

        self.__configure_widgets = {
            float: self.__configure_float,
            int: self.__configure_int,
            str: self.__configure_str,
            bool: self.__configure_bool,
            list: self.__configure_list,
        }
        self.__master = master
        self.label = label
        self.widget = widget
        self.variable = variable
        self.description = description
        self.__hidden = False
        self.__combobox_relation: dict = None
        config = self.__configure_widgets[type(value)]
        config(widget, variable, value)

    def __configure_list(
        self, widget: ttk.Combobox, variable: tk.StringVar, values: list
    ) -> None:
        """
        Configure form value list

        Args:
            widget (ttk.Entry): ttk entry
            variable (tk.DoubleVar): var dict
            value (str): value set variable
        """

        self.__combobox_relation = dict(zip(values, values))
        variable.set(values[0])
        widget.config(state="readonly", values=values, textvariable=variable)

    def __configure_bool(
        self, widget: ttk.Checkbutton, variable: tk.BooleanVar, value: bool
    ) -> None:
        """
        Configure form value float

        Args:
            widget (ttk.Entry): ttk entry
            variable (tk.DoubleVar): var dict
            value (bool): value set variable
        """
        variable.set(value)
        widget.config(variable=variable)

    def __configure_float(
        self, widget: ttk.Entry, variable: tk.DoubleVar, value: float
    ) -> None:
        """
        Configure form value float

        Args:
            widget (ttk.Entry): ttk entry
            variable (tk.DoubleVar): var dict
            value (float): value set variable
        """
        variable.set(value)
        reg_fun = (self.__master.reg_validate_float, "%P")
        widget.config(validate="key", validatecommand=reg_fun, textvariable=variable)

    def __configure_str(
        self, widget: ttk.Entry, variable: tk.StringVar, value: str
    ) -> None:
        """
        Configure form value str

        Args:
            widget (ttk.Entry): ttk entry
            variable (tk.StringVar): var dict
            value (str): value set variable
        """
        variable.set(value)
        widget.config(textvariable=variable)

    def __configure_int(
        self, widget: ttk.Entry, variable: tk.IntVar, value: int
    ) -> None:
        """
        Configure form value int

        Args:
            widget (ttk.Entry): ttk entry
            variable (tk.IntVar): var dict
            value (int): value set variable
        """
        variable.set(value)
        reg_fun = (self.__master.reg_validate_int, "%P")

        widget.config(validate="key", validatecommand=reg_fun, textvariable=variable)

    def hide(self):
        """
        Hide field form
        """

        if self.__hidden:
            return

        self.label.grid_remove()
        self.widget.grid_remove()

        if isinstance(self.description, ttk.Label):
            self.description.grid_remove()

        self.__hidden = True

    def show(self):
        """
        show field form
        """
        if not self.__hidden:
            return
        self.label.grid()
        self.widget.grid()
        if isinstance(self.description, ttk.Label):
            self.description.grid()

        self.__hidden = False

    def get(self):
        """
        return value logical

        Returns:
            any: field value
        """
        if self.__combobox_relation:
            value_select = self.variable.get()
            return self.__combobox_relation[value_select]

        return self.variable.get()

    def set(self, value: Any):
        """
        Set value field

        Args:
            value (Any): value
        """
        self.variable.set(value)

    def set_labels_text(self, value: str):
        """
        Set text from self.label

        Args:
            value (str): new_text
        """
        self.label.config(text=value)

    def set_description_text(self, value: str):
        """
        Set self.description

        Args:
            value (str): new_value
        """
        self.description.config(text=value)

    def set_combobox_list(self, renames_list: list):
        """
        Set text combobox list

        Args:
            renames_list (list[str]): new renames list

        Raises:
            TypeError: No combobox field
            IndexError: difference in size between the old and the new list
        """
        if not self.__combobox_relation:
            raise TypeError(f'Widget not Combobox field {self.label.cget("text")}')

        list_elements: list = self.widget.cget("values")

        if len(list_elements) != len(renames_list):
            raise IndexError(
                f"renames list diff size combobox list {len(list_elements)}!={len(renames_list)}"
            )

        values = list(self.__combobox_relation.values())

        self.__combobox_relation = dict(zip(renames_list, values))

        index = list_elements.index(self.variable.get())
        self.variable.set(renames_list[index])

        self.widget.configure(values=renames_list)
