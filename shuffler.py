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


# ищем халявщиков
lazy_bois = list(set(fnames) - set(workers))
# берём халявщиков и менее нагруженных, и отправляем их чекать
worker_checkers = [x[0] for x in c.most_common()[:-(tasks - len(lazy_bois)):-1]] 
checkers_1 = lazy_bois + worker_checkers

# пытаемся не отправить уже работавших на проверку
for slave in worker_checkers:
    c[slave] += 0.5

# ещё раз
worker_checkers = [x[0] for x in c.most_common()[:-(tasks - len(lazy_bois)):-1]] 
checkers_2 = lazy_bois + worker_checkers

# циклический сдвиг, чтобы лентяии по 2 раза не чекали
checkers_2 = checkers_2[1:] + checkers_2[:1] 


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