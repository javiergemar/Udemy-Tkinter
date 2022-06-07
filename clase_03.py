import tkinter as tk
from tkinter import ttk

window = tk.Tk()

def seleccionar(option):
    print(option)

def imprimir():
    ttk.Label(window, text='Imprimiendo...').pack()

'''
Nuestra función acepta un parámetro y como nuestra función será la acción del botón que vamos a crear
tenemos que utilizar una función lambda.
Si el usuario selecciona este botón el parámetro 'Python' se almacena la selección en el parámetro 'option'.
'''

ttk.Button(window, text='Python', command=lambda:seleccionar('Python')).pack(side='top')

ttk.Button(window, text='Java', command=imprimir).pack()

ttk.Button(window, text='JavaScript', command=lambda:seleccionar('JavaScript')).pack(side='bottom')

window.mainloop()
