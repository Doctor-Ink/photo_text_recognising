
from tkinter import *

# http://kabinet-vplaksina.narod.ru/olderfiles/5/Modul_tkinter.pdf

root = Tk()

# # Frame (рамка)
#
# fra1 = Frame(root, width=500, height=100, bg="darkred")
# fra2 = Frame(root, width=300, height=200, bg="green", bd=20)
# fra3 = Frame(root, width=500, height=150, bg="darkblue")
#
# fra1.pack()
# fra2.pack()
# fra3.pack()
#
# ent1 = Entry(fra2, width=20,)
# ent1.pack()

# Scale (шкала)
#
# sca1 = Scale(fra3, orient=HORIZONTAL, length=300,
#              from_=0,to=100, tickinterval=10, resolution=5)
# sca2 = Scale(root, orient=VERTICAL, length=400,
#              from_=1, to=2, tickinterval=0.1, resolution=0.1)
#
# sca1.pack()
# sca2.pack()


# добавления функциональности GUI.

# def output(event):
#     s = ent.get()
#     if s == "1":
#         tex.delete(1.0, END)
#         tex.insert(END, "Обслуживание клиентов на втором этаже")
#     elif s == "2":
#         tex.delete(1.0, END)
#         tex.insert(END, "Пластиковые карты выдают в соседнем здании")
#     else:
#         tex.delete(1.0, END)
#         tex.insert(END, "Введите 1 или 2 в поле слева")
#
# ent = Entry(root, width=1)
# but = Button(root, text="Вывести")
# tex = Text(root, width=20, height=3, font="12", wrap=WORD)
#
# ent.grid(row=0, column=0, padx=60)
# but.grid(row=0, column=1)
# tex.grid(row=0, column=2, padx=20, pady=10)
#
# but.bind("<Button-1>", output)

# # example № 2
#
# li = ["red", "green"]
# def color(event):
#     fra.configure(bg=li[0])
#     li[0], li[1] = li[1], li[0]
# def outgo(event):
#     root.destroy()
# fra = Frame(root, width=100, height=100)
# but = Button(root, text="Выход")
# fra.pack()
# but.pack()
# root.bind("<Return>", color)
# but.bind("<Button-1>", outgo)




# события, производимые мышью
#
# def b1(event):
#     root.title("Левая кнопка мыши")
# def b3(event):
#     root.title("Правая кнопка мыши")
# def move(event):
#     root.title("Движение мышью")
# root.minsize(width=500, height=400)
# root.bind('<Button-1>', b1)
# root.bind('<Button-3>', b3)
# root.bind('<Motion>', move)


# События, производимые с помощью клавиатуры

# def exit_(event):
#     root.destroy()
# def caption(event):
#     t = ent.get()
#     lbl.configure(text=t)
# ent = Entry(root, width=40)
# lbl = Label(root, width=80)
# ent.pack()
# lbl.pack()
# ent.bind('<Return>', caption)
# root.bind('<Control-z>', exit_)

# специальные классы Tkinter
#
# var=IntVar()
# var.set(1)
# rad0 = Radiobutton(root, text="Первая", variable=var, value=0)
# rad1 = Radiobutton(root, text="Вторая", variable=var, value=1)
# rad2 = Radiobutton(root, text="Третья", variable=var, value=2)
# rad0.pack()
# rad1.pack()
# rad2.pack()
# def display(event):
#     v = var.get()
#     if v == 0:
#         print ("Включена первая кнопка")
#     elif v == 1:
#         print ("Включена вторая кнопка")
#     elif v == 2:
#         print ("Включена третья кнопка")
# but = Button(root, text="Получить значение")
# but.pack()
# but.bind('<Button-1>', display)

# # example 2 with flags
#
# var0=StringVar() # значение каждого флажка ...
# var1=StringVar() # ... хранится в собственной переменной
# var2=StringVar()
# # если флажок установлен, то в ассоциированную переменную ...
# # ...(var0,var1 или var2) заносится значение onvalue, ...
# # ...если флажок снят, то - offvalue.
# ch0 = Checkbutton(root, text="Окружность", variable=var0,
#                   onvalue="circle", offvalue="")
# ch1 = Checkbutton(root, text="Квадрат", variable=var1,
#                   onvalue="square", offvalue="")
# ch2 = Checkbutton(root, text="Треугольник", variable=var2,
#                   onvalue="triangle", offvalue="")
# lis = Listbox(root, height=3)
# def result(event):
#     v0 = var0.get()
#     v1 = var1.get()
#     v2 = var2.get()
#     l = [v0,v1,v2] # значения переменных заносятся в список
#     lis.delete(0,2) # предыдущее содержимое удаляется из Listbox
#     for v in l: # содержимое списка l последовательно ...
#         lis.insert(END,v) # ...вставляется в Listbox
# but = Button(root,text="Получить значения")
# but.bind('<Button-1>',result)
# ch0.deselect()# "по умолчанию" флажки сняты
# ch1.deselect()
# ch2.deselect()
# ch0.pack()
# ch1.pack()
# ch2.pack()
# but.pack()
# lis.pack()


# example 3 option textvariable
#
# v = StringVar()
# ent1 = Entry(root, textvariable=v, bg="black",fg="white")
# ent2 = Entry(root, textvariable=v)
# ent1.pack()
# ent2.pack()


