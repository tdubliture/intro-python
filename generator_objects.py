"""
generator objects are a cross between comprehensions and generator functions
syntax similar to list comprehensions but with parenthesis:
    expr(item) for item in iterable)
"""
from list_comprehensions import is_prime

def main():
    """
    Test function
    :return: 
    """
    # list with first 1 million square numbers
    m_sq = (x*x for x in range(1,1000001))
    print(m_sq, type(m_sq))
    print("sum of the 1st 1 mill squares is ", sum(m_sq))
    print("sum of the 1st 1 mill squares is ", sum((x*x for x in range(1,1000001))))
    print("sum of the prime numbers between 1 and 1 mil", sum(x for x in range(10001) if is_prime(x)))
    



if __name__ == '__main__':
    main()
    exit(0)