from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Agenda')
root.geometry('700x600')
colorFondo = '#000066'
colorLetra = '#ffffff'
root.configure(background=colorFondo)

# Creating a variable that will be used to store the value of the entry box.
nombre = StringVar()
apellido = StringVar()
correo = StringVar()
telefono = StringVar()
eliminar = StringVar()

etiquetaTitulo = Label(root, text='Mi aplicación', fg=colorLetra, bg=colorFondo)
etiquetaTitulo.place(x=270, y=10)

etiquetaNombre = Label(root, text='Nombre', fg=colorLetra, bg=colorFondo)
etiquetaNombre.place(x=50, y=50)
entradaNombre = Entry(root, textvariable=nombre)
entradaNombre.place(x=150, y=50)

etiquetaApellido = Label(root, text='Apellido', fg=colorLetra, bg=colorFondo)
etiquetaApellido.place(x=50, y=80)
entradaApellido = Entry(root, textvariable=apellido)
entradaApellido.place(x=150, y=80)

etiquetaCorreo = Label(root, text='Email', fg=colorLetra, bg=colorFondo)
etiquetaCorreo.place(x=50, y=110)
entradaCorreo = Entry(root, textvariable=correo)
entradaCorreo.place(x=150, y=110)

etiquetaTelefono = Label(root, text='Teléfono', fg=colorLetra, bg=colorFondo)
etiquetaTelefono.pack(x=)


root.mainloop()
