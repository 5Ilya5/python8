#Функция, которая генерирует файлы с разными расширениями. Это доработка домашней задачи №3 из 7 семинара#
from make_files import make_files
def new_make_file(extensions: dict):
    for extension, count in extensions.items():
        make_files(extension=extension, count=count)