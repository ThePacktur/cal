import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        
        self.entrada_texto = tk.StringVar()
        self.crear_interfaz()
        
    def crear_interfaz(self):
        entrada = tk.Entry(self.root, textvariable=self.entrada_texto, font=("Arial", 24), bd=8, insertwidth=2, width=14, borderwidth=4)
        entrada.grid(row=0, column=0, columnspan=4)

        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for boton in botones:
            if boton == '=':
                action = self.calcular
            else:
                action = lambda x=boton: self.agregar_caracter(x)
            tk.Button(self.root, text=boton, padx=20, pady=20, font=("Arial", 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.root, text='C', padx=20, pady=20, font=("Arial", 18), command=self.limpiar_entrada).grid(row=row_val, column=0, columnspan=4)
        
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

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()