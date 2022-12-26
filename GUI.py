from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Recognize photo text')
root.iconbitmap(r'C:\Users\Zver\PycharmProjects\my_IMAGES\icons\IAD USE FULL green\IAD USE FULL green Icon pack\renamer.ico')
root.geometry('400x400')


def my_click():
    my_label = Label(root, text='Look! I clicked a Button!')
    my_label.pack()

myButton = ttk.Button(
    root,
    command=my_click,
    text='Start recognising!',
)
myButton.pack(expand=True)

root.mainloop()