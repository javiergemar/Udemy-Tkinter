from tkinter import *

ventana = Tk()
ventana.title('Primera ventana')
ventana.geometry('400x300')

boton_uno = Button(ventana, text='Minimizar', command=ventana.iconify, bg='#237566')
boton_uno.pack(ipadx=10, ipady=10, expand=True, fill='both')

def imprimir():
    etiqueta_uno = Label(ventana, text='Imprimiendo...')
    etiqueta_uno.pack(side='right')

boton_dos = Button(ventana, text='Imprimir', command=imprimir, bg='blue')
boton_dos.pack(side='left', ipadx=10, ipady=10)

ventana.mainloop()
