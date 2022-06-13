from tkinter import *

window=Tk()
window.title('Entrada')
window.geometry('400x400')
window.resizable(0,0)       # No permitimos que el usuario cambie el tamaño de la pantalla

# Creating a variable that will be used to store the text that will be displayed in the entry3 widget.
regard = StringVar()

name = StringVar(value='Escribe aquí')
surname = StringVar(value='Escribe aquí')

'''
Podemos establecer un valor inicial de la siguiente manera:

name.set('Escribe aquí')
surname.set('Escribe aquí')

En lugar de hacerlo entre los paréntesis del StringVar.
'''

def hello():
    print('Hello ' + name.get() + ' ' + surname.get())

def bye():
    print('Bye ' + name.get() + ' ' + surname.get())

def regards():
    regard.set('Hola ' + name.get() + ' ' + surname.get())

label1 = Label(window, text='Escribe aquí tu nombre', bg='#F0F0F0', bd=0.5, relief='raised', font=('Arial', 11))
label1.place(x=10, y=10)
entry1 = Entry(window, textvariable=name, bg='#FEFFD1', bd=1)
entry1.place(x=170, y=10)

label2 = Label(window, text='Escribe aquí tu apellido', bg='#F0F0F0', bd=0.5, relief='raised', font=('Arial', 11))
label2.place(x=10, y=40)
entry2 = Entry(window, textvariable=surname, bg='#FEFFD1', bd=1)
entry2.place(x=170, y=40)

button1 = Button(window, text='Saludar ahora', command=regards, bg='#7E8A8B', bd=1)
button1.place(x=10, y=100)

button2 = Button(window, text='Despedirse ahora', command=bye, bg='#7E8A8B', bd=1)
button2.place(x=150, y=100)

button3 = Button(window, text='Salir', command=window.destroy, bg='#7E8A8B', bd=1)
button3.place(x=325, y=100)

entry3 = Entry(window, bd=20, font=('Arial', 11), textvariable=regard, state='disabled')
entry3.place(x=80, y=220)

window.mainloop()
