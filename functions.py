"""
learn about functions/definitions
use keyword def <name>()
"""


def even_or_odd(number):
    """
    find if number is even or odd
    :param number: input number
    :print "even" on even number
             "odd" on odd number
    """
    if number %2 == 0:
        print("even")
    else:
        print("odd")

def main():
    """
    test function
    :return: nothing

    """
    #call function
    print(__name__)
    even_or_odd(89)
    even_or_odd(92)

if __name__ ==  "__main__":
    main()
    exit(0)

