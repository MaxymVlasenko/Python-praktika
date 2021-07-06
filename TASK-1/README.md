<h1 align="left">Task-1</h1>

<h3 align="left">Git clone</h3>
<p align="left">Зробіть git-клон вашого попереднього сховища.</p>

<p align="left">1. Посилання:https://github.com/MaxymVlasenko/Python-praktika.git</p>
<kbd>
    <img src="https://drive.google.com/uc?id=17tn4v1SVel_RawnNsDRSYnWhEKxm1ZTA" width="700px" alt="Task-1">
</kbd>

<br>
<br>

<p align="left">2. Введення команди :</p>

### Приклад

```shell
gh repo clone MaxymVlasenko/Python-praktika
```

<p align="left">3. Завдання: Створити програму, яка на вхід приймає рядок, та виділяє з нього всі
числа в окремий масив, після чого програма друкує рядок без чисел. і
масив чисел. Змінити цей рядок таким чином, щоб кожне слово в ньому,
починалось і закінчувалось великою літерою. Знайти максимальне
значення в масиві чисел, а всі інші числа піднести до степеню по їх
індексу, та записати в інший масив.</p> 

### Приклад

```python
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
```
<kbd>
    <img src="https://drive.google.com/uc?id=1Bkz2XwyOrOyByYxjlfqfPMO9JOe2DKwG" width="700px" alt="Task-1">
</kbd>
