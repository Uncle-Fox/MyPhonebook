from tkinter import *
import json

root = Tk()
root.title('Phonebook')
root.geometry('1240x840')
root.resizable(width = False, height = False)

bg = PhotoImage(file= "Bg.png")
labelBg = Label(root, image= bg)
labelBg.place(x = 0, y = 0)

terminal_text_Output = Text(root, wrap=WORD, height=30, width=80, font=('Courier New', 12))
terminal_text_Output.place(x= 400, y=50)

terminal_text_Input_Name = Entry(font=('Courier New', 12))
terminal_text_Input_Name.place(x= 650, y=655)

terminal_text_Input_birthday = Entry(font=('Courier New', 12))
terminal_text_Input_birthday.place(x= 650, y=680)

terminal_text_Input_Email = Entry(font=('Courier New', 12))
terminal_text_Input_Email.place(x= 650, y=705)

terminal_text_Input_Phone = Entry(font=('Courier New', 12))
terminal_text_Input_Phone.place(x= 650, y=730)

terminal_text_Input_id = Entry(font=('Courier New', 12))
terminal_text_Input_id.place(x= 650, y=785)

def save(phonebook):
    with open("phoneNumber.json", "w", encoding="utf-8") as doc:
        doc.write(json.dumps(phonebook, ensure_ascii=False))

def load():
    try:
        with open("phoneNumber.json", "r", encoding="utf-8") as doc:
            telephone = json.load(doc)
        return telephone
    except FileNotFoundError:
        return {}

def Show_all():
    terminal_text_Output.delete(1.0, END)
    terminal_text_Output.insert(END, "Текущий телефонный справочник\n")
    with open("phoneNumber.json", "r", encoding="utf-8") as doc:
        phonebook_data = json.load(doc)
        sorted_phonebook_data = sorted(phonebook_data.items(), key=lambda item: item[1]["id"])
        
        for name, data in sorted_phonebook_data:
            terminal_text_Output.insert(END, f"№ {data.get('id', 'N/A')}. {name}: телефон {', '.join(map(str, data['phones']))}; дата рождения: {data.get('birthday', 'N/A')}; email: {data.get('email', 'N/A')}\n")

def clear_input_fields():
    terminal_text_Input_Name.delete(0, END)
    terminal_text_Input_birthday.delete(0, END)
    terminal_text_Input_Email.delete(0, END)
    terminal_text_Input_Phone.delete(0, END)

def add():
    name = terminal_text_Input_Name.get()
    birthday = terminal_text_Input_birthday.get()
    email = terminal_text_Input_Email.get()
    phone =  terminal_text_Input_Phone.get().split()

    phonebook = load()
    id_counter = len(phonebook)+1

    for key, value in phonebook.items():
        if 'id' in value and value['id'] == id_counter:
            entry_id = id_counter + 1
        else: entry_id = id_counter

    if name in phonebook:
            phonebook[name]['phones'].extend(phone)
            phonebook[name]['birthday'] = birthday
            phonebook[name]['email'] = email
    else:
        phonebook[name] = {'id': entry_id, 'phones': phone, 'birthday': birthday, 'email': email}

    save(phonebook)
    Show_all()

def change():
    phonebook = load()
    Show_all()
    id_to_change = int(terminal_text_Input_id.get())

    name = terminal_text_Input_Name.get()
    birthday = terminal_text_Input_birthday.get()
    email = terminal_text_Input_Email.get()
    phone =  terminal_text_Input_Phone.get().split()

    key_to_change = None
    for key, value in phonebook.items():
        if 'id' in value and value['id'] == id_to_change:
            key_to_change = key
            break

    if key_to_change is not None:
        phonebook[key_to_change]['phones'] = phone
        phonebook[key_to_change]['birthday'] = birthday
        phonebook[key_to_change]['email'] = email
    else:
        terminal_text_Output.delete(1.0, END)
        terminal_text_Output.insert(END, "Абонент не найден.")

    save(phonebook)
    Show_all()

