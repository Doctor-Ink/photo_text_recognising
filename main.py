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

    with open(r'output_text\text.txt', mode='r', encoding='utf-8') as file:
        reader = file.read()
        reader.replace('  ', ' ')
        print(reader)


def main():
    recognise()
    extra_spaces()


if __name__=='__main__':
    main()

