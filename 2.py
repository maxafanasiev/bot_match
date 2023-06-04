from prompt_toolkit import PromptSession


class NoteTaker:
    def __init__(self):
        self.notes = {}
        self.session = PromptSession()

    def add_note(self, parameters):
        if len(parameters) < 2:
            return 'Помилка: Недостатньо параметрів! Введіть заголовок та вміст нотатки.'

        title = parameters[0]
        content = parameters[1:]
        self.notes[title] = ' '.join(content)
        return f'Нотатку з заголовком "{title}" додано.'

    def view_note(self, parameters):
        if len(parameters) != 1:
            return 'Помилка: Недостатньо параметрів! Введіть заголовок нотатки для перегляду.'

        title = parameters[0]
        if title in self.notes:
            return f'Заголовок: {title}\nВміст: {self.notes[title]}'
        else:
            return f'Нотатку з заголовком "{title}" не знайдено.'

    def delete_note(self, parameters):
        if len(parameters) != 1:
            return 'Помилка: Недостатньо параметрів! Введіть заголовок нотатки для видалення.'

        title = parameters[0]
        if title in self.notes:
            del self.notes[title]
            return f'Нотатку з заголовком "{title}" видалено.'
        else:
            return f'Нотатку з заголовком "{title}" не знайдено.'

    def edit_note(self, parameters):
        if len(parameters) != 1:
            return 'Помилка: Недостатньо параметрів! Введіть заголовок нотатки для редагування.'

        title = parameters[0]
        if title in self.notes:
            current_content = self.notes[title]
            new_content = self.session.prompt(f'Редагуйте вміст нотатки з заголовком "{title}": ',
                                              default=current_content)
            if new_content:
                self.notes[title] = new_content
                return f'Нотатку з заголовком "{title}" змінено.'
            else:
                return f'Нотатку з заголовком "{title}" не змінено.'
        else:
            return f'Нотатку з заголовком "{title}" не знайдено.'

    def parse_command(self, command):
        if not command:
            return 'Помилка: Невідома команда!'

        command_parts = command.split()
        action = command_parts[0]
        parameters = command_parts[1:]

        if action == 'add':
            return self.add_note(parameters)
        elif action == 'view':
            return self.view_note(parameters)
        elif action == 'delete':
            return self.delete_note(parameters)
        elif action == 'edit':
            return self.edit_note(parameters)
        else:
            return 'Помилка: Невідома команда!'


note_taker = NoteTaker()

while True:
    command = input('Введіть команду: ')
    if command == 'exit':
        break
    output = note_taker.parse_command(command)
    print(output)
