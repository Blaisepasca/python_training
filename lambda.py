#lambda agruments : expression
add10 = lambda x: x + 10
# Example usage
print(add10(5))  # Output: 15
print(add10(20))  # Output: 30

def add10_func(x):
    return x + 10

mult = lambda x,y: x+y
# Example usage
print(mult(5, 10))  # Output: 15
print(mult(20, 30))  # Output: 50

points2D =[1, 2], [3, 4], [5, 6],[10,-4]
points2D_sorted = sorted(points2D, key=lambda x: x[1])

print(points2D_sorted)  # Output: [(10, -4), (1, 2), (3, 4), (5, 6)]    
print(points2D_sorted)


#example
a =[1, 2, 3, 4, 5]
b =map(lambda x: x+2, a)
print(list(b))

c =[x*2 for x in a]
print(c)

d =[x/1 for x in a]
print(d)

e =[x-1 for x in a]
print(e)