""" def find_key(num): #Надо использовать эту функцию в delete и в change
    global phonebook
    key_to_delete = None
    for key, value in phonebook.items():
        if 'id' in value and value['id'] == num:
            key_to_delete = key
            return key_to_delete
    if key_to_delete == None: print(f"Абонент с ID {num} не найден") """

def delete(): #сначала будет осуществлен вариант удаления только через id
    phonebook = load()
    info_to_delete = terminal_text_Input_id.get()

    key_to_delete = None
    for key, value in phonebook.items():
        if 'id' in value and value['id'] == int(info_to_delete):
            key_to_delete = key
            break

    if key_to_delete is not None:
        del phonebook[key_to_delete]
        save(phonebook)
        Show_all()
    else:
        terminal_text_Output.delete(1.0, END)
        terminal_text_Output.insert(END, "Абонент не найден.")

def get_info():
    terminal_text_Output.delete(1.0, END)
    terminal_text_Output.insert(END, 'Вам доступны следующие кнопки: \n'
                                    'Открыть контакты - показывает весь справочник\n\n'
                                    'Добавить контакт - добавляет нового абонента в справочник. Для этого:\n'
                                    'Введите внизу программы все необходимые данные и нажмите кнопку "Ввести данные"\n\n'
                                    'Удалить контакт - удаляет абонента с выбранным id\n\n'
                                    'Изменить контакт - меняет данные абонента с выбранным id. Предварительно введите данные\n\n'
                                    'Help - показывает информацию по командам\n\n'
                                    'Ввод данных - сохраняет в программу ваши введенные данные\n\n'
                                    'Выход - выход из программы')

def exit_program():
    root.destroy()

btn_open_book = Button(root,
            text = 'Открыть контакты',
            command = Show_all,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown',
            width = 17
            )
btn_open_book.place(x = 60, y = 55)

btn_change_data = Button(root,
            text = 'Изменить данные',
            command = change,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown',
            width = 17
            )
btn_change_data.place(x = 900, y = 685)

btn_help = Button(root,
            text = 'Help',
            command= get_info,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn_help.place(x = 60, y = 430)

btn_input_data = Button(root,
            text = 'Ввести данные',
            command = add,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown',
            width = 17
            )
btn_input_data.place(x = 900, y = 615)

btn_delete_abonent = Button(root,
            text = 'Удалить абонента',
            command = delete,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown',
            width = 17
            )
btn_delete_abonent.place(x = 900, y = 755)

btn_exit = Button(root,
            text = 'Выход',
            command = exit_program,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn_exit.place(x = 60, y = 730)

label_main = Label(root,
            text = 'PhoneBook',
            font = ('Comic Sans MS', 20),
            bg = '#FAF5D5',
            fg = 'brown'
            ).pack()

label_input_data = Label(root,
            text = 'Ввод данных',
            font = ('Comic Sans MS', 20),
            bg = '#FAF5D5',
            fg = 'brown'
            )
label_input_data.place(x = 660, y = 599)

label_name = Label(root,
            text = 'Введите Имя абонента',
            font = ('Comic Sans MS', 13),
            bg = '#FAF5D5',
            fg = '#000000'
            )
label_name.place(x = 445, y = 650)

label_birthday = Label(root,
            text = 'Введите день рождения',
            font = ('Comic Sans MS', 13),
            bg = '#FAF5D5',
            fg = '#000000'
            )
label_birthday.place(x = 445, y = 675)

label_Email = Label(root,
            text = 'Введите Email абонента',
            font = ('Comic Sans MS', 13),
            bg = '#FAF5D5',
            fg = '#000000'
            )
label_Email.place(x = 445, y = 700)

label_Phone = Label(root,
            text = 'Введите телефон',
            font = ('Comic Sans MS', 13),
            bg = '#FAF5D5',
            fg = '#000000'
            )
label_Phone.place(x = 445, y = 725)

label_id = Label(root,
            text = 'Введите id абонента\n для его изменения/удаления',
            font = ('Comic Sans MS', 13),
            bg = '#FAF5D5',
            fg = '#000000'
            )
label_id.place(x = 390, y = 770)

root.mainloop()

phonebook = load()
id_counter = len(phonebook)+1