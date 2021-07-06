import random as rndm

print('Введіть строку:')
String = input()

string = ''
mass = []

for index, i in enumerate(String):
    if i >= '0' and i <= '9':
        mass.append([int(i), int(index)])

for i in String:
    if i >= '0' and i <= '9':
        continue
    else:
        string += i

print('Строка без символів:', string)
print('Строка символів:', mass)

slova = []
slova = String.split()

for index, i in enumerate(slova):
    slova[index] = slova[index][0].upper() + slova[index][1:-1] + slova[index][-1].upper()
print('З великої літери:', ' '.join(slova), '\n')

maxymum = -1
for i in mass:
    if int(i[0]) > maxymum:
        maxymum = int(i[0])

mass2 = []
for i in mass:
    if int(i[0]) != maxymum:
        mass2.append([i[0], i[0]**i[1], i[1]])

print('Найбільше значення у масиві: ' + str(maxymum)  )
print('Підвищення чисел до степенів за їх індексом ([номер, ступінь, індекс], ...', mass2)
