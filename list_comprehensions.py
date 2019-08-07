"""
list comprehensions
readable expresssive and effective
"""
from math import factorial, sqrt
from pprint import pprint as pp


def is_prime(num):
    """
    determine if a number is prime
    :param num: number to test
    :return: true for prime, false for non prime
    """
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def main():
    """
    Test function
    :return: 
    """
    words = "today i am very happy to learn about list comprehensions".split()
    print(words)
    data = []  #empty list
    for word in words:
        #some analysis
        data.append(word)

    # filter data
    print(data)

    info = [] #empty list
    # task find the length of the first 20 factorial numbers
    for x in range(20):
        #print(factorial(x))
        info.append(len(str(factorial(x))))
    pp(info)

    # use a list comprehension
    info2 = [len(str(factorial(x)))for x in range(20)]
    pp(info2)

    # set comprehensions {}
    info3 = {len(str(factorial(x)))for x in range(20)}
    pp(info3)

    # dictionary comprehensions{}
    nba_teams = {'jazz':'slc','warriors':'oakland', 'lakers':'la', 'clippers':'la'}
    teams_nba = {city:mascot for mascot, city in nba_teams.items()}
    pp(teams_nba)

    # filter predicates
    primes = [x for x in range(1001) if is_prime(x)]
    pp(primes)
    print(len(primes))



if __name__ == '__main__':
    main()
    exit(0)