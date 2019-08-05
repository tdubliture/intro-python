"""
learn about control flow in python
"""

# IF Statement
# indentation is 4 spaces
if True:
    print("it is true")

if bool("eggs"):
    print("yes please!")

if "eggs":
    print("yes why not")

#flat is better than nested
h=42
if h > 50:
    print("greater than 50")
    if h > 100:
        print ("greater than 100")
elif h < 50:
    print ("less than 50")
else:
    print ("equal to 50")


#######
print("done")