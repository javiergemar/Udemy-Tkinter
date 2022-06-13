import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# It creates a new window.
ventana = tk.Tk()
# It sets the size of the window.
ventana.geometry('300x300')
# It sets the window to be not resizable.
ventana.resizable(0,0)
# It sets the title of the window.
ventana.title('Demo de Radiobutton')

def mostrar_tamano_seleccionado():
    """
    It creates a message box that displays the value of the variable tamano_seleccionado
    """
    showinfo(title='Result', message=tamano_seleccionado.get())

# It creates a variable that will store the value of the selected radiobutton.
tamano_seleccionado =tk.StringVar()

# A tuple of tuples. Each tuple contains the text to display and the value to return.
tamanos = (('Small', 'S'), ('Medium', 'M'), ('Large', 'L'), ('Extra Large', 'XL'), ('Giant', 'G'))

# It creates a label with the text '¿Cuál es tu talla de camiseta?'
etiqueta = ttk.Label(ventana, text='¿Cuál es tu talla de camiseta?')
# Packing the label `etiqueta` with a padding of 5 pixels in the x and y axis.
etiqueta.pack(fill='x', padx=5, pady=5)

for tamano in tamanos:
    """
    Creating a radiobutton for each tuple in the tuple `tamanos`
    """
    rb = ttk.Radiobutton(ventana, text=tamano[0], variable=tamano_seleccionado, value=tamano[1])
    rb.pack(fill='x', padx=5, pady=5)

# It creates a button that calls the function `mostrar_tamano_seleccionado` when it is clicked.
button = ttk.Button(ventana, text='Obtener talla seleccionada', command=mostrar_tamano_seleccionado)
button.pack(fill='x', padx=5, pady=5)

# A method that keeps the window open until it is closed.
ventana.mainloop()

"""
Comments created by Mintlify plugin. Link: https://www.mintlify.com
"""