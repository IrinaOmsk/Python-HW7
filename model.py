def find_contact(base, name):
    for contact in base:
        if name.lower() == contact[0].lower():
            return contact[1]
    else:
        return 'не найден'

def is_name_in_base(base, new_contact):
    name = new_contact.split(',')[0]
    for contact in base:
        if name.lower() == contact[0].lower():
            return True 
    else:
        return False