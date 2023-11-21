def spaces(string):
    index = 0
    try:
        while string[index] in ' ':
            index += 1
        new_string = ''
        for i in range(index,len(string)):
            new_string += string[i]
        return new_string
    except:
        return ''

def debil_guard_str(str:str):
    while True:
        try:
            string = input(str)
            if len(spaces(string)) == 0:
                raise ValueError
            break
        except:
            print('Введена пустая стока')
    return spaces(string)

text = debil_guard_str('Введите текст -> ')
count = 0

for el in text:
    if el == 'A' or el == 'А':
        count += 1
print(count)