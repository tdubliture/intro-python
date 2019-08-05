"""
learn about lists
unlike string, list are mutable
you can update and append elements to it
"""

# use brackets to define a list
l = [1,2,3]
print("list", l, type(l))
# a list of objects (any type)
a = ["apple", "orange", "pear"]
#access by index notion
print(a, a[1])
#replace an elemnt
a[0] = "tomatoes"
print(a, a[0])
a[1] = 3.14
print(a, a[1])

# begin with an empty list
names = []
counter = 3
while counter:
    name = input("Enter your name")
    names.append(name)
    counter -= 1
# display list
print(names)



