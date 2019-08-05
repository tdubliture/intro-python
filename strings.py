"""
strings and collections

a string is an immutable sequence of unicode code-points
"""
print('this is a string')
print ("this is a string too")

#concatenation and adjacent strings
s1 = "First"
s2 = "Second"
print(s1 + s2)

#multiline strings and newlines
s3 = """this is 
a multi-line
string"""
print(s3)
s4 = "this is\na multi-line\nstirng"
print(s4)

#support for backslash
s5 = "A\\in a string"
print(s5)