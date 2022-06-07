from tkinter import *

window=Tk()
window.title('Posicionamiento')
window.geometry('500x200')

def saludo():
    print('Hola te saludo')

def minimizar():
    window.iconify()

label1 = Label(window, text='Saluda desde aquí')
label1.place(x=30, y=50)

label2 = Label(window, text='Minimizar desde aquí')
label2.place(x=30, y=100)

button1 = Button(window, text='Haz click aquí para saludo', command=saludo)
button1.place(x=200, y=50)

button2 = Button(window, text='Haz click aquí para minimizar', command=minimizar)
button2.place(x=200, y=100)

window.mainloop()
