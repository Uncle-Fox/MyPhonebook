# урок взят с https://www.youtube.com/watch?v=2Z8qRJ7Lqag&list=PL9aGGxgLOVw5oEXMk8Qhg3RVWY2dtyw8H

from tkinter import *

root = Tk()
root.title('Phonebook')
root.geometry('1240x840')
root.resizable(width = False, height = False)

#root.config(bg = 'Yellow') - создание фона
bg = PhotoImage(file= "Bg.png")
labelBg = Label(root, image= bg)
labelBg.place(x = 0, y = 0)

def click():
    x = "Hello!"
    terminal_text_Output.insert(END, f">>> {x}\n")

def test():
    terminal_text_Output.insert(END, f"END\n")
# btn = Button(root,
#             text = 'Кнопка №1',
#             command = click,
#             font = ('Comic Sans MS', 20),
#             bg = 'white',
#             activebackground = 'green',
#             activeforeground = 'white',
#             fg = 'brown'
#             # width = 10,
#            height = 10)


btn = Button(root,
            text = 'Открыть контакты',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown',
            width = 17
            #height = 1
            )
btn.place(x = 60, y = 55)

btn2 = Button(root,
            text = 'Добавить контакт',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown',
            width = 17
            )
btn2.place(x = 60, y = 130)

btn3 = Button(root,
            text = 'Удалить контакт',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown',
            width = 17
            )
btn3.place(x = 60, y = 205)

btn4 = Button(root,
            text = 'Изменить контакт',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown',
            width = 17
            )
btn4.place(x = 60, y = 280)

btn5 = Button(root,
            text = 'Загрузка справочника',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn5.place(x = 60, y = 355)

btn6 = Button(root,
            text = 'Help',
            command = test,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn6.place(x = 60, y = 430)

btn8 = Button(root,
            text = 'Выход',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn8.place(x = 60, y = 730)


label = Label(root,
            text = 'PhoneBook',
            font = ('Comic Sans MS', 20),
            bg = '#FAF5D5',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            ).pack()

label2 = Label(root,
            text = 'Ввод команд',
            font = ('Comic Sans MS', 20),
            bg = '#FAF5D5',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
label2.place(x = 750, y = 599)


terminal_text_Output = Text(root, wrap=WORD, height=30, width=80, font=('Courier New', 12))
terminal_text_Output.place(x= 400, y=50)

terminal_text_Input = Text(root, wrap=WORD, height=5, width=80, font=('Courier New', 12))
terminal_text_Input.place(x= 400, y=655)

root.mainloop()