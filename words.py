"""
get a file from the web:
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

task 1: count the number of words in a document
"""
from urllib.request import urlopen
file = r"http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

count = 0
data = {}
with urlopen(file) as story:
    for line in (story):
        words =  line.decode('utf-8').split()
        print(words)
        for word in (words):
            if word in data:
                data[word] += 1
            else:
                data[word] = 1
            count += 1
#sort by keys
for key in sorted(data.keys()):
    print(key, data[key])


print("total data", data)
print("total number of words", count)
