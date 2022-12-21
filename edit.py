
import re

with open('text1.txt', mode='r', encoding='utf-8') as file:
    new_str = ''
    for line in file.readlines():
        if len(line) > 1 and line[-2] in '.!?...' and line[-1] == '\n':
            new_str += line
        else:
            new_str += line[:-1:]
    print(new_str)


my_str = "12. Определить       количество теплоты, переданного   в процессе теплового из"
print(my_str.replace(('  ', '   '), ' '))

