mydict = {"name":"Blaise" ,"age": 25,"city":"kigali"}
print(mydict)

value = mydict["city"]
print(value)

mydict["lastname"] = "Pascal"
print(mydict)   
mydict["lastname"] = "Boula"
print(mydict)

if "lastname" in mydict:
    print(mydict["lastname"])
else:
    print("not found")
    #or the try except way
try:
    print(mydict["age"])
except :
    print("not found")

mydict.pop("lastname")
print(mydict)

mydict.update({"name":"Shadrack"})
print(mydict)

mydict.popitem()
print(mydict)

del mydict["name"]
print(mydict)

if "age" in mydict :
    print("yes")
else:
    print("no")