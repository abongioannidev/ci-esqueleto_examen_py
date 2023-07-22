import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from typing import Optional, Tuple, Union
import customtkinter

'''
Ejercicio 2
Alumno: Nombre, Apellido
Division: Div J

'''


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar",command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=0,column=0, pady=10,padx=10)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar",command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2,column=0, pady=10,padx=10)
        

    def btn_agregar_on_click(self):
        print("hice click en agregar")
        
        
        
    def btn_mostrar_on_click(self):
        print("hice click en mostrar")


print(__name__)
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()  