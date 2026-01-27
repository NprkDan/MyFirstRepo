# immutable data types
# str,tuple,range
name = "Daniel"
print(type(name))
print(id(name))
name = name.upper()
print(name)
print(type(name))
print(id(name))
# --------------------------------------#
# tuple
points = ()
print(type(points))
print(id(points))
points = (1, 2, 3, 4, 5, 10, 12, 14, 6.6, "data", True)
print(type(points))
print(id(points))
print(points)
# points[0]=10
print(points)
points = points + (20, 30, 40) + (50,)
print(points)
print(type(points))
print(id(points))

x = "data"
y = "science"

x = x + y
print(x)
print(type(x))
print(id(x))
print(id(y))
print(y)

# --------------------------------------#
# range
numbers = range(1, 4)
print(type(numbers))
print(id(numbers))

print(numbers)
for i in range(numbers.start, numbers.stop):
    print("printing range upto 5:", i)
for i in range(2, 8):
    print("printing range from 2 to 8:", i)

for i in range(1, 10, 2):
    print("printing range from 1 to 10 with step 2:", i)
