# /usr/bin/env python 3.10

import pytesseract
from PIL import Image

# указывам фото, которое необходимо распознать
img = Image.open(r'C:\Users\Zver\PycharmProjects\photo_text_recognising\input_photos\термодинамика и теплотехника.jpg')
# указываем путь к исполняемому файлу программы тессеракт
pytesseract.pytesseract.tesseract_cmd = r'c:\Users\Zver\AppData\Local\Tesseract-OCR\tesseract.exe'

# настройка точности распознования
custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, lang='rus', config=custom_config)
print(text)
with open(r'output_text\text.txt', mode='w', encoding='utf-8') as file:
    file.write(text)



