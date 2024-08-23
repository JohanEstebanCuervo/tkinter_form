Module tkinter_form.field_form
==============================
Programmed By Johan Esteban Cuervo Chica

Module logical form field

Classes
-------

`FieldForm(master, label: tkinter.ttk.Label, widget: tkinter.ttk.Widget, variable: Any, value: Any, description: tkinter.ttk.Label = None)`
:   form field
    contains all the objects required for a form field.
    
    Args:
        master (Form): Form
        label (ttk.Label): primer texto del campo
        widget (ttk.Widget): interactive part of the field
        variable (Any): tkinter variable field
        value (Any): initial value
        description (ttk.Label, optional): description of the field. Defaults to None.

    ### Methods

    `get(self)`
    :   return value logical
        
        Returns:
            any: field value

    `hide(self)`
    :   Hide field form

    `set(self, value: Any)`
    :   Set value field
        
        Args:
            value (Any): value

    `set_combobox_list(self, renames_list: list[str])`
    :   Set text combobox list
        
        Args:
            renames_list (list[str]): new renames list
        
        Raises:
            TypeError: No combobox field
            IndexError: difference in size between the old and the new list

    `set_description_text(self, value: str)`
    :   Set self.description
        
        Args:
            value (str): new_value

    `set_labels_text(self, value: str)`
    :   Set text from self.label
        
        Args:
            value (str): new_text

    `show(self)`
    :   show field form