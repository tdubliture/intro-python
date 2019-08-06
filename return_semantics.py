"""
Learn about return semantics and function arguments in Python
"""


def egg(var):
    """
    returns a varible back to the user
    :param var: input object
    :return: input object
    """
    return var


def sum_two(num1, num2=8):
    """
    sum of two integer objects
    :param num1: obj 1
    :param num2: obj 2 optional default is 8
    :return: sum of objects
    """
    return num1 + num2


def banner(message,border = '*'):
    """
    prints a message with a border
    :param message: string to print
    :param border: *
    :return:
    """
    messlength = message.__len__()
    print(border*messlength+border*4)
    print(border,message,border)
    print(border*messlength+border*4)


def add_spam(menu = None):
    """
    add spam to the list
    :param menu:
    :return: menu list
    """
    if menu is None:
        menu = []
    menu.append('spam')
    return menu



def main():
    """
    Test function
    :return:
    """
    c = [6,10,20]
    e = egg(c)
    print(c is e)

    n1 = 3
    n2 = 9
    print(n1, " + ", n2, " = ", sum_two(n1,n2))
    print("only one input", sum_two(n1))
    banner("weber state","@")
    banner("utah state is better")

    breakfast = ['eggs', 'bacon']
    print("before ", breakfast)
    add_spam(breakfast)
    print('after', breakfast)


if __name__ == '__main__':
    main()
    exit(0)