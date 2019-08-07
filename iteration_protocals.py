"""
Learn about iterable iterator objects
use the built-in:
iter(): create an iterable object
next(): fetch the next element in the iterable object
"""


def first(iterable):
    """
    return the next member on the list if available
    :param iterable: iterable object
    :return: next member or
    :except: ValueError for StopIteration
    """
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

def main():
    """
    Test function
    :return: 
    """
    iterable = ['spring','summer','fall','winter']
    iterator = iter(iterable)
    print(type(iterator),iterator)
    print(next(iterator))
    first(iterable)


if __name__ == '__main__':
    main()
    exit(0)