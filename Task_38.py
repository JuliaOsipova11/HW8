# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных

def add_contact(f):
    input_name = input('Введите Имя: ')
    input_last_name = input('Введите Фамилию: ')
    input_phone = input('Введите номер телефона: ')
    data = f'{input_last_name}; {input_name}; {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Запись {data} добавлена')


def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list

def print_all(f):
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)


def search_contact(f):
    last_name = input('Введите фамилию для поиска: ')
    adr_book = read_all(f)
    print(len(adr_book))
    for i in range(len(adr_book)):
        print(i, adr_book[i])
    idx = int(input('Введи индекс для замены: '))
    last_name, name, _ = adr_book[idx].split('; ')
    phone = input('новый номер: ')
    new_record = f'{last_name}; {name}; {phone}'
    adr_book[idx] = new_record
    with open(f, 'w', encoding='utf-8') as fd:
        fd.writelines(adr_book)
    # for line in adr_book:
    #     if last_name in line:
    #         print(line)


def main():
    # user_choice = ''
    # while user_choice != 'z':
    file = 'address_book.txt'
    while True:
        user_choice = input('1 - добавить запись,\n2 - прочитать всю тел.книгу,\n'
                            '3 - найти запись,\nz - для выхода: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == 'z':
            print('Всего хорошего')
            break


def change_phone_number(f):
    adr_book = read_all(f)
    number_to_change = search_contact(adr_book)
    adr_book.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    user_choice = input('1 - Фамилия,\n2 - Имя,\n3 - Номер телефона,\nz - для выхода:')
    if user_choice == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif user_choice == '2':
        number_to_change[1] = input('Введите имя: ')
    elif user_choice == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    elif user_choice == 'z':
        print('Всего хорошего')
    adr_book.append(number_to_change)
    with open(f, 'w', encoding='utf-8') as file:
        for contact in adr_book:
            line = ' '.join(contact) + '\n'
            print(line)


def delete_contact(f):
    adr_book = read_all(f)
    number_to_change = search_contact(adr_book)
    adr_book.remove(number_to_change)
    with open(f, 'w', encoding='utf-8') as file:
        for contact in adr_book:
            line = ' '.join(contact) + '\n'
            print(line)


if __name__ == '__main__':
    main()
