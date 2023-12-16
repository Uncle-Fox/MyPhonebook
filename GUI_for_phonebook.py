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

terminal_text_Output = Text(root, wrap=WORD, height=30, width=80, font=('Courier New', 12))
terminal_text_Output.place(x= 400, y=50)

terminal_text_Input = Text(root, wrap=WORD, height=5, width=55, font=('Courier New', 12))
terminal_text_Input.place(x= 650, y=655)

terminal_text_Input_Info = Text(root, wrap=WORD, height=5, width=20, font=('Courier New', 12))
terminal_text_Input_Info.place(x= 400, y=655)

def Input_data():
    input_data = terminal_text_Input.get("1.0", END)
    btn6.config(command=lambda: terminal_text_Output.insert(END, f">>> {input_data}"))

def click():
    x = "Hello!"
    terminal_text_Output.insert(END, f">>> {x}\n")

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

input_data = terminal_text_Input.get("1.0", END)

btn6 = Button(root,
            text = 'Help',
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn6.place(x = 60, y = 430)

btn7 = Button(root,
            text = 'Ввод данных',
            command = Input_data,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn7.place(x = 760, y = 760)

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

root.mainloop()