# Task-0 

<br>
<h2 align="left">Підключення ssh</h2>

### Приклад 

```shell
$ ssh-keygen -t rsa -b 4096 -C "visualsunity@gmail.com"
eval `ssh-agent -s`
ssh-add ~/.ssh/id_rsa
```
<kbd>
    <img src="https://drive.google.com/uc?id=1ioadIei7nNX8r9G1GYCKx4WodH6WGGAR" width="700px" title="Connection ssh">
</kbd>
    
<br>
<br>
<hr>

<h2 align="left">Task-0</h2>
<p align="left">Сформувати список з 30 випадкових цілих чисел від -100 до + 100.
Знайти максимальний елемент списку і його порядковий номер. Отримати
інший список, що складається тільки з непарних чисел вихідного списку
або повідомити, що таких чисел немає. Отриманий список вивести в
порядку зменшення елементів.</p>

### Приклад

```python
import random as rndm
data = []

for _ in range(0, 30):
    data.append(rndm.randint(-100, 100))

print('масив різних чисел:', data)
print('максимальне значення:', max(data))

counter = 1
for idx, i in enumerate(data):
    if i == max(data):
        print('   %s) Index (%s) = %s' % (counter, idx, i))
        counter+=1

odd = []
for elt in data:
    if elt % 2 != 0:
        odd.append(elt)
if len(odd) == 0:
    print('Без чисел')
else:
    print('Odd:', sorted(odd, reverse=True))
```
<kbd>
    <img src="https://drive.google.com/uc?id=1Bkz2XwyOrOyByYxjlfqfPMO9JOe2DKwG" width="700px" title="Task-0">
</kbd>
 
