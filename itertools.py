# from itertools import product

# a =[1,2]
# b=[3,4]
# prod =product(a,b, repeat =2)
# print(list(prod))


# from itertools import permutations

# a =[1,2,3]
# perm =permutations(a)
# print(list(perm))


# f

from itertools import groupby


persons =[{name :'Paci','age':35},{'name':'Aimerance','age':17},
          {'name':'Leah','age':25},{'name':'koko','age':35}]

goup_obj =groupby(persons, key =lambda x: x['age'])
for key, value in group_obj:
    print(key,list(value))

# from itertools import operator
# from itertools import count,cycle,repeat







