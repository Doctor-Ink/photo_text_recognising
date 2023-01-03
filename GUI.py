from tkinter import *
from tkinter.ttk import Progressbar
from config import *
from main import Recognising


def main():
    ''' Graphic user interface'''
    root = Tk()
    root.title('Recognize photo text')
    root.iconbitmap(
        r'C:\Users\Zver\PycharmProjects\my_IMAGES\icons\IAD USE FULL green\IAD USE FULL green Icon pack\renamer.ico')
    root.geometry('400x400')

    def my_click():
        recognise.recognise_photo()
        if var_spaces.get() == '1':
            print('Delete extra spaces')
            recognise.extra_spaces()
        if var_wrap.get() == '1':
            print('remove text wrap')
            recognise.remove_word_wraps()
        if var_paragraph.get() == '1':
            print('Paragraph breaks')
            recognise.paragraph_break()

    Label(root, text='Введите путь к папке с фотографиями текста').pack(anchor=N)

    ent_folder = Entry(root, width=100, bd=3)
    ent_folder.insert(0, r'C:\Users\Zver\PycharmProjects\photo_text_recognising\input_photos')
    ent_folder.pack(anchor=N)
    recognise = Recognising(folder=f'{ent_folder.get()}')

    var_spaces = StringVar()  # значение каждого флажка ...
    var_wrap = StringVar()  # ... хранится в собственной переменной
    var_paragraph = StringVar()
    # если флажок установлен, то в ассоциированную переменную ...
    # ...(var0,var1 или var2) заносится значение onvalue, ...
    # ...если флажок снят, то - offvalue.
    ch0 = Checkbutton(root, text="Удалить лишние пробелы", variable=var_spaces,
                      onvalue='1', offvalue=False)
    ch1 = Checkbutton(root, text="На фото есть перенос слов", variable=var_wrap,
                      onvalue='1', offvalue=False)
    ch2 = Checkbutton(root, text="Разрыв обзаца после знака препинания", variable=var_paragraph,
                      onvalue='1', offvalue=False)

    ch0.deselect()    # "по умолчанию" флажки сняты
    ch1.deselect()
    ch2.select()
    ch0.pack()
    ch1.pack()
    ch2.pack()

    myButton = Button(
        root,
        command=my_click,
        width=14,
        bg='green',
        fg='black',
        text='Start recognising!',
        underline=TRUE,
        font="Arial 18"
    )

    myButton.pack(side=BOTTOM)

    root.mainloop()
    ''' Graphic user interface end!'''


if __name__=='__main__':
    main()
