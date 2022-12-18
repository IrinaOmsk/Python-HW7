import model
import view
import logger


def run():
    mode = view.choose_mode()
    if mode == '1':
        name = view.get_name()
        base = logger.get_data()
        number = model.find_contact(base, name)
        view.show_number(number)
    if mode == '2':
        contact = view.get_new_contact()
        base = logger.get_data()
        if model.is_name_in_base(base, contact):
            view.show_write_failure()
        else:
            logger.push_data(contact)
            view.show_write_success()
    else:
        view.show_error()
  