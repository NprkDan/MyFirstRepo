# Mutable data types in python
# list, set, dictionary
# list
list1 = []
print(type(list1))
print(id(list1))
list1 = [1, 2, 3, "data", 10.5, True]
print(type(list1))
print(id(list1))
print(list1)
list1.append(33)
print(list1)
print(list1.__len__())
name = "Krishna"
print(name.__len__())
print(id(list1))
list1[0] = 28
print(list1)
print(id(list1))
a = [100, 200]
print(id(a))
b = []
# b=a
print(id(a))
print(id(b))
b.append(300)
print(a)
print(b)
print(id(a))
print(id(b))
print("------------safe copy of list----------------------")
x = [1, 2, 3]
y = x.copy()
print(id(x))
print(id(y))
y.append(4)
print(x)
print(y)
print(id(x))
print(id(y))
