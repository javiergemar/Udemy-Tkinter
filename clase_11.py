from tkinter import *

root = Tk()
root.geometry('400x400')

productos = Label(root, text='Productos')
productos.pack()

def agregar_producto():
    listaProductos.insert(END, entrada1.get())

def eliminar_producto():
    listaProductos.delete(entrada1.get())

listaProductos = Listbox(root, width=50)
listaProductos.insert(0, 'Producto 1')
listaProductos.insert(1, 'Producto 2')
listaProductos.insert(2, 'Producto 3')
listaProductos.insert(3, 'Producto 4')
listaProductos.pack()

'''
Para eliminar un producto usamos la siguiente función y entre paréntesis el índice del producto.
En este caso eliminamos 'Producto 1' con índice 0.
'''
listaProductos.delete(0)

entrada1 = Entry(root, bd=10)
entrada1.pack()

boton1 = Button(root, text='Agregar producto', command=agregar_producto)
boton1.pack()

boton2 = Button(root, text='Eliminar producto', command=eliminar_producto)
boton2.pack()

root.mainloop()
