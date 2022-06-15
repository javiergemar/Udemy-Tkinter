from distutils import command
from tkinter import *
from tkinter import messagebox

ventana = Tk()

menuBar = Menu(ventana)
ventana.config(menu=menuBar)

def cerrar():
    messagebox.askquestion('Cerrar', message='¿Estás seguro?')

def licencia():
    messagebox.showinfo('Versión', message='Versión 1.0')

def error():
    messagebox.showerror('¡ERROR CRÍTICO!', message='SE ENCONTRÓ UN ERROR FATAL')

def atencion():
    messagebox.showwarning('Atención', message='Esto es una advertencia')

archivoMenu = Menu(menuBar, tearoff=0)  # Creamos el menú Archivo
# tearoff=0 elimina la linea discontinua que aparece en la parte superior del menú.
archivoMenu.add_command(label='Nuevo')
archivoMenu.add_command(label='Abrir', command=atencion)
archivoMenu.add_command(label='Guardar', command=error)
archivoMenu.add_command(label='Cerrar', command=cerrar)
archivoMenu.add_separator()
archivoMenu.add_command(label='Salir', command=ventana.quit)

editMenu = Menu(menuBar, tearoff=0)
editMenu.add_command(label='Cortar')
editMenu.add_command(label='Copiar')
editMenu.add_command(label='Pegar')

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='Ayuda')
helpMenu.add_separator()            # Agrega una separación entre las dos entradas del menú.
helpMenu.add_command(label='Acerca de', command=licencia)

menuBar.add_cascade(label='Archivo', menu=archivoMenu)  # Agregamos el menú Archivo al menú principal y asignamos nombre
menuBar.add_cascade(label='Editar', menu=editMenu)
menuBar.add_cascade(label='Ayuda', menu=helpMenu)

ventana.mainloop()