"""
learn conditional repetition
two loops: for-loops and while-loops
"""

counter = 5
while counter != 0:
    print(counter)
    #augmented operator
    counter -= 1

counter = 5
while counter:
    print(counter)
    #augmented operator
    counter -= 1

# run forever
while True:
    print("enter a number")
    response = input() #take use input
    if int(response) % 7 == 0:
        break



print("outside while loop")

