import tkinter as tk
from tkinter_form import Form


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        estruct = {
            "measures": {"high": 1.0, "width": 1.0},
            "round": False,
            "type of calculation": ["calculate area", "calculate perimeter"],
            "result": "",
        }
        self.form = Form(
            self,
            name_form="calculations of a rectangle",
            form_dict=estruct,
            name_config="calculate",
            button=True,
        )
        rename_labels = {
            "__form__": "Calculos Rectangulo",
            "measures": {
                "__form__": "medidas",
                "width": "ancho",
                "high": "alto",
            },
            "round": "redondear",
            "type of calculation": "tipo de calculo",
            "result": "resultado",
        }
        self.form.set_labels_text(rename_labels)
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
