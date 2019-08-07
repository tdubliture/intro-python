"""
learn about exceptions
"""
import sys


def convert(s):
    """
    converts a string to integer
    :param s:
    :return:
    """

    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        pass
    return -1


def sqrt(x):
    """
    comput sqrt using methion of hero of ale
    :param x: number to compute the sqrt
    :return: the sqrt of x
    :raise: ValueError on zerodivision error
    """
    guess = x
    i = 0
    try:
        while guess*guess != x and i< 20:
            guess = (guess + x/guess)/2.0
        return guess
    except ZeroDivisionError:
        raise ValueError


def main():
    """
    Test function
    :return: 
    """
    #print(convert("11"))
    #print(convert('hello'))
    #print(convert([1,2,5]))
    try:
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(-1))
    except ValueError:
        print("cannot compute the value of negitive numbers")
    print("done")


if __name__ == '__main__':
    main()
    exit(0)