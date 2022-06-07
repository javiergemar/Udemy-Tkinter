from tkinter import *

window = Tk()
window.title('Posicionamiento grid')    # El posicionamiento grid se realiza por filas y columnas.
window.geometry('400x200')

label = Label(window, text='Etiqueta')
label.grid(row=0, column=0)

button = Button(window, text='Botón')
button.grid(row=0, column=1)

window.mainloop()
