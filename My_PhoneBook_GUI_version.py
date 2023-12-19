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

terminal_text_Input_Info = Text(root, wrap=WORD, height=5, width=23, font=('Courier New', 12))
terminal_text_Input_Info.place(x= 400, y=655)

terminal_text_Input_Name = Entry(font=('Courier New', 12))
terminal_text_Input_Name.place(x= 650, y=655)

terminal_text_Input_birthday = Entry(font=('Courier New', 12))
terminal_text_Input_birthday.place(x= 650, y=680)

terminal_text_Input_Email = Entry(font=('Courier New', 12))
terminal_text_Input_Email.place(x= 650, y=705)

terminal_text_Input_Phone = Entry(font=('Courier New', 12))
terminal_text_Input_Phone.place(x= 650, y=730)

def Input_data():
    input_data = terminal_text_Input_Name.get()
    btn7.config(command=lambda: terminal_text_Output.insert(END, f">>> {input_data}"))

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
        #sorted_phonebook_data = sorted(phonebook_data.items(), key=lambda item: item[1]["id"]) - нужно добавить сортировку, сейчас идет сбой int - string из-за int 4 в словаре
        for name, data in phonebook_data.items():
            terminal_text_Output.insert(END, f"№ {data.get('id', 'N/A')}. {name}: телефон {', '.join(map(str, data['phones']))}; дата рождения: {data.get('birthday', 'N/A')}; email: {data.get('email', 'N/A')}\n")

def clear_input_fields():
    terminal_text_Input_Name.delete(0, END)
    terminal_text_Input_birthday.delete(0, END)
    terminal_text_Input_Email.delete(0, END)
    terminal_text_Input_Phone.delete(0, END)

def add_info():
    terminal_text_Input_Info.delete(1.0, END)
    terminal_text_Input_Info.insert(END, f'Введите Имя абонента\n'
                                        f'Введите дату рождения\n\n'
                                        f'Введите Email\n'
                                        f'Введите телефон\n')
    

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
    #clear_input_fields

def change():
    global phonebook
    Show_all()
    num = (input("Выберите id абонента, которого хотите изменить в книге: "))
    key_to_change = find_key(num)

    if key_to_change is not None:
        abonent = phonebook[key_to_change]  # Получаем словарь данных абонента

        print(f"Выберите, что хотите изменить для {key_to_change}:")
        for key, value in phonebook.items():
            if 'id' in value and value['id'] == num:
                print(f"№ {value.get('id', 'N/A')}. {key}: телефон {', '.join(map(str, value['phones']))}; дата рождения: {value.get('birthday', 'N/A')}; email: {value.get('email', 'N/A')}")


        value_to_change = input("id - id, phones - phones, birthday - birthday, email - email\n")
        value_to_change_list = ["id", "phones", "birthday", "email", "address"]

        if value_to_change in value_to_change_list:
            changed_value = input(f"Введите новые данные для {value_to_change}: ").split()
            abonent[value_to_change] = changed_value
            print(f"Данные для {key_to_change} обновлены! {value_to_change} теперь {changed_value}\n") 
            save()
            Show_all()
        else:
            print("Вы ошиблись параметром! Попробуйте еще раз")
    else:
        print(f"Абонент с id {num} не найден в книге.")

def find_key(num): #Надо использовать эту функцию в delete и в change
    global phonebook
    key_to_delete = None
    for key, value in phonebook.items():
        if 'id' in value and value['id'] == num:
            key_to_delete = key
            return key_to_delete
    if key_to_delete == None: print(f"Абонент с ID {num} не найден")

def delete():
    global phonebook
    Show_all
    num = (input("Выберите id абонента, которого хотите удалить из книги: "))
    key_to_delete = None
    for key, value in phonebook.items():
        if 'id' in value and value['id'] == num:
            key_to_delete = key
            break
    
    if key_to_delete is not None:
        x = input("Вы точно хотите удалить этого абонента? Введите 'N' для 'Нет' или 'Y' для 'Да': ")
        if x.lower() == 'n':
            pass
        elif x.lower() == 'y':
            del phonebook[key_to_delete]
            print(f"Абонент с id {key_to_delete} удален из книги.")
    else:
        print(f"Абонент с ID {num} не найден")

def get_info():
    terminal_text_Output.delete(1.0, END)
    terminal_text_Output.insert(END, 'Вам доступны следующие кнопки: \n'
                                    'Открыть контакты - показывает весь справочник\n'
                                    'Добавить контакт - добавляет нового абонента в справочник\n'
                                    'Удалить контакт - удаляет абонента с выбранным именем\n'
                                    'Изменить контакт - меняет данные у выбранного абонента\n'
                                    'Загрузка справочника - загружает справочник из файла\n'
                                    'Help - показывает информацию по командам\n'
                                    'Ввод данных - сохраняет в программу ваши введенные данные\n'
                                    'Выход - выход из программы')

def exit_program():
    root.destroy()

btn = Button(root,
            text = 'Открыть контакты',
            command = Show_all,
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
            command = add_info,
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
            command = delete,
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
            command = change,
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
            command = load,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn5.place(x = 60, y = 355)

input_data = terminal_text_Input_Phone.get()
#после ввода данных, нужно удалять все данные из окна:
#text.delete(1.0,END)

btn6 = Button(root,
            text = 'Help',
            command= get_info,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn6.place(x = 60, y = 430)

btn7 = Button(root,
            text = 'Ввести данные',
            command = add,
            font = ('Comic Sans MS', 20),
            bg = 'white',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
btn7.place(x = 900, y = 665)

btn8 = Button(root,
            text = 'Выход',
            command = exit_program,
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
            text = 'Ввод данных',
            font = ('Comic Sans MS', 20),
            bg = '#FAF5D5',
            activebackground = 'green',
            activeforeground = 'white',
            fg = 'brown'
            )
label2.place(x = 665, y = 599)

root.mainloop()

phonebook = load()
id_counter = len(phonebook)+1