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

mylist.remove("kiwi")
print(mylist)

mylist.clear()
print(mylist)


mylist =['Rav4']
print(mylist)

mylist.append("Tesla")

print(mylist)

mylist.insert(3,"BMW")
print(mylist)

mylist =[1,9,0,2,11,-1,56]
mylist.sort()
print(mylist)

mylist.reverse()
print(mylist)
mylist =['Rav4,Tesla,BMw']
mylist = mylist[0].split(',')
print(mylist)

list =[0]*4
print(list)

list2 = [1,2,3,4,6]
print(list2)

newlist = list + list2
print(newlist)

list =[1,2,4,5,7,8,9,10,11,12,13]
a =list[1:4]
print(a)


list =["Dr congo" ,"Tanzania","uganda","kenya"]

listcopy = list
listcopy.append("cameroun")
print(listcopy)