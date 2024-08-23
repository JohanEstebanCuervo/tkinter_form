"""
This code generates a tkinter form automatically from a base dictionary.
from a base dictionary. Returning a tk.Frame object
with some additional attributes.

Programmed By Johan Esteban Cuervo Chica
"""

import tkinter as tk
from tkinter import ttk
import re
from typing import Any

from .field_form import FieldForm

class Value:
    """This class helps to enrich the field with a description."""

    def __init__(self, val:Any, description:str):
        self.val = val
        self.description = description


class Form(ttk.LabelFrame):
    """
    Form is a ttk.LabelFrame containing a form from a python dictionary with the
    from a Python dictionary with the additional methods.

    Args:
        master (object): tk.Tk content
        name_form (str): name form
        form_dict (dict): structure of the form with logical values
        name_button (str, optional): name button submit. Defaults to "submit".
        button_command (callable, optional): function for button. Defaults to None.
    """

    def __init__(
        self,
        master: object,
        name_form: str,
        form_dict: dict,
        name_button: str = "submit",
        button_command: callable = None,
    ) -> None:

        super().__init__(master, text=name_form)
        self.__register_validations()

        self.fields: dict = {}

        self.__type_vars = {
            float: tk.DoubleVar,
            int: tk.IntVar,
            str: tk.StringVar,
            bool: tk.BooleanVar,
            list: tk.StringVar,
        }

        self.__type_widgets = {
            float: ttk.Entry,
            int: ttk.Entry,
            str: ttk.Entry,
            bool: ttk.Checkbutton,
            list: ttk.Combobox,
        }

        self.__hidden = False
        self.__validation = False
        self.__full_validation = False
        self.__if_validation_false: callable = None
        self.__command = None
        self.button = None
        self.__create_widgets(form_dict, name_button, button_command)
        self.__styles()

    def __register_validations(self):

        self.reg_validate_int = self.register(self.__validate_int)
        self.reg_validate_float = self.register(self.__validate_float)

    def __validate_float(self, new_text: str) -> bool:
        """
        Validate Float number in tk.entry

        Args:
            new_text (str): entry text

        Returns:
            bool: True si es Float, False si no es float
        """

        if not new_text:
            return True

        pattern = r"^-?[0-9]*\.?[0-9]*$"
        if not re.fullmatch(pattern, new_text):
            return False

        return True

    def __validate_int(self, new_text: str) -> bool:
        """
        Validate Int number in tk.entry

        Args:
            new_text (str): entry text

        Returns:
            bool: True si es int, False si no es int
        """
        if not new_text:
            return True

        pattern = r"(?=^((?!0)(?!-0)|0$))^-?[0-9]*$"
        if not re.fullmatch(pattern, new_text):
            return False

        return True

    def __styles(self):

        self.__style = ttk.Style()
        try:
            self.__style.element_create("plain.field", "from", "clam")
        except tk.TclError:
            return

        self.__style.layout(
            "ErrorStyle.TEntry",
            [
                (
                    "Entry.plain.field",
                    {
                        "children": [
                            (
                                "Entry.background",
                                {
                                    "children": [
                                        (
                                            "Entry.padding",
                                            {
                                                "children": [
                                                    (
                                                        "Entry.textarea",
                                                        {"sticky": "nswe"},
                                                    )
                                                ],
                                                "sticky": "nswe",
                                            },
                                        )
                                    ],
                                    "sticky": "nswe",
                                },
                            )
                        ],
                        "border": "2",
                        "sticky": "nswe",
                    },
                )
            ],
        )

        self.__style.configure(
            "ErrorStyle.TEntry",
            background="red",
            foreground="black",
            fieldbackground="#ff9999",
        )

        self.__style.layout(
            "Normal.TEntry",
            [
                (
                    "Entry.plain.field",
                    {
                        "children": [
                            (
                                "Entry.background",
                                {
                                    "children": [
                                        (
                                            "Entry.padding",
                                            {
                                                "children": [
                                                    (
                                                        "Entry.textarea",
                                                        {"sticky": "nswe"},
                                                    )
                                                ],
                                                "sticky": "nswe",
                                            },
                                        )
                                    ],
                                    "sticky": "nswe",
                                },
                            )
                        ],
                        "border": "2",
                        "sticky": "nswe",
                    },
                )
            ],
        )

        self.__style.configure(
            "Normal.TEntry",
            background="white",
            foreground="black",
            fieldbackground="white",
        )

    def __create_widgets(
        self, form_dict: dict, name_config: str, button_command: callable
    ) -> None:
        """
        Create form widgets

        Args:
            form_dict (dict): form dict base
            name_config (str): name_config
            button (bool): button_config
        """

        for index, (name_key, value) in enumerate(form_dict.items()):

            description = None
            if isinstance(value, Value):
                value, description = value.val, value.description

            self.rowconfigure(index, weight=1)

            if isinstance(value, dict):
                widget = Form(self, name_key, value)
                widget.grid(row=index, column=0, columnspan=3, sticky="nesw")

                self.fields[name_key] = widget
                last_index = index
                continue

            variable = self.__type_vars[type(value)]()
            widget = self.__type_widgets[type(value)](self)

            self.columnconfigure(1, weight=1)
            widget.grid(row=index, column=1, sticky="nesw", padx=2, pady=2)
            label = ttk.Label(self, text=name_key)
            self.columnconfigure(0, weight=1)
            label.grid(row=index, column=0, sticky="nes", padx=2, pady=2)

            # Add a further description to the row below the widget
            description_label = None
            if not description is None:
                description_label = ttk.Label(self, text=description)
                description_label.grid(
                    row=index, column=2, sticky="nesw", padx=2, pady=2
                )

            self.fields[name_key] = FieldForm(
                master=self,
                label=label,
                widget=widget,
                variable=variable,
                value=value,
                description=description_label,
            )

            last_index = index

        if button_command:
            self.__command = button_command
            self.button = ttk.Button(
                self, text=name_config, command=self.__command_button
            )
            self.button.grid(row=last_index + 1, column=0, columnspan=3, sticky="nesw")

    def hide(self):
        """
        hide form with tkinter method grid_remove()
        WARNING no use pack method
        """

        if self.__hidden:
            return

        self.grid_remove()
        self.__hidden = True

    def show(self):
        """
        show form with tkinter method grid()
        WARNING no use pack method
        """
        if not self.__hidden:
            return
        self.grid()
        self.__hidden = False

    def get(self) -> dict:
        """
        returns a dictionary with the values entered in the form.
        in the form.

        Returns:
            dict: dictionary with the structure of the form
        """
        plain_dict = {}

        for key, field in self.fields.items():
            try:
                value = field.get()
            except tk.TclError:
                value = "0"
                field.set(0)

            plain_dict[key] = value

        return plain_dict

    def set(self, set_dict: dict) -> None:
        """
        Change the values of the form

        Args:
            set_dict (dict): values to be set

        """

        for key, var in set_dict.items():
            self.fields[key].set(var)

    def set_labels_text(self, set_labels: dict) -> None:
        """
        Edit text labels Interfaces

        Args:
            set_labels (dict): labels to_edit
        """
        for key, text in set_labels.items():

            if key == "__form__":
                self.config(text=text)
            elif key == "__button__":
                self.button.config(text=text)

            elif key.startswith("__description__"):
                key = key.replace("__description__", "")
                self.fields[key].set_description_text(text)

            elif key.startswith("__list__"):
                key = key.replace("__list__", "")
                self.fields[key].set_combobox_list(text)

            else:
                self.fields[key].set_labels_text(text)

    def validation(
        self,
        dict_validations: dict,
        full_validation: bool = False,
        if_validation_false: callable = None,
    ):
        """
        validates the form data before the button command function.
        According to a dictionary with the same keys as the form which can contain regular
        expressions which are evaluated with full_match method.
        Or have functions which return a boolean value and receive as argument the value to
        evaluate.

        Args:
            dict_validations (dict[str, callable] | None): regex or functions validation if 
                None overrides data validation.
            full_validation (bool, optional): if true validates the entire form. Defaults to False.
            if_validation_false (callable, optional): function in case the validation is false 
                Defaults to None.

        Raises:
            TypeError: if dict_validation no dict o None
        """
        if dict_validations is None:
            self.__validation = False
            self.__full_validation = False
            self.__if_validation_false = None

        elif isinstance(dict_validations, dict):
            self.__validation = dict_validations
            self.__full_validation = full_validation
            self.__if_validation_false = if_validation_false
        else:
            raise TypeError("No type correct for dict_validations")

    def __validate(self, dict_validations: dict, form) -> bool:
        result = True
        results = form.get()
        for key, validation in dict_validations.items():
            if isinstance(validation, dict):  # dict form within the form
                if not self.__validate(validation, form.fields[key]):
                    if self.__full_validation:
                        result = False
                    else:
                        return False

                continue

            elif isinstance(validation, str):  # validate regex
                re_expresion = validation
                value = str(results[key])
                result_val = re.fullmatch(re_expresion, value)

            else:  # validate function
                result_val = validation(results[key])

            if not result_val:  # if validation field false or None
                form.fields[key].widget.config(style="ErrorStyle.TEntry")
                if self.__full_validation:
                    result = False
                else:
                    return False
            else:
                form.fields[key].widget.config(style="Normal.TEntry")

        return result

    def set_command_button(self, new_command: callable):
        """
        Set command button form
        Args:
            new_command (callable): _description_
        """
        self.__command = new_command

    def __command_button(self):

        if self.__validation:
            result = self.__validate(self.__validation, self)

            if not result and self.__if_validation_false:

                self.__if_validation_false()

            if not result:
                return

        self.__command()
