from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry('400x300')

cajaDeTexto1 = Spinbox(ventana, values=('Python', 'HTML5', 'Java', 'JavaScript'))
cajaDeTexto1.pack()

cajaDeTexto2 = Spinbox(ventana, values=('Carne', 'Verdura', 'Pasta'))
cajaDeTexto2.pack()

ventana.mainloop()