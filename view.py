def choose_mode():
    print('Телефонный справочник:')
    print('1. Поиск номера телефона в базе')
    print('2. Добавление в базу нового контакта')
    return input('Введите пункт из меню (1 или 2): ')


def get_name():
    return input('Введите имя контакта для поиска: ')


def get_new_contact():
    name = input('Ввведите имя контакта: ')
    phone_number = input('Введите номер телефона контакта: ')
    return f'{name},{phone_number}'


def show_number(number):
    print(f'Телефон контакта: {number}')


def show_write_success():
    print('Новый контакт записан успешно')


def show_write_failure():
    print('Контакт с таким именем уже существует')


def show_error():
    print('Некорректный ввод')
    