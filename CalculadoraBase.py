import tkinter as tk
from tkinter import messagebox

class CalculadoraBase:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.entrada_texto = tk.StringVar()
        self.crear_interfaz()

    def crear_interfaz(self):
        entrada = tk.Entry(self.root, textvariable=self.entrada_texto, font=("Arial", 24), bd=8, insertwidth=2, width=14, borderwidth=4)
        entrada.grid(row=0, column=0, columnspan=4)
        self.crear_menu()

    def crear_menu(self):
        menu_bar = tk.Menu(self.root)
        calculadora_menu = tk.Menu(menu_bar, tearoff=0)
        for calc in self.app.calculadoras:
            calculadora_menu.add_command(label=calc, command=lambda x=calc: self.app.mostrar_calculadora(x))
        menu_bar.add_cascade(label="Calculadoras", menu=calculadora_menu)
        self.root.config(menu=menu_bar)

    def agregar_caracter(self, caracter):
        self.entrada_texto.set(self.entrada_texto.get() + caracter)

    def limpiar_entrada(self):
        self.entrada_texto.set('')

    def calcular(self):
        try:
            operacion = self.entrada_texto.get()
            resultado = str(eval(operacion))
            self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror("Error", "Operación inválida")
