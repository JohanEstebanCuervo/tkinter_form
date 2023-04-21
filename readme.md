# tkinter_form

tk_form is a simple module that helps you to create forms in tkinter easily and quickly from a base dictionary, saving certain repetitive tasks in the creation of a form and adding the verification of integer and float variables. In simple words it is similar to having a tkinter variable. Its value is a dictionary.

## Install

```bash
pip install tkinter_form
```

## Tutorial

### Fast Example

```python
import tkinter as tk
from tkinter_form import Form

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        estruct = {
            "high": 1.0,
            "width": 1.0,
            "round": False,
            "type of calculation": ["calculate area", "calculate perimeter"],
            "result": "",
        }
        self.form = Form(
            self,
            name_form="calculations of a rectangle",
            form_dict=estruct,
            name_config="calculate",
            button=True
        )
        self.form.pack()
        self.button = self.form.button

        self.button.config(command=self.calculate)
        self.mainloop()
    def calculate(self):
        """
        Calculate values rectangle
        """
        dict_vals = self.form.get()
        if dict_vals["type of calculation"] == "calculate area":
            value = dict_vals["high"] * dict_vals["width"]
        elif dict_vals["type of calculation"] == "calculate perimeter":
            value = 2 * dict_vals["high"] + 2 * dict_vals["width"]
        else:
            value = 0
        if dict_vals["round"]:
            value = round(value)
        result = {"result": str(value)}
        self.form.set(result)
if __name__ == "__main__":
    App()
```

With these lines we create the interface that performs the calculations of area and perimeter of a rectangle. This frees us the declaration of the labels and other objects returning a ttk.LabelFrame with the additional methods set(), get() and the attributes widgets and button.



![example](src/example.png)
