"""
Learn about list()
"""


def main():
    """
    Test function
    :return: 
    """
    s = "show how to do it".split()
    print(s, type(s))
    # access by index
    print("s[3]", s[3])
    print("last member:", s[len(s)-1])
    # pythoic way
    print("s[-1]:", s[-1])
    # slicing
    print("from 1 to one before last", s[1:-1])
    print("from 1 to three", s[1:3])
    print("from 1 to end", s[1:])
    print("from 0 to 1 less", s[:3])
    print("all of it", s[:])
    # make a copy of list
    t = s
    print("s", s)
    print("t", t)
    print("t is s:", t is s)
    t = s[:]
    print("s", s)
    print("t", t)
    print("t is s:", t is s)
    print("t == s", t == s)
    # shallow copies
    # a list of lists
    a = [[1,2],[3,4]]
    print(a, type(a))
    print("a[0]:", a[0])
    print("a[0][1]:", a[0][1])
    # copy the list of list
    b = a[:]
    a[0][0] = 0
    print(b)

    # repetition
    c = [21,37]
    d = c * 4
    print(d)

    s = [[-1,1]]*5
    print(s)
    s[1].append(7)
    print(s)

    #
    w = "the quick brown fox jumps over the lazy dog".split()
    i = w.index('fox')
    print("the index of 'fox' entry is:", i , w[i])
    # if no index is found it will throw a valueError

    #membership testing with count()

    print("'the' value is ", w.count("the"))
    # also test membership with in not it
    print(37 in [12,22,37,99])
    print(78 not in [12,22,37,99])
    # removing elements from list
    w = "the quick brown fox jumps over the lazy dog".split()
    print(len(w),(w))
    del w[3]
    print(len(w), (w))
    # remove using remove
    w.remove("over")
    print(len(w), (w))
    del w[w.index('dog')]
    del w[3]
    print(len(w),w)
    # rearranging list of elements
    g = [1,11,21,1211,112111]
    print("g",g)
    g.reverse()
    print("revers g", g)

    # sort
    d = [21,33,11,77,88,33,101,1]
    print("d:, ",d)
    d.sort()
    print("sorted d", d)
    d = [21,33,11,77,88,33,101,1]
    d.sort(reverse = True)
    print("reverse sorted d", d)
    # sort by key
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w)
    w.sort(key=len)
    print(w)



if __name__ == '__main__':
    main()
    exit(0)