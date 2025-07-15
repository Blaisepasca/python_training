import copy
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

class company:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

p1 = Person("John", 30)
p2 = copy.copy(p1)  # Shallow copy
p3=copy.deepcopy(p1)  # Deep copy

p2.age =19
print(p2.age)
print(p1.age)  # Original object remains unchanged

print(p1.name)
print(p2.name)
print(p3.name)  # Deep copy retains original name

p1 = Person("Alice", 25)
p2 =Person("Bob", 40)


company = company(p1,p2)
company_clone =copy.copy(company)  # Shallow copy of company object
company_clone.boss.age =75
print(company_clone.boss.age)  # Changes in shallow copy affect original
print(company.boss.age)  # Original object reflects changes




# org = 3
# cpy = org
