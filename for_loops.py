"""
practice for loops
keyword: for   foreach
"""

cities = ["london", "newyork", "madrid", "paris", "ogden"]
#iterate over collection
for city in cities:
    print(city)

d = {'alice':'801-123-45-8989',
     'pedro':'999-999-45-0000',
     'john:': '123-456-78-9000'}
#iterate over a dictionary
for item in d:
    print(item, "=>", d[item])
