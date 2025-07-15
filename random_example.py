import random

mylist = list("QBERCYIL")
a = random.choice(mylist)
print(a)

mylist = list("QBERCYIL")
a = random.sample(mylist ,3)
print(a)

mylist = list("QBERCYIL")
a = random.choice(mylist)
print(a)

mylist = list("QBERCYIL")
a = random.shuffle(mylist)
print(mylist)

#other examples

import numpy as np

a = np.random.randint(0, 10, (3,4))
print(a)