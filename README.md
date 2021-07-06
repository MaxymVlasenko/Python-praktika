<h1 align="left">Task-1</h1>

<h3 align="left">Git clone</h3>
<p align="left">Make a git clone of your past repository.</p>

<p align="left">1. Copy url:</p>
<kbd>
    <img src="../Images/Task-1_2.png" width="700px" alt="Task-1">
</kbd>

<br>
<br>

<p align="left">2. Entering the command into the terminal:</p>

### Example command

```shell
$ git clone https://github.com/sergden2021/python-practice.git
```

<kbd>
    <img src="../Images/Task-1_2.1.png" width="700px" alt="Task-1">
</kbd>

<br>
<br>

<p align="left">3. Task: Create a program, if you enter a row, that sees all the numbers in the surrounding array, for which the program is another row without numbers. and an array of numbers. The change of a row in such a rank, so that the word is skinny in new, was repaired and ended with a great letter. To know the maximum value in the array of numbers, and all of the іnshі numbers are brought to the degree according to the іх index, that is recorded in the first array.</p> 

### Example

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

<br>
<em><p align="left">An example of running a program with three different introductory sentences:</p></em>

<kbd>
    <img src="../Images/Task-1_1-1.png" width="700px" alt="Task-1">
</kbd>

