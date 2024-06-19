import tkinter as tk
from Calculadora1 import Calculadora1
from Calculadora2 import Calculadora2
from Calculadora3 import Calculadora3
from Calculadora4 import Calculadora4

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Calculadoras")
        self.calculadoras = {
            "Calculadora 1": Calculadora1,
            "Calculadora 2": Calculadora2,
            "Calculadora 3": Calculadora3,
            "Calculadora 4": Calculadora4
        }
        self.mostrar_calculadora("Calculadora 1")

    def mostrar_calculadora(self, calc_name):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.calculadoras[calc_name](self.root, self)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
