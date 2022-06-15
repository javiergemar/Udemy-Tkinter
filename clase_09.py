from tkinter import *

ventana = Tk()

menuBar = Menu(ventana)
ventana.config(menu=menuBar)

archivoMenu = Menu(menuBar, tearoff=0)  # Creamos el menú Archivo
# tearoff=0 elimina la linea discontinua que aparece en la parte superior del menú.
archivoMenu.add_command(label='Nuevo')
archivoMenu.add_command(label='Abrir')
archivoMenu.add_command(label='Guardar')
archivoMenu.add_command(label='Cerrar')
archivoMenu.add_separator()
archivoMenu.add_command(label='Salir', command=ventana.quit)

editMenu = Menu(menuBar, tearoff=0)
editMenu.add_command(label='Cortar')
editMenu.add_command(label='Copiar')
editMenu.add_command(label='Pegar')

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='Ayuda')
helpMenu.add_separator()            # Agrega una separación entre las dos entradas del menú.
helpMenu.add_command(label='Acerca de')

menuBar.add_cascade(label='Archivo', menu=archivoMenu)  # Agregamos el menú Archivo al menú principal y asignamos nombre
menuBar.add_cascade(label='Editar', menu=editMenu)
menuBar.add_cascade(label='Ayuda', menu=helpMenu)

ventana.mainloop()