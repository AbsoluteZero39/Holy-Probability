import itertools

def permute(A):
    if len(A)==1:
        return [tuple(A)]
    permutations = []
    for x in A:
        for y in permute(A-{x}):
            permutations.append((x,)+y)
    return permutations

A = {1, 2, 3}

permute_all = set(permute(A))
print("Перестановки множини {}: {}".format(A,permute_all))
print("Кількість перестановок: ", len(permute_all))

# Використовуючи бібліотеку itertools
permute_all1 = set(itertools.permutations(A))
print("Перестановки множини {}: {}".format(A,permute_all1))
print("Кількість перестановок: ", len(permute_all1))
print('\n')

print("Now some tasks NUMBER 1\n\n")
print ("1.3 Задача")
# количество перестановок это ФАКТОРИАЛ
A1 = {1, 3, 5}
A2 = {1, 2, 3, 4}
A3 = [1, 2, 2, 1] # очевидно списком нужно, ведь множесвто убирает одинаковые элементы...

print("Перестановки множини {}: {}".format(A1,set(itertools.permutations(A1))))
print("Кількість перестановок: ", len(set(itertools.permutations(A1))))
print('\n')
print("Перестановки множини {}: {}".format(A2,set(itertools.permutations(A2))))
print("Кількість перестановок: ", len(set(itertools.permutations(A2))))
print('\n')
print("Перестановки множини {}: {}".format(A3,set(itertools.permutations(A3))))
print("Кількість перестановок: ", len(set(itertools.permutations(A3))))
print('\n')

A4 = {1, 2, 3, 4, 5}
A5 = {1, 2, 3, 4, 5, 6, 7}
A6 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}

print("Кількість перестановок: ", len(set(itertools.permutations(A4))))
print('\n')
print("Кількість перестановок: ", len(set(itertools.permutations(A5))))
print('\n')
print("Кількість перестановок: ", len(set(itertools.permutations(A6))))
print('\n')

print ("1.4 Задача")
A7 = {1, 2, 3}
A8 = {1, 2, 3, 4}
A9 = {1, 3, 5, 7}
A10 = [1, 2, 2, 1]

print( "for {1, 2, 3}")
res1 = set(itertools.permutations(A7))
a = []
A7=list(A7)
res1=list(res1)
for i in res1:
    if A7[0] == i[0] or A7[1] == i[1] or A7[2] == i[2]:
        a.append(i)
print(set(res1)-set(a))
print("\n")
print( "for {1, 2, 3, 4}")
res2 = set(itertools.permutations(A8))
a = []
A8=list(A8)
res2=list(res2)
for i in res2:
    if A8[0] == i[0] or A8[1] == i[1] or A8[2] == i[2] or A8[3] == i[3]:
        a.append(i)
print(set(res2)-set(a))
print("\n")
print( "for {1, 3, 5, 7}")
res3 = set(itertools.permutations(A9))
a = []
A9=list(A9)
res3=list(res3)
for i in res3:
    if A9[0] == i[0] or A9[1] == i[1] or A9[2] == i[2] or A9[3] == i[3]:
        a.append(i)
print(set(res3)-set(a))
print("\n")
print( "for A10 = [1, 2, 2, 1]")
res4 = set(itertools.permutations(A10))
a = []
res4=list(res4)
for i in res4:
    if A10[0] == i[0] or A10[1] == i[1] or A10[2] == i[2] or A10[3] == i[3]:
        a.append(i)
print(set(res4)-set(a))
print("\n")

print ("1.5 Задача")

A11 = {1, 2, 3, 4, 5, 6, 7, 8}
A12 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("for {1, 2, 3, 4, 5, 6, 7, 8}")
a = len(A11)
res = set(itertools.permutations(A11))
a=[]
for i in res:
    if i[0] < i[1] and i[1]<i[2] and i[2]<i[3] and  i[3]>i[4] and  i[4]>i[5] and  i[5]>i[6] and  i[6]>i[7]:
        a.append(i)
print(a,'\n')

print("for {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}")
a = len(A12)
res = set(itertools.permutations(A12))
a=[]
for i in res:
    if i[0] < i[1] and i[1]<i[2] and i[2]<i[3] and  i[3]>i[4] and  i[4]>i[5] and  i[5]>i[6] and  i[6]>i[7] and  i[7]>i[8] and  i[8]>i[9]:
        a.append(i)
print(a,'\n')
    
    



print("Now some tasks NUMBER 2\n\n")

# перестановки довжини k множини B
B = {1, 2, 3}
k = 2
permute_k = list(itertools.permutations(B, k))
print("Перестановки довжини {} множини {}: {}".format(k,A,permute_k))
print("Кількість таких перестановок: {}".format(len(permute_k)))

print ("2.2 Задача")

B1 = {1, 2, 3, 4}
B2 = {1, 3, 5, 7}
B3 = {1, 5, 8, 10, 15}

