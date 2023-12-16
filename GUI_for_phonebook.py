# урок взят с https://www.youtube.com/watch?v=2Z8qRJ7Lqag&list=PL9aGGxgLOVw5oEXMk8Qhg3RVWY2dtyw8H

from tkinter import *

root = Tk()
root.title('Phonebook')
root.geometry('840x840')
root.resizable(width = False, height = False)

#root.config(bg = 'Yellow') - создание фона
bg = PhotoImage(file= "Bg.png")
labelBg = Label(root, image= bg)
labelBg.place(x = 0, y = 0)

def click():
    print("Hello!")


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
            text = 'Кнопка №1',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown',
            width = 10,
            height = 1
            )
btn.place(x = 60, y = 55)

btn2 = Button(root,
            text = 'Кнопка №2',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn2.place(x = 60, y = 130)

btn3 = Button(root,
            text = 'Кнопка №3',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn3.place(x = 60, y = 205)

btn4 = Button(root,
            text = 'Кнопка №4',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn4.place(x = 60, y = 280)

btn5 = Button(root,
            text = 'Кнопка №5',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn5.place(x = 60, y = 355)

btn6 = Button(root,
            text = 'Кнопка №6',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn6.place(x = 60, y = 430)

btn7 = Button(root,
            text = 'Кнопка №7',
            command = click,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn7.place(x = 60, y = 505)

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


root.mainloop()