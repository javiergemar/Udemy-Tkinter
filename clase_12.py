from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title('Mi bloc de notas')

text = Text(root, height=8)     # height=8 es el número de líneas
text.pack()

text.insert('1.0', 'Esto es un ejemplo de bloc de notas')   # inserta texto en la línea 1 carácter 0

root.mainloop()