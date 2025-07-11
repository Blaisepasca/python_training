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