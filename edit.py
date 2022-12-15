


with open('text1.txt', mode='r', encoding='utf-8') as file:
    all_text = file.read()
    # print(all_text)
    for line in all_text.split('\n'):
        print(line)
