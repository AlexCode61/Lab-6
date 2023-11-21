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

def debil_guard_str(str):
    while True:
        try:
            string = input(str)
            if len(spaces(string))==0:
                raise ValueError
            break
        except ValueError:
            print('Введена пустая стока')
    return spaces(string)

def debil_guard_int(str):
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