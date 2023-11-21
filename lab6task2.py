def spaces(string):
    i = 0
    _string_ = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    while string[0] not in (_string_):
        i += 1
    _string = ''
    for j in range(i,len(string)):
        _string += string[i] 
    return _string

def debil_guard_str(str:str):
    while True:
        try:
            string = input(str)
            if len(spaces(string)) == 0:
                raise ValueError
            break
        except:
            print('Введена пустая стока')
    return string

text = debil_guard_str('Введите текст -> ')
count = 0

for el in text:
    if el == 'A' or el == 'А':
        count += 1
print(count)