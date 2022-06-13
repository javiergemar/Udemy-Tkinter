from tkinter import *

window = Tk()
window.config(bd=10, bg='goldenrod3')
window.title('Casa de comidas')

def orden():
    lista = '' + (' Con queso' if queso.get() else ' Sin queso')
    lista += ' y con lechuga' if lechuga.get() else ' y sin lechuga'
    '''
    Si queso.get() es True (es decir, que está marcado) entonces se agrega la palabra ' Con queso',
    si no, se agrega la palabra ' Sin queso'.
    '''
    imprimirPedido.config(text=lista)

# Creamos las variables que se usarán para almacenar el valor de los checkbutton.
queso = IntVar()
lechuga = IntVar()

imagen = PhotoImage(file='clase_08_hamburguesa.gif')

etiquetaImagen = Label(window, image=imagen)
etiquetaImagen.pack(side='left')

# Creamos un frame dentro de la ventana principal.
frame = Frame(window)
frame.pack(side='right')
frame.config(bg='goldenrod3')

'''
Los siguientes elementos los vamos a alojar en el frame, que nos permite ordenar los elementos en subventanas
dentro de la ventana principal.
'''
etiquetaPedido = Label(frame, text='¿Cómo quieres tu hamburguesa?', bg='goldenrod3', font='Courier 15')
etiquetaPedido.pack(anchor='w')

conQueso = Checkbutton(frame, text='Con queso', variable=queso, onvalue=1, offvalue=0, bg='goldenrod3',
                       font='Courier 10', command=orden)
conQueso.pack(anchor='w')
'''
El onvalue es cuando el usuario selecciona y el valor del checkbutton es 1, el offvalue es cuando el usuario no 
selecciona y el valor del checkbutton es 0.
'''

conLechuga = Checkbutton(frame, text='Con lechuga', variable=lechuga, onvalue=1, offvalue=0, bg='goldenrod3',
                         font='Courier 10', command=orden)
conLechuga.pack(anchor='w')

imprimirPedido = Label(frame, bg='goldenrod3')
imprimirPedido.config(text='El pedido aparecerá aquí', font='Courier 12')
imprimirPedido.pack(anchor='w')

window.mainloop()