"""
Learn dictionaries
dictionaries maps keys to values

in some languages are known as associative arrays, or hashes or maps

create them using {} containing a key-value pain
retrieve them by key value
retrieve them by [key_value]
"""
d = {'alice':'801-123-45-8989',
     'pedro':'999-999-45-0000',
     'john:': '123-456-78-9000'}
print(d, type(d))
#access one element
print(d['pedro'])

roster = {}
total =0
while total < 3:
    #get key value
    name = input("enter a name:")
    grade = input("enter grade")
    roster[name] = grade
    #roster.update(name,grade)
    #get value associated with key

    #add element to dictionary
    #not if key value exist it will update the value, otherwise it will be added

    total +=1
print(roster)