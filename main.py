import difflib
import os


from * import Contacts
from * import Notes


def clear():
    return os.system('clear')


class Bot:
    bot_working = True
    save_path = 'saves/'
    book = Contacts.Address_book()
    notes = Notes.Note_book()

    def help(self):
        clear()
        res = ''
        for key, value in self.commands.items():
            res += f"{key} - "
            res += f"{value[1]}\n"
        return "Список доступних функцій:\n" + res

    def func_exit(self):
        clear()
        self.bot_working = False
        # book.save_to_file(save_path)
        return "До зустрічі! Бот завершує роботу!"

    def func_hello(self):
        clear()

        return f'Привіт! Як я можу вам допомогти?\n {self.help()}'

    def func_add(self):
        clear()
        user_input = input('Що ви хочете додати? (Contact, Note): ')
        if user_input.lower() == 'contact':
            book.load_from_file(type(self).save_path)
            name = book.Name()
            address = book.Address()
            phones = book.Phones()
            email = book.Email()
            birthday = book.Birthday()
            record = book(name, address, phones, email, birthday)
            book.addRecord(record)
            book.save_to_file(type(self).save_path)

        elif user_input.lower() == 'note':
            notes.load_from_file(type(self).save_path)
            tags = notes.Tags()
            content = notes.Content()
            edit_date = notes.Edit_date()
            record = notes.Record(tags, content, edit_date)
            notes.addRecord(record)
            notes.save_to_file(type(self).save_path)

        return record

    def func_edit(self):
        clear()
        user_input = input('Що ви хочете додати? (Contact, Note): ')
        if user_input.lower() == 'contact':
            book.load_from_file(type(self).save_path)
            ...
            book.save_to_file(type(self).save_path)

        elif user_input.lower() == 'note':
            notes.load_from_file(type(self).save_path)
            ...
            notes.save_to_file(type(self).save_path)

        return record

    def func_show_all(self):
        clear()
        user_input = input('Що ви хочете вивести на екран? (Contact, Note): ')
        if user_input.lower() == 'contact':
            book.load_from_file(type(self).save_path)
            return book
        elif user_input.lower() == 'note':
            notes.load_from_file(type(self).save_path)
            return notes

    commands = {
        "hello": [func_hello, 'Функція привітання з користувачем, та довідка по командам.'],
        "add": [func_add, 'Функція додавання контакту, або нотатки.'],
        "edit": [func_edit, 'Функція редагування записів.'],
        "show all": [func_show_all, 'Виведення на екран списку всіх контактів.'],
        "good bye": [func_exit, 'Завершення роботи.'],
        "close": [func_exit, 'Завершення роботи.'],
        "exit": [func_exit, 'Завершення роботи.'],

    }

    def command_parser(self, input_string):
        if input_string.lower() in self.commands:
            print(f"Виконую команду: {input_string}")
            return self.commands[input_string][0](self)

        suggestion = difflib.get_close_matches(input_string, self.commands, cutoff=0.55)
        if suggestion:
            return f"Невідома команда. Можливо, ви мали на увазі: {', '.join(suggestion)}."
        else:
            return "Невідома команда."

    def main(self):
        while type(self).bot_working:
            user_input = input("Введіть команду: ")
            print(self.command_parser(user_input))



if __name__ == '__main__':
    my_bot = Bot()
    my_bot.main()




'''
Приклад реалізації створення екземплярів классу для контактів у Address_book.


class Name():
    def __init(self):
        self.values = input("Введіть імʼя:  ")
            
            
class Phones():
    def __init__(self):
        while True:
            self.value = []
            self.values = input("Введіть номер телефону в форматі ........................ ")
            try:
                for number in self.values.split(' '):
                    if 'тут якась перевірка':
                        self.value.append(number)
                    else:
                        raise ValueError
            except ValueError:
                print('Неправильний формат телефонного номеру. Введіть номер ще раз.')
            else:
                break
'''