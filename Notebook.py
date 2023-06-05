import datetime
from collections import UserDict


class Note:
    def __init__(self, content: str):
        self.content = ''
        limit = 80
        if len(content) <= limit:
            self.content = content
        else:
            raise ValueError(f'Нотатка довша {limit} символів.')
        self.creation_date = datetime.datetime.now()

    def __eq__(self, other_note):
        return self.content == other_note.content

    def __repr__(self):
        return self.content


class Notebook(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {}

    def __setitem__(self, tags, note: Note):
        tags.sort()
        if tuple(tags) not in self.data.keys():
            self.data[tuple(tags)] = []
            self.data[tuple(tags)].append(note)
        else:
            self.data[tuple(tags)].append(note)

    def __getitem__(self, tags):
        matching_notes = []
        for note_tags, notes in self.data.items():
            if all(tag in note_tags for tag in tags):
                if isinstance(notes, list):
                    for note in notes:
                        matching_notes.append(note)
                else:
                    matching_notes.append(notes)

        return matching_notes

    def edit_note(self, old_note: Note, new_note: Note):
        for note_list in self.data.values():
            if old_note in note_list:
                index = note_list.index(old_note)
                note_list[index] = new_note
                break
        else:
            raise ValueError('Нотатка не знайдена.')

    def clean_dict_keys(self, ):
        for key in self.data.keys():
            if not self.data[key]:
                self.data.pop(key)
                break

    def delete_note(self, old_note: Note):
        for note_list in self.data.values():
            if old_note in note_list:
                note_list.remove(old_note)
                self.clean_dict_keys()
                break
        else:
            raise ValueError('Нотатка не знайдена.')

    def search_in_content(self, search_string='/all'):
        matching_notes = []
        for note_list in self.data.values():
            for note in note_list:
                if search_string.lower() == '/all':
                    matching_notes.append(note)
                elif search_string.lower() in note.content.lower():
                    matching_notes.append(note)
        return matching_notes

    def iterator(self, n=10):
        self.page = 0
        self.record_per_page = n
        self.out = list(self.data.items())

        while True:
            start = self.page * self.record_per_page
            end = start + self.record_per_page
            page_record = self.out[start:end]

            if not page_record:
                return

            self.page += 1

            yield page_record

    def __str__(self):
        page_num = 1
        out = ''
        if self.keys():
            out += '-' * 77 + '\n'
            out += '| {:^20} | {:^50} |\n'.format('Теги', 'Зміст')
            for page in self.iterator(1):
                out += '-' * 77 + '\n'
                out += ' {:^77} \n'.format(f"Запис #{page_num}")
                out += '-' * 77 + '\n'
                for record in page:
                    out += '| {:^20} | {:^50} |\n'.format(', '.join(record[0]),
                                                          ', '.join([note.content for note in (record[1])]))
                page_num += 1
        else:
            out += '| {:^77} |\n'.format('Нотатник пустий.')
        out += '-' * 77 + '\n'
        return out





notebook = Notebook()

# Додавання нотаток до словника
note1 = Note('Content 1')
note2 = Note('Content 11ghjkdfhgkjdfhgkjhdfkghdfkj')
note3 = Note('Content 2')
note4 = Note('Ctent 3')

notebook[['tag1', 'tag2']] = note1
notebook[['tag2', 'tag1']] = note2
notebook[['tag2', 'tag3']] = note3
notebook[['tag3', 'tag4']] = note4
#


# print('\n Друк пошуку за тегами')
# result = notebook[['tag2']]
# result1 = notebook[['tag3']]
# result2 = notebook[['tag4']]
# print(result)
# print(result1)
# print(result2)


print(notebook)

'''Пошук за змістом та зміна нотатки'''

print('\nВивід пошуку за змістом')
search_string = input('Введіть рядок для пошуку (/all щоб показати всі): ')
result_search = notebook.search_in_content(search_string)

i = 1
for match in result_search:
    for tags, notes in notebook.data.items():
        for note in notes:
            if note == match:
                print(f"#{i} : {', #'.join(tags)} | {match}")
    i += 1

selected_note_index = int(input('Виберіть індекс нотатки для зміни: '))
inp = input('Що зробити з нотаткою? (edit, delete). ')

if inp == 'edit':
    # Вибір конкретної нотатки для зміни
    if 0 < selected_note_index < len(result_search)+1:
        selected_note = result_search[selected_note_index-1]
        new_content = input('Введіть новий вміст нотатки: ')
        new_note = Note(new_content)
        notebook.edit_note(selected_note, new_note)
        print('Нотатку успішно змінено.')
    else:
        print('Неправильний індекс нотатки.')

elif inp == 'delete':
    # Вибір конкретної нотатки для видалення
    if 0 < selected_note_index < len(result_search) + 1:
        selected_note = result_search[selected_note_index - 1]
        notebook.delete_note(selected_note)
        print('Нотатку успішно видалено.')
    else:
        print('Неправильний індекс нотатки.')

    print('\n Друк Notebook')

print(notebook)
