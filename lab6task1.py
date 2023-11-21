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

def debil_guard_int(str:str):
    while True:
        try:
            integer = int(input(str))
            break
        except:
            print('ERROR - 1\nВведено не число')
    return integer

n1 = debil_guard_int('Введите положительное число N1 -> ')
n2 = debil_guard_int('Введите положительное число N2 -> ')
s1 = debil_guard_str('Введите строку S1 -> ')
s2 = debil_guard_str('Введите строку S2 -> ')
new_s = ''
if n1 == 0 and n2 == 0:
    print('Полученна пустая строка')
else:
    if n1 > len(s1):
        new_s = s1
    else:
        for i in range(n1):
            new_s += s1[i]
    if n2 >= len(s2):
        new_s += s2
    else:
        for i in range(len(s2)-n2,len(s2)):
            new_s += s2[i]
        print(f'Полученная новая строка - {new_s}')