#Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле 
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# 1. UI ( user interface) 
# 2. Создать файл
# 3. Читать файл
# 4. Вывод данных:
#     1) Считать файл
#     2) Сохранить в перменную
#     3) Вывести на экран
# 5. Запись контакта:
#     1) Запросить данные
#     2) Сохранить в переменную
#     3) Записать в файл
# 6. Поиск контакта:
#     1) Запросить данные поиска
#     2) Сохранить в пременную
#     3) Считать файл и сохранить в переменную
#     4) Произвести поиск
# 7. Внесение изменений:
#     1) Запросить данные, что менять
#     2) Сохранить в переменную
#     3) Запросить, что внести взамен 
#     4) Заменить
#     5) Записать в файл
# 8. Удаление:
#     1) Запросить данные, что удалить
#     2) Сохранить в переменную
#     3) Удалить из файла
#     4) Перезаписать новый файл 
      
      
def name_data():
    return input('Введите имя: ')
    
def surname_data():
    return input('Введите фамилию: ')
    
def patronymic_data():
    return input('Введите отчество: ')
     
def phone_number_data():
    return input('Введите номер: ')
    
def adress_data():
    return input('Введите адрес: ')

def input_contact():
    name = name_data()
    surname = surname_data()
    patronymic = patronymic_data()
    phone_number = phone_number_data()
    adress = adress_data()
    return f'{name} {patronymic} {surname}\n{phone_number}\n{adress}'

def add_contact():
    contact = input_contact()
    with open('Phonebook.txt', 'a', encoding ='utf-8') as data:
        data.write(contact + '\n\n')
        
def read_file():
    with open('Phonebook.txt', 'r', encoding ='utf-8') as data:
        return data.read()
    
def print_contacts():
    data = read_file()
    print()
    print(data)
    print()
    
def search_contact():
    print('Варианты поиска: \n'
            '1. По имени \n'
            '2. По отчеству \n'
            '3. По фамилии \n'
            '4. По номеру телефона \n'
            '5. По адрусу')
    choice = input('Выберите вариант поиска: ')
    i_choice = int(choice) - 1
    search = input('Введите данные для поиска: ')
    data_str = read_file().rstrip()
    if search not in data_str:
        print('Нет такого контакта')
    else:
        #print([data_str])
        data_lst = data_str.split('\n\n')
        #print(data_lst)
        for contact_str in data_lst:
            contact_lst = contact_str.replace('\n', ' ').split() #заменили \n на пробелы и разделили по пробелам
            if search in contact_lst[i_choice]:
               #print(contact_lst)
               print()
               #print(contact_str)
               return contact_str

def change_contact():
    contact_for_change_str = search_contact()
    print(contact_for_change_str)
    data_str = read_file()
    if contact_for_change_str not in data_str:
        print('Нет такого контакта')
    else:
        print('Введите новый контакт')
        new_contact_str = input_contact()
        data_str = data_str.replace(contact_for_change_str, new_contact_str)
        with open('Phonebook.txt', 'w', encoding ='utf-8') as data:
            data.write(data_str)

def dell_contact():
    contact_for_change_str = search_contact()
    print(contact_for_change_str)
    data_str = read_file()
    if contact_for_change_str not in data_str:
        print('Нет такого контакта')
    else:
        data_str = data_str.replace(contact_for_change_str + '\n\n', '')
        with open('Phonebook.txt', 'w', encoding ='utf-8') as data:
            data.write(data_str)
        print('Контакт удалён')                  

def user_interface():
    with open('Phonebook.txt', 'a', encoding ='utf-8'): # создали файл, если его нет
        pass
    cmd = None
    while cmd != '6':
        print('Меню: \n'
            '1. Запись контакта \n'
            '2. Вывести данные на экран \n'
            '3. Поиск контакта \n'
            '4. Изменить контакт \n'
            '5. Удалить контакт \n'
            '6. Выход')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        match cmd:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                change_contact()
            case '5':
                dell_contact()
            case '6':
                print('До свидания')
user_interface()