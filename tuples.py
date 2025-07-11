mytuple =(1,2,3,4,5 ,)
print(mytuple)
item =mytuple[1:4]
print(item)

if 3 in mytuple :
    print('yes')
else:
    print('no')

print(len(mytuple))
print(mytuple.count(16))
print(mytuple.index(3))

my_tuple =("Blaise","pascal","kigali")
name,lastname,cite = my_tuple
print(name)
print(lastname)
print(cite)

import sys

my_list =[1,2,3,"hello Guys",4,5]
my_tuple =(1,2,3,"hello Guys",4,5)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")