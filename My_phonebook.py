import json

#Надо добавить сортировку книги(?), а то сейчас выводит как они были записаны

def save():
    with open("phoneNumber.json", "w", encoding="utf-8") as doc:
        doc.write(json.dumps(phonebook, ensure_ascii=False)) #заменить тест бук
    print("")

def load():
    try:
        with open("phoneNumber.json", "r", encoding="utf-8") as doc:
            telephone = json.load(doc)
        print("")
        return telephone
    except FileNotFoundError:
        return {}

def Show_all():
    print("Текущий телефонный список")
    with open("phoneNumber.json", "r", encoding="utf-8") as doc:
        phonebook_data = json.load(doc)
        for name, data in phonebook_data.items():
            print(f"№ {data.get('id', 'N/A')}. {name}: телефон {', '.join(map(str, data['phones']))}; дата рождения: {data.get('birthday', 'N/A')}; email: {data.get('email', 'N/A')}")

def add():
    global id_counter
    global phonebook
    name = input("Введите имя: ")
    birthday = input("Введите дату рождения: ")
    email = input("Введите EMAIL: ")
    phone = input("Введите номера телефонов через пробел: ").split()

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

    phone_str = ', '.join(phone)
    print(f'Вы добавили нового абонента: \n'
        f'ID: {entry_id}\n'
        f'Имя: {name}\n'
        f'День рождения: {birthday}\n'
        f'Email: {email}\n'
        f'Телефон: {phone_str}\n')
    

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
    Show_all()
    num = int(input("Выберите id абонента, которого хотите удалить из книги: "))
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


phonebook = load()
id_counter = len(phonebook)+1

info = ('Вам доступны следующие команды: \n'
    'save - сохраняет ваши изменения в файл\n'
    'load - загружает справочник из файла\n'
    'all - показывает весь справочник\n'
    'info - показывает информацию по командам\n'
    'delete - удаляет абонента с выбранным именем\n'
    'change - меняет данные у выбранного абонента\n'
    'exit - выход из программы')


while True:
    command = input("Введите одну из команд: exit, info, load, save, all, add, delete, change\n")

    if command == "exit": break

    elif command == "info": print(info)

    elif command == "load": phonebook = load()

    elif command == "save": save(), print("Изменения сохранены") #Мб стоит убрать save из набора команд?

    elif command == "all": Show_all()

    elif command == "add": add(), save()

    elif command == "delete": delete(), save()

    elif command == "change": change()

    else:
        print('Вы ввели неверную команду! Для списка команд обратитесь к "info"!')