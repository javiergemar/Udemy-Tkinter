from tkinter import *

window = Tk()
window.title('Radiobuttons')
window.geometry('400x400')              # Definimos las dimensiones de la ventana
window.config(bg='goldenrod3')          # Asignamos un color para bg (o background)
window.resizable(False, False)          # Indicamos que el usuario no pueda redimensionar la ventana

def operation():
    number = num.get()
    if option.get() == 1:
        total = number*5
    elif option.get() == 2:
        total = number*10
    elif option.get() == 3:
        total = number*20
    elif option.get() == 4:
        total = number*30
    elif option.get() == 5:
        total = number*40
    else:
        total = number*number
    print(f'El total de la operación es: {str(total)}')

option = IntVar()
num = IntVar()

label1 = Label(window, text='Escriba su número', bg='goldenrod3')
label1.place(x=20, y=20)
entry1 = Entry(window, bd=3, font=('Arial', 11), textvariable=num)
entry1.place(x=150, y=20)

label2 = Label(window, text='Elija la cantidad:', bg='goldenrod3')
label2.place(x=20, y=50)
button1 = Button(window, text='Realizar operación', bg='goldenrod2', bd=3, command=operation)
button1.place(x=20, y=280)

x5 = Radiobutton(window, text='x5', value=1, bg='goldenrod2', bd=3, variable=option)
x5.place(x=20, y=80)
x10 = Radiobutton(window, text='x10', value=2, bg='goldenrod2', bd=3, variable=option)
x10.place(x=20, y=120)
x20 = Radiobutton(window, text='x20', value=3, bg='goldenrod2', bd=3, variable=option)
x20.place(x=20, y=160)
x30 = Radiobutton(window, text='x30', value=4, bg='goldenrod2', bd=3, variable=option)
x30.place(x=20, y=200)
x40 = Radiobutton(window, text='x40', value=5, bg='goldenrod2', bd=3, variable=option)
x40.place(x=20, y=240)

window.mainloop()