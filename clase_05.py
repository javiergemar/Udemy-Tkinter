from tkinter import *

window=Tk()
window.title('Entrada')
window.geometry('400x150')

name = StringVar()
surname = StringVar()

name.set('Escribe aquí tu nombre')
surname.set('Escribe aquí tu apellido')

def hello():
    print('Hello ' + name.get() + ' ' + surname.get())

def bye():
    print('Bye ' + name.get() + ' ' + surname.get())

label1 = Label(window, text='Escribe aquí tu nombre', bg='#F0F0F0')
label1.place(x=10, y=10)
entry1 = Entry(window, textvariable=name, bg='#FEFFD1')
entry1.place(x=170, y=10)

label2 = Label(window, text='Escribe aquí tu apellido', bg='#F0F0F0')
label2.place(x=10, y=40)
entry2 = Entry(window, textvariable=surname, bg='#FEFFD1')
entry2.place(x=170, y=40)

button1 = Button(window, text='Saludar ahora', command=hello, bg='#7E8A8B')
button1.place(x=10, y=100)

button2 = Button(window, text='Despedirse ahora', command=bye, bg='#7E8A8B')
button2.place(x=150, y=100)

button3 = Button(window, text='Salir', command=window.destroy, bg='#7E8A8B')
button3.place(x=325, y=100)

window.mainloop()
