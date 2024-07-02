"""
Programmed By Johan Esteban Cuervo Chica

This code generates a tkinter form automatically from a base dictionary.
from a base dictionary. Returning a tk.Frame object
with some additional attributes.
"""

import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass
from typing import Any


@dataclass
class Value:
    """ This class helps to enrich the field with a description. """
    val: Any
    description: str


class Form(ttk.LabelFrame):
    """
    Form is a ttk.LabelFrame containing a form from a python dictionary with the
    from a Python dictionary with the additional methods
    additional methods:

    self.get()
    self.set()
    self.widgets
    self.button

    Args:
        master (object): tk container
        name_form (str): Form Name
        form_dict (dict): base dictionary of the form
        name_config (str, optional): Name of the button that performs an action with the form..
            Defaults to "configure".
        button (bool, optional): Action button. Defaults to True.
    """

    def __init__(
        self,
        master: object,
        name_form: str,
        form_dict: dict,
        name_config: str = "configure",
        button: bool = True,
    ) -> None:
        super().__init__(master, text=name_form)

        self.__type_vars = {
            "float": tk.DoubleVar,
            "int": tk.IntVar,
            "str": tk.StringVar,
            "bool": tk.BooleanVar,
            "list": tk.StringVar,
        }

        self.__configure_widgets = {
            "float": self.__configure_float,
            "int": self.__configure_int,
            "str": self.__configure_str,
            "bool": self.__configure_bool,
            "list": self.__configure_list,
        }

        self.__type_widgets = {
            "float": ttk.Entry,
            "int": ttk.Entry,
            "str": ttk.Entry,
            "bool": ttk.Checkbutton,
            "list": ttk.Combobox,
        }

        self.button = None
        self.__create_widgets(form_dict, name_config, button)

    def __validate_float(self, new_text: str) -> bool:
        """
        Validate Float number in tk.entry

        Args:
            new_text (str): entry text

        Returns:
            bool: True si es Float, False si no es float
        """
        try:
            float(new_text)
            return True
        except ValueError:
            if new_text == "":
                return True

            return False

    def __validate_int(self, new_text: str) -> bool:
        """
        Validate Int number in tk.entry

        Args:
            new_text (str): entry text

        Returns:
            bool: True si es int, False si no es int
        """
        try:
            int(new_text)
            return True
        except ValueError:
            if new_text == "":
                return True

            return False

    def __configure_list(
        self, widget: ttk.Combobox, variable: tk.StringVar, value: str
    ) -> None:
        """
        Configure form value list

        Args:
            widget (ttk.Entry): ttk entry
            variable (tk.DoubleVar): var dict
            value (str): value set variable
        """
        variable.set(value[0])
        widget.config(state="readonly", values=value, textvariable=variable)

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
        reg_fun = (self.register(self.__validate_float), "%P")

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
        reg_fun = (self.register(self.__validate_int), "%P")

        widget.config(validate="key", validatecommand=reg_fun, textvariable=variable)

    def __create_widgets(self, form_dict: dict, name_config: str, button: bool) -> None:
        """
        Create form widgets

        Args:
            form_dict (dict): form dict base
            name_config (str): name_config
            button (bool): button_config
        """
        self.widgets = {}
        self.__vars = {}
        index = 0
        for dict_vals in form_dict.items():
            index += 1
            name_key, value, description = *dict_vals, None
            if isinstance(value, Value):
                value, description = value.val, value.description

            type_value = str(type(value))[8:-2]
            tk.Grid.rowconfigure(self, index, weight=1)
            if type_value == "dict":
                widget = Form(self, name_key, value, button=False)
                widget.grid(row=index, column=0, columnspan=2, sticky="nesw")

                self.__vars[name_key] = widget
                self.widgets[name_key] = widget

                ult_val = index

                continue

            variable = self.__type_vars[type_value]()
            self.__vars[name_key] = variable
            widget = self.__type_widgets[type_value](self)
            tk.Grid.columnconfigure(self, 1, weight=1)
            widget.grid(row=index, column=1, sticky="nesw", padx=2, pady=2)
            label = ttk.Label(self, text=name_key)
            tk.Grid.columnconfigure(self, 0, weight=1)
            label.grid(row=index, column=0, sticky="nes", padx=2, pady=2)
	
            # Add a further description to the row below the widget
            if description:
                index += 1
                description_label = ttk.Label(self, text=description)
                description_label.grid(row=index, column=1, columnspan=2, sticky="nesw", padx=2, pady=2)


            config = self.__configure_widgets[type_value]

            config(widget, variable, value)

            self.widgets[name_key] = [label, widget]

            ult_val = index

        if button is True:
            self.button = ttk.Button(
                self, text=name_config, command=lambda: print(self.get())
            )
            self.button.grid(row=ult_val + 1, column=0, columnspan=2, sticky="nesw")

    def get(self) -> dict:
        """
        returns a dictionary with the values entered in the form.
        in the form.

        Returns:
            dict: dictionary with the structure of the form
        """
        plain_dict = {}

        for key, var in self.__vars.items():
            try:
                value = var.get()

            except tk.TclError:
                value = "0"
                var.set(0)

            plain_dict[key] = value

        return plain_dict

    def set(self, set_dict: dict) -> None:
        """
        Change the values of the form

        Args:
            set_dict (dict): values to be set

        """
        for key, var in set_dict.items():
            self.__vars[key].set(var)

    def set_labels_text(self, set_labels: dict) -> None:
        """
        Edit text labels Interfaces

        Args:
            set_labels (dict): labels to_edit
        """
        for key, var_name in set_labels.items():
            if key == "__form__":
                self.config(text=var_name)
                continue
            if isinstance(var_name, dict):
                self.widgets[key].set_labels_text(var_name)
                continue

            self.widgets[key][0].config(text=var_name)
