import random
import collections
import sys
random.seed(42)


fnames = []
tasks = int(sys.argv[1])
with open('fnames.txt', 'r', encoding="utf8") as f:
    for line in f.readlines():
        fnames.append(line.strip())
random.shuffle(fnames)


workers = fnames[:tasks]


# рандомно выбираем тех, кого заставим работать больше всех
while len(workers) < tasks:
    workers.append(random.choise(fnames))
    
c = collections.Counter(workers)

print(list(range(1,3, -1)))
# ищем халявщиков
lazy_bois = list(set(fnames) - set(workers))
# берём халявщиков и менее нагруженных, и отправляем их чекать
worker_checkers = [x[0] for x in c.most_common()[:-(tasks - len(lazy_bois) + 1):-1]] 
checkers_1 = lazy_bois + worker_checkers

random.shuffle(checkers_1)

# пытаемся не отправить уже работавших на проверку
for slave in checkers_1:
    c[slave] += 0.5

# ещё раз
checkers_2 = [x[0] for x in c.most_common()[:-tasks - 1:-1]]

random.shuffle(checkers_2)




print('workers')
for x in workers:
    print(x)
print('_______________________________')
print('checkers_1')
for x in checkers_1:
    print(x)
print('_______________________________')
print('checkers_2')
for x in checkers_2:
    print(x)