permute_k = list(itertools.permutations(B1, k))
print("Перестановки довжини {} множини {}: {}".format(k,A,permute_k))
print("Кількість таких перестановок: {}".format(len(permute_k)),'\n')

permute_k = list(itertools.permutations(B2, k+1))
print("Перестановки довжини {} множини {}: {}".format(k+1,A,permute_k))
print("Кількість таких перестановок: {}".format(len(permute_k)),'\n')

permute_k = list(itertools.permutations(B3, k))
print("Перестановки довжини {} множини {}: {}".format(k,A,permute_k))
print("Кількість таких перестановок: {}".format(len(permute_k)),'\n')

B4 = {1,2,3,4,5,6}
permute_k = list(itertools.permutations(B4, k))
print("Кількість таких(len=2) перестановок: {}".format(len(permute_k)),'\n')

permute_k = list(itertools.permutations(B4, k+2))
print("Кількість таких(len=4) перестановок: {}".format(len(permute_k)),'\n')

B5 = {1,3,5,7,9,11,13,15}
permute_k = list(itertools.permutations(B5, k+2))
print("Кількість таких(len=4) перестановок: {}".format(len(permute_k)),'\n')

print("Now some tasks NUMBER 3\n\n")

print ("3.2 Задача")

C = {1, 2, 3}
k=2
choose_k = list(itertools.combinations(C,k))
print("Комбінації довжини {} множини {}: {}".format(k,C,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)),'\n')

C1 = {1, 2, 3, 4}
choose_k = list(itertools.combinations(C1,k))
print("Комбінації довжини {} множини {}: {}".format(k,C1,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)),'\n')

C2 = {1, 3, 5, 7}
choose_k = list(itertools.combinations(C2,k+1))
print("Комбінації довжини {} множини {}: {}".format(k+1,C2,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)),'\n')

C3 = {1, 5, 8, 10, 15}
choose_k = list(itertools.combinations(C3,k))
print("Комбінації довжини {} множини {}: {}".format(k,C3,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)),'\n')

C4 = {1,2,3,4,5,6}
choose_k = list(itertools.combinations(C4,k))
print("Кількість таких(len=2) комбінацій: {}".format(len(choose_k)),'\n')

choose_k = list(itertools.combinations(C4,k+2))
print("Кількість таких(len=4) комбінацій: {}".format(len(choose_k)),'\n')

C5 = {1,3,5,7,9,11,13,15}
choose_k = list(itertools.combinations(C5,k+2))
print("Кількість таких(len=4) комбінацій: {}".format(len(choose_k)),'\n')

print ("3.3 Задача")

from random import randint
C6 = [randint(1,20) for i in range(10)]
print("Множина B може містити {} елементів.".format(len(list(itertools.combinations(C6, 2)))),'\n')

print("Now some tasks NUMBER 4\n\n")

D = {1, 2, 3}
k = 2
choose_k = list(itertools.combinations_with_replacement(D,k))
print("Комбінації довжини {} множини {}: {}".format(k,D,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ),'\n')

print ("4.2 Задача")

D1 = {1, 2, 3, 4}
choose_k = list(itertools.combinations_with_replacement(D1,k))
print("Комбінації довжини {} множини {}: {}".format(k,D1,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ),'\n')

D2 = {1, 3, 5, 7}
choose_k = list(itertools.combinations_with_replacement(D2,k+1))
print("Комбінації довжини {} множини {}: {}".format(k+1,D2,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ),'\n')

D3 = {1, 5, 8, 10, 15}
choose_k = list(itertools.combinations_with_replacement(D3,k))
print("Комбінації довжини {} множини {}: {}".format(k,D3,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ),'\n')

D4 = {1,2,3,4,5,6}

choose_k = list(itertools.combinations_with_replacement(D4,k))
print("Кількість таких (len=2) комбінацій: {}".format(len(choose_k)  ),'\n')

choose_k = list(itertools.combinations_with_replacement(D4,k+2))
print("Кількість таких (len=4) комбінацій: {}".format(len(choose_k)  ),'\n')

D5 = {1,3,5,7,9,11,13,15}
choose_k = list(itertools.combinations_with_replacement(D5,k+2))
print("Кількість таких (len=4) комбінацій: {}".format(len(choose_k)  ),'\n')

print ("4.4 Задача")

a=100000
b=999999
res=0
for i in range(a,b+1):
    i = str(i)
    if int(i[0])!= int(i[1]) and int(i[1])!= int(i[2]) and int(i[2])!= int(i[3]) and int(i[3])!= int(i[4]) and int(i[4])!= int(i[5]):
        res+=1
print(res,'\n')

print ("4.3 Задача")
num = itertools.product(range(10), repeat=6)
num=list(num)
a = 0
for i in num:
    if sum(i[:3]) == sum(i[3:]):
        a+=1

print(a)