# objects MENU
#
# m = Menu(root) #создается объект Меню на главном окне
# root.config(menu=m) #окно конфигурируется с указанием меню для него
# fm = Menu(m) #создается пункт меню с размещением на основном меню (m)
# m.add_cascade(label="File", menu=fm) #пункту располагается на основном меню (m)
# fm.add_command(label="Open...") #формируется список команд пункта меню
# fm.add_command(label="New")
# fm.add_command(label="Save...")
# fm.add_command(label="Exit")
# hm = Menu(m) #второй пункт меню
# m.add_cascade(label="Help",menu=hm)
# hm.add_command(label="Help")
# hm.add_command(label="About")
# nfm = Menu(fm)
# fm.add_cascade(label="Import",menu=nfm)
# nfm.add_command(label="Image")
# nfm.add_command(label="Text")
#
# # Привязка функций к меню
#
# def new_win():
#     win = Toplevel(root)
# def close_win():
#     root.destroy()
# def about():
#     win = Toplevel(root)
#     lab = Label(win,text="Это просто программа-тест \n меню в Tkinter")
#     lab.pack()
# fm.add_command(label="New",command=new_win)
# fm.add_command(label="Exit",command=close_win)
# hm.add_command(label="About",command=about)


# диалоговые окна

from tkinter.filedialog import *
# op = askopenfilename()
# sa = asksaveasfilename()

# txt = Text(root, width=40, height=15, font="12")
# txt.pack()
# op = askopenfilename()
# txt.insert(END,op)
# import fileinput
# for i in fileinput.input(op):
#     txt.insert(END,i)


# # увязываем на пункт меню
#
# from tkinter.filedialog import *
# import fileinput
# def _open():
#     op = askopenfilename()
#     for l in fileinput.input(op):
#         txt.insert(END,l)
# m = Menu(root)
# root.config(menu=m)
# fm = Menu(m)
# m.add_cascade(label="File",menu=fm)
# fm.add_command(label="Open...",command=_open)
# txt = Text(root,width=40,height=15,font="12")
# txt.pack()
#
# # Теперь попробуем сохранять текст
#
# def _save():
#     sa = asksaveasfilename()
#     letter = txt.get(1.0,END)
#     f = open(sa,"w")
#     f.write(letter)
#     f.close()
# fm.add_command(label="Save",command=_save)
#
# from tkinter.messagebox import *
# def close_win():
#     if askyesno("Exit", "Do you want to quit?"):
#         root.destroy()
# def about():
#     showinfo("Editor", "This is text editor.\n(test version)")
# fm.add_command(label="Exit", command=close_win)
# hm = Menu(m)
# m.add_cascade(label="Help", menu=hm)
# hm.add_command(label="About", command=about)



# # объект-холст
#
# canv = Canvas(root, width=500, height=500, bg="lightblue",
#               cursor="pencil")
# canv.create_line(200, 50, 300, 50, width=3, fill="blue")
# canv.create_line(0, 0, 100, 100, width=2, arrow=LAST)
# x = 75
# y = 110
# canv.create_rectangle(x, y, x+80, y+50, fill="white", outline="blue")
# canv.create_polygon([200,100],[200,150],[300,150],[300,100],fill="yellow")
# canv.create_polygon([250,100],[200,150],[300,150],fill="yellow")
# canv.create_polygon([300,80],[400,80],[450,75],[450,200],
#                     [300,180],[330,160],outline="white",smooth=1)
#
#
# canv.pack()


# дзэн питона
#текстовое поле и его первоначальные настройки
# tx = Text(font=('times',12), width=50, height=15, wrap=WORD)
# tx.pack(expand=YES,fill=BOTH)
#
# tx.insert(1.0, 'Дзэн Питона\n\
# Если интерпретатору Питона дать команду\n\
# import this ("импортировать это"),\n\
# то выведется так называемый "Дзен Питона".\n Некоторые выражения:\n\
# * Если реализацию сложно объяснить — это плохая идея.\n\
# * Ошибки никогда не должны замалчиваться.\n\
# * Явное лучше неявного.\n\n')
#
# #установка тегов для областей текста
# tx.tag_add('title', '1.0', '1.end')
# tx.tag_add('special', '6.0', '8.end')
# tx.tag_add('special', '3.0', '3.11')
# #конфигурирование тегов
# tx.tag_config('title',foreground='red',
#               font=('times',14,'underline'),justify=CENTER)
# tx.tag_config('special',background='grey85',font=('Dejavu',10,'bold'))
#
# def erase():
#     tx.delete('1.0',END)
#
# #добавление кнопки
# bt = Button(tx, text='Стереть', command=erase)
# tx.window_create(END, window=bt)
# def smiley(event):
#     cv = Canvas(height=30,width=30)
#     cv.create_oval(1,1,29,29,fill="yellow")
#     cv.create_oval(9,10,12,12)
#     cv.create_oval(19,10,22,12)
#     cv.create_polygon(9,20,15,24,22,20)
#     tx.window_create(CURRENT,window=cv)
#
# #ЛКМ -> смайлик
# tx.bind('<Button-1>',smiley)
#
# root.mainloop()


a = 4
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
elif 2 <= a <= 10:
    print('Mid-2')
else:
    print('High')