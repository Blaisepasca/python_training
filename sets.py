myset = set('hello everyone how are you Guys')
print(myset)

#set does not allow duplicates

myset ={1,2,3,4,44,4,1,2,6,7,8,9,9,0,0,0,1,4,8,1,5,3,5,5,}
print(myset)

myset.add(12)
myset.add(14)
print(myset)
myset.remove(4)

myset.discard(5)
print(myset)

for x in myset:
    print(x)

if 12 in myset:
    print("yes")
else:
    print("error please")

odds ={1,3,5,7,9}
evens ={2,4,6,8,10}
primes ={2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)

set1 ={1,2,3,4}
set2={1,2,3,4,5,6,7,8,9,}

diff =set2.difference(set1)
print(diff)

diff =set2.symmetric_difference(set1)
print(diff)

set1.update(set2)
print(set1)

set1.intersection_update(set2)
print(set1)

# and so menu other methods of sets