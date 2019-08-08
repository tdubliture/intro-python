"""
describe iterables series with code functions
are lazy evaluated the next value in the sequence is computed on demand
can model infinite series/sequences: data streams, mathematical series with no end
can use pipelines
use the yield keyword
"""


def gen123():
    yield 1
    yield 2
    yield 3
def gen246():
    print("about to yield 2")
    yield 2
    print("about to yield 4")
    yield 4
    print("about to yield 6")
    yield 6
    print("about to return")


def main():
    """
    Test function
    :return: 
    """
    g = gen123()
    print(g,type(g))
    # yield next value
    print(next(g))
    for v in gen123():
        print(v)




if __name__ == '__main__':
    main()
    exit(0)