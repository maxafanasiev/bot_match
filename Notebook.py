import datetime
from collections import UserDict


class Note:
    def __init__(self, note: str):
        self.content = []
        self.content.append(note)
        self.creation_date = datetime.datetime.now()

    def add_note(self, note: str):
        if note not in self.content:
            self.content.append(note)

    # def __repr__(self):
    #     return f"Note : {self.content} (Created on {self.creation_date})"

    def __str__(self):
        return ' ,'.join(self.content)


class Notebook(UserDict):
    def __init__(self):
        self.data = {}

    def iterator(self, n=10):
        self.page = 0
        self.record_per_page = int(n)
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
            out += '| {:^20} | {:^50} |\n'.format('Tags', 'Note')
            for page in self.iterator(2):
                out += '-' * 77 + '\n'
                out += ' {:^77} \n'.format(f"Page #{page_num}")
                out += '-' * 77 + '\n'
                for record in page:
                    out += '| {:^20} | {:^50} |\n'.format(', '.join(record[0]), str(record[1]))
                page_num += 1
        else:
            out += '| {:^77} |\n'.format('Notebook is empty.')
        out += '-' * 77 + '\n'
        return out

    def add_note(self, tags, note):
        self.data[tuple(tags)] = note

    def __getitem__(self, tags):
        matching_notes = []
        for note_tags, note in self.data.items():
            if all(tag in note_tags for tag in tags):
                matching_notes.append(note)
        return matching_notes

    def search_note(self, search_string):
        for note_obj in self.data.values():
            for note in note_obj.content:
                if search_string in note:
                    return note_obj


notebook = Notebook()
# Додавання нотаток до словника
notebook.add_note(['tag1', 'tag2'], Note('Content 1'))
notebook.add_note(['tag2', 'tag3'], Note('Content 2'))
notebook.add_note(['tag3', 'tag4'], Note('Ctent 3'))

notebook.search_note('Content 1').add_note('Cfdsfsdfds')
print(notebook)
# Отримання нотаток за тегами
# result = notebook[['tag2']]
# result1 = notebook[['tag3']]
# result2 = notebook[['tag4']]

# result_search = notebook.search_note('onte')

# print('\n')
#
# for note in result:
#     print(note)
#
# print('\n')
#
# for note in result1:
#     print(note)
#
# print('\n')
#
# for note in result2:
#     print(note)
#
# print('\n')

# print(', '.join([note for note in result_search]))
