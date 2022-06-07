from tkinter import *

window = Tk()
window.title('Posicionamiento grid')    # El posicionamiento grid se realiza por filas y columnas.
window.geometry('400x200')

label = Label(window, text='Etiqueta')
label.place(x=30, y=60)

button = Button(window, text='Botón')
button.place(x=90, y=60)

window.mainloop()