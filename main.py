# /usr/bin/env python 3.10
import pytesseract
from PIL import Image
import os


# настройка точности распознования
custom_config = r'--oem 3 --psm 6'


class Recognising:

    def __init__(self, folder, *args, **kwargs):
        self.folder= folder
        self.count = 0
        self.list_photos = 0

    def recognise_photo(self):
        ''' функция распознаёт все фото в указанной папке input_photos'''

        list_photos = os.listdir(path=f'{self.folder}')
        self.count = 1
        for item in list_photos:
            img = Image.open(f'{self.folder}\\{item}')
            text = pytesseract.image_to_string(img, lang='rus', config=custom_config)
            with open(f'{self.folder}\\text.txt', mode='a', encoding='utf-8') as file:
                file.write(text)
            print(f"[INFO] {self.count}/{len(list_photos)} ")
            self.count +=1

    def extra_spaces(self):
        ''' функция убирает лишние пробелы'''

        with open(f'{self.folder}\\text.txt', mode='r+', encoding='utf-8') as file:
            reader = file.read()
            file.write(reader.replace('  ', ' '))

    def remove_word_wraps(self):
        ''' функция убирает переносы слов,
        если слово пишется через дефис и попадает
        в конец строки - дефис уберётся
        '''

        with open(f'{self.folder}\\text.txt', mode='r', encoding='utf-8') as file:
            result_text = ''
            for line in file.readlines():
                if len(line) > 1 and line[-2] == '-':
                    result_text += line[:-2:]
                else:
                    result_text += line
        with open(f'{self.folder}\\text.txt', mode='w', encoding='utf-8') as file:
            file.write(result_text)

    def paragraph_break(self):
        ''' функция оставляет перенос строки
        только после абзаца.
        Если строка заканчивается знаком препинания
        и есть перенос строки, тогда распознается как абзац
        '''

        with open(f'{self.folder}\\text.txt', mode='r', encoding='utf-8') as file:
            result_text = ''
            for line in file.readlines():
                if len(line) > 1 and line[-2] in '.,!?:':
                    result_text += line
                elif len(line) > 1:
                    result_text += line[:-1:] + ' '
                else:
                    pass
        with open(f'{self.folder}\\text.txt', mode='w', encoding='utf-8') as file:
            file.write(result_text)


def main():
    pass
    # recognise= Recognising(folder=r'C:\Users\Zver\PycharmProjects\photo_text_recognising\input_photos')
    # recognise.recognise_photo()
    # recognise.remove_word_wraps()
    # recognise.paragraph_break()


if __name__=='__main__':
    main()

