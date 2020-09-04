from itertools import permutations
from itertools import combinations
from itertools import product

a = []
b = []
items= [1,2,3,4]
for i in list(combinations(items,2)):
    a.append(i)
print(a)

for i in list(permutations(items,2)):
    b.append(i)
print(b)

num=8
j=0
while True:
    for i in product([1,4,6], repeat=j):
        print(i, sum(i))
        if sum(i)==num:
            print(j)
            exit(1)

    j+=1

