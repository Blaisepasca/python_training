mylist =["banana","apple","orange"]
print(mylist)

mylist2 =list()
print(mylist2)

items =mylist[2]
print(items)

for i in mylist:
    print(i)

if "banana" in mylist :
    print('yes is there')
else:
    print('no is not there')

print(len(mylist))
mylist.append("lemon")
print(mylist)
print(len(mylist))

mylist.insert(0, "kiwi")
print(mylist)

items = mylist.pop()
print(items)
print(mylist)