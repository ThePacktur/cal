from CalculadoraBase import CalculadoraBase
import tkinter as tk

class Calculadora3(CalculadoraBase):
    def crear_interfaz(self):
        super().crear_interfaz()
        botones = [
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '*',
            '0', '.', '=', '/'
        ]
        self.crear_botones(botones)

    def crear_botones(self, botones):
        row_val, col_val = 1, 0
        for boton in botones:
            action = self.calcular if boton == '=' else lambda x=boton: self.agregar_caracter(x)
            tk.Button(self.root, text=boton, padx=20, pady=20, font=("Arial", 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        tk.Button(self.root, text='AC', padx=20, pady=20, font=("Arial", 18), command=self.limpiar_entrada).grid(row=row_val, column=0, columnspan=4)
