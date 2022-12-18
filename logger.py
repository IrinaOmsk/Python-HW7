def get_data():
    with open('phone_base.csv', 'r', encoding='utf-8') as file:
        return [line.strip().split(',') for line in file]


def push_data(contact):
    with open('phone_base.csv', 'a', encoding='utf-8') as file:
        file.write(f'\n{contact}')

