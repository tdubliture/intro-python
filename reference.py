"""
learn about references
"""


def modify(k):
    """
    modify the content of a list
    :param k:
    :return: nothing
    """
    # lists are passed by reference
    k.append(39)
    print("k = ", k)


def replace(g):
    """
    replace input list
    :param g:
    :return: nothing
    """
    g = [17,48,89]
    print("g = ", g)


def replace_content(g):
    """
    replace content of the input list
    :param g: input list
    :return: nothing
    """
    g[0] = 88
    g[1] = 22
    g[2] = 44
    print("g = ", g)


def main():
    """
    test function
    :return: nothing
    """
    m = [9,15,24]
    print("before modify() m = ", m)
    modify(m)
    print("after modify() = ", m)
    replace(m)
    print("after replace() = ", m)
    replace_content(m)
    print("after replace_content() = ", m)



if __name__ == '__main__':
    main()
    exit(0)