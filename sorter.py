import os
import shutil


class Sorter:

    CATEGORIES = dict(IMAGE=['jpeg', 'png', 'jpg', 'svg'],
                      VIDEO=['avt', 'mp4', 'mov', 'mkv'],
                      DOCS=['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx', 'rtf'],
                      MUSIC=['mp3', 'ogg', 'wav', 'amr'],
                      ARCHIVE=['zip', 'gz', 'tar', '7z'],
                      OTHER=[])
    IGNORE = ['.DS_Store']

    translate_dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
                      'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
                      'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
                      'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
                      'ю': 'u', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO',
                      'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
                      'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
                      'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
                      'Ю': 'U', 'Я': 'YA', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
                      'Є': 'e', '1': '1', '2': '2', '3': '3'}

    def file_list_by_folder(self, sorted_path):
        for folder in os.listdir(sorted_path):
            way = os.listdir(os.path.join(sorted_path, folder))
            print('{:>50} - {:<50} '.format('Folder', folder))
            print('{:^100}'.format('-' * 99))
            for file in way:
                print('{:^5} {:<95} '.format('', file))
            print('\n')
            print('{:^100}'.format('-' * 99))

    def translite(self, word):
        for key in self.translate_dict:
            word = word.replace(key, self.translate_dict[key])
        return word

    def normalize(self, sorted_path):
        for el in os.listdir(sorted_path):
            tel = self.translite(el)
            os.rename(os.path.join(sorted_path, el), os.path.join(sorted_path, tel))

    def create_ext_set(self, sorted_path):
        ext_set = set()
        for el in os.listdir(sorted_path):
            ext = el.split('.')[-1]
            if os.path.isfile(os.path.join(sorted_path, el)) and ext in str(self.CATEGORIES.values()):
                ext_set.add(ext)
        return ext_set

    def create_un_ext_set(self, sorted_path):
        ext_set = set()
        for el in os.listdir(sorted_path):
            ext = el.split('.')[-1]
            if os.path.isfile(os.path.join(sorted_path, el)) and ext not in str(self.CATEGORIES.values()):
                ext_set.add(ext)
        return ext_set

    def del_empty_dirs(self, address):
        for dirs in os.listdir(address):
            dir = os.path.join(address, dirs)
            if os.path.isdir(dir):
                self.del_empty_dirs(dir)
                if not os.listdir(dir):
                    shutil.rmtree(dir)

    def deep_folders(self, sorted_path):
        for subdir, dirs, files in os.walk(sorted_path):
            for file in files:
                src = os.path.join(subdir, file)
                dst = os.path.join(sorted_path, file)
                shutil.move(src, dst)
            self.del_empty_dirs(sorted_path)

    def create_sort_folders(self, sorted_path):
        for category in self.CATEGORIES:
            if category not in os.listdir():
                os.mkdir(os.path.join(sorted_path, category))

    def get_category(self, ext):
        for category, extensions in self.CATEGORIES.items():
            if ext in extensions and ext not in self.IGNORE:
                return category
        return "OTHER"

    def sort(self, sorted_path):
        for el in os.listdir(sorted_path):
            if os.path.isfile(os.path.join(sorted_path, el)):
                ext = el.split('.')[-1]
                category = self.get_category(ext)
                target_folder = os.path.join(sorted_path, category)
                if category == "ARCHIVE":
                    shutil.unpack_archive(os.path.join(sorted_path, el), target_folder)
                    os.remove(os.path.join(sorted_path, el))
                    continue
                shutil.move(os.path.join(sorted_path, el), target_folder)

    def move_to(self, sorted_path, destination=''):
        if destination:
            for el in os.listdir(sorted_path):
                shutil.move(os.path.join(sorted_path, el), destination)
            shutil.rmtree(sorted_path)

    def main(self, sorted_path, destination):
        self.deep_folders(sorted_path)
        with_ext = self.create_ext_set(sorted_path)
        without_ext = self.create_un_ext_set(sorted_path)
        self.normalize(sorted_path)
        self.create_sort_folders(sorted_path)
        self.sort(sorted_path)
        self.file_list_by_folder(sorted_path)
        self.move_to(sorted_path, destination)
        print('{:^100}'.format('*' * 100))
        print(f"Founded file's with know extension: {with_ext}")
        print(f"Founded file's with unknown extension: {without_ext}")
        print('{:^100}'.format('*' * 100))


if __name__ == '__main__':
    a = input('Source :')
    b = input('Destination :')
    sort = Sorter()
    sort.main(a, b)



