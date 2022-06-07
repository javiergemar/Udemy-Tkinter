# Importamos del módulo tkinter todos sus métodos y atributos.
from tkinter import *

# Estamos creando un objeto ventana
ventana = Tk()

'''
Creamos un objeto Label y lo asignamos a la variable etiqueta. En los parámetros de Label le decimos en
la ventana que se tiene que mostrar la etiqueta y una serie de parámetros. 
'''
etiqueta = Label(ventana, text='Hola mundo')

# Le decimos a ventana que muestre la etiqueta mediante el posicionamiento pack.
etiqueta.pack()

''' 
Mantiene la ventana abierta en pantalla hasta que decidamos cerrarlo. El código siempre tiene que
terminar con mainloop().
'''
ventana.mainloop()
