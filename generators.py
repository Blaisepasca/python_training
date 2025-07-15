def mygenerator():
    yield 4
    yield 2
    yield 0

g = mygenerator()
print(next(g))

