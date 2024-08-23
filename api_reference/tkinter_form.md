Module tkinter_form.tkinter_form
================================
Programmed By Johan Esteban Cuervo Chica

This code generates a tkinter form automatically from a base dictionary.
from a base dictionary. Returning a tk.Frame object
with some additional attributes.

Classes
-------

`Form(master: object, name_form: str, form_dict: dict, name_button: str = 'submit', button_command: <built-in function callable> = None)`
:   Form is a ttk.LabelFrame containing a form from a python dictionary with the
    from a Python dictionary with the additional methods.
    
    Args:
        master (object): tk.Tk content
        name_form (str): name form
        form_dict (dict): structure of the form with logical values
        name_button (str, optional): name button submit. Defaults to "submit".
        button_command (callable, optional): function for button. Defaults to None.
    
    Construct a Ttk Labelframe with parent master.
    
    STANDARD OPTIONS
    
        class, cursor, style, takefocus
    
    WIDGET-SPECIFIC OPTIONS
        labelanchor, text, underline, padding, labelwidget, width,
        height

    ### Ancestors (in MRO)

    * tkinter.ttk.Labelframe
    * tkinter.ttk.Widget
    * tkinter.Widget
    * tkinter.BaseWidget
    * tkinter.Misc
    * tkinter.Pack
    * tkinter.Place
    * tkinter.Grid

    ### Methods

    `get(self) ‑> dict`
    :   returns a dictionary with the values entered in the form.
        in the form.
        
        Returns:
            dict: dictionary with the structure of the form

    `hide(self)`
    :   hide form with tkinter method grid_remove()
        WARNING no use pack method

    `set(self, set_dict: dict) ‑> None`
    :   Change the values of the form
        
        Args:
            set_dict (dict): values to be set

    `set_command_button(self, new_command: <built-in function callable>)`
    :   Set command button form
        Args:
            new_command (callable): _description_

    `set_labels_text(self, set_labels: dict) ‑> None`
    :   Edit text labels Interfaces
        
        Args:
            set_labels (dict): labels to_edit

    `show(self)`
    :   show form with tkinter method grid()
        WARNING no use pack method

    `validation(self, dict_validations: dict[str, callable] | None, full_validation: bool = False, if_validation_false: <built-in function callable> = None)`
    :   validates the form data before the button command function.
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

`Value(val: Any, description: str)`
:   This class helps to enrich the field with a description.

    ### Class variables

    `description: str`
    :

    `val: Any`
    :