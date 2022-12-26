# /usr/bin/env python 3.10
import pytesseract
from PIL import Image
import os

# указываем путь к исполняемому файлу программы тессеракт
pytesseract.pytesseract.tesseract_cmd = r'c:\Users\Zver\AppData\Local\Tesseract-OCR\tesseract.exe'

# настройка точности распознования
custom_config = r'--oem 3 --psm 6'


def recognise():
    ''' функция распознаёт все фото в указанной папке input_photos'''

    list_photos = os.listdir('input_photos')
    count = 1
    for item in list_photos:
        img = Image.open(f'input_photos\\{item}')
        text = pytesseract.image_to_string(img, lang='rus', config=custom_config)
        with open(r'output_text\text.txt', mode='a', encoding='utf-8') as file:
            file.write(text)
        print(f"[INFO] {count}/{len(list_photos)} ")
        count +=1


def extra_spaces():
    ''' функция убирает лишние пробелы'''

    with open(r'output_text\text.txt', mode='r+', encoding='utf-8') as file:
        reader = file.read()
        file.write(reader.replace('  ', ' '))


def remove_word_wraps():
    ''' функция убирает переносы слов,
    если слово пишется через дефис и попадает
    в конец строки - дефис уберётся
    '''

    with open(r'output_text\text.txt', mode='r', encoding='utf-8') as file:
        result_text = ''
        for line in file.readlines():
            if len(line) > 1 and line[-2] == '-':
                result_text += line[:-2:]
            else:
                result_text += line
    with open(r'output_text\text.txt', mode='w', encoding='utf-8') as file:
        file.write(result_text)


def paragraph_break():
    ''' функция оставляет перенос строки
    только после абзаца.
    Если строка заканчивается знаком препинания
    и есть перенос строки, тогда распознается как абзац
    '''

    with open(r'output_text\text.txt', mode='r', encoding='utf-8') as file:
        result_text = ''
        count = 0
        for line in file.readlines():
            print(f'{count}string is --- {line}')
            if len(line) > 1 and line[-2] in '.,!?:':
                print(f'-2 element is {line[-2]}')
                result_text += line
            elif len(line) > 1:
                result_text += line[:-1:] + ' '
                print(line[:-1:])
            else:
                pass
            count += 1
    with open(r'output_text\text.txt', mode='w', encoding='utf-8') as file:
        file.write(result_text)


def main():
    recognise()
    # extra_spaces()
    remove_word_wraps()
    paragraph_break()


if __name__=='__main__':
    main()

