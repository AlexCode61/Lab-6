from random import *

class N_ERROR(Exception):
    pass

def _abs(number):
    if number < 0:
        return number * (-1)
    return number

while True:
  try:
      n = int(input('Введите целое число N, количество элементов -> '))
      if n < 2:
        raise N_ERROR
      break
  except SyntaxError:
    print('Ошибка, введено не целое число')
  except N_ERROR:
    print('Ошибка, N < 2, минимум должно быть 2 элемента')

mas = [ randint(-100,100) for _ in range(n)]
print(mas)
minimum = 10**11
index = -1
summa = 0
null_index = -1

for i in range(len(mas)):
    if _abs(mas[i]) < _abs(minimum):
        minimum = mas[i]
        index = i
        
print(f'Минимальный элемент - {minimum} находится {(index+1)} элементом')

for i in range(len(mas)):
    if mas[i] == 0:
        null_index = i
        break

for i in range(null_index+1, len(mas)):
    summa += _abs(mas[i])

print(f'Сумма модулей элемнтов списка, расположенных после первого элемента, равного нулю {summa}')