from view import input_data, output_data, var_funcs
from data_base import write_data, find_contact, find_contact, change_contact, import_file


def click():
    temp = var_funcs()
    if temp == 1:
        output_data(find_contact())
    elif temp == 2:
        write_data(input_data())
    elif temp == 3:
        change_contact()
    elif temp == 4:
        import_file()