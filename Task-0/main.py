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
