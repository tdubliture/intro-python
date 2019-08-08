"""
when working iwth iterators generators look at the doc for itertools module
"""
from itertools import islice, count, chain
from list_comprehensions import is_prime

def main():
    """
    Test function
    :return: 
    """
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type(thousand_primes))
    print("list of fist 1k prime numbers", list(thousand_primes))
    # in order to use thousand primes you have to regenerate it
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print("list of fist 1k prime numbers", sum(thousand_primes))
    # other built-ins use with itertools: any, all
    print(any([False, False, True]))
    print(all([False, False, True]))
    print(any( is_prime(x) for x in range(1328,1362)))

    names = ['London', 'New York', 'Ogden']
    print(all(name == name.title() for name in names))
    # another built in: zip
    sunday = [2,2,5,7,9,10,9,6,4,4]
    monday = [12,14,14,15,15,16,15,13,10,9]
    tuesday = [13,14,15,15,16,17,16,16,12,12]
    for temps in zip(sunday,monday,tuesday):
        print(min(temps),max(temps),sum(temps)/len(temps))

    #chaining
    all_temps = chain(sunday,monday,tuesday)
    print("all temps > 0", all(t>0 for t in all_temps))



if __name__ == '__main__':
    main()
    exit(0)