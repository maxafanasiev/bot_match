import datetime
from collections import UserDict


class Note:
    def __init__(self, content: str):
        self.content = ''
        if len(content) <= 80:
            self.content = content
        else:
            raise ValueError('Note too long.')
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

    def search_in_content(self, search_string):
        matching_notes = []
        for note_list in self.data.values():
            for note in note_list:
                if search_string.lower() in note.content.lower():
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
            out += '| {:^20} | {:^50} |\n'.format('Tags', 'Note')
            for page in self.iterator(1):
                out += '-' * 77 + '\n'
                out += ' {:^77} \n'.format(f"Note #{page_num}")
                out += '-' * 77 + '\n'
                for record in page:
                    out += '| {:^20} | {:^50} |\n'.format(', '.join(record[0]),
                                                          ', '.join([note.content for note in (record[1])]))
                page_num += 1
        else:
            out += '| {:^77} |\n'.format('Notebook is empty.')
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


print('\n Друк пошуку за тегами')
result = notebook[['tag2']]
result1 = notebook[['tag3']]
result2 = notebook[['tag4']]
print(result)
print(result1)
print(result2)


print('\nВивід пошуку за змістом')
result_search = notebook.search_in_content('Content')
print(result_search)



print('\n Друк Notebook')
print(notebook)
