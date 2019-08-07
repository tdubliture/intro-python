"""
Learn about dictionaries
"""
from pprint import pprint as pp

def main():
    """
    Test function
    :return: 
    """
    urls = {
        "google": "www.google.com",
        "yahoo": "www.yahoo.com",
        "twitter": "www.twitter.com",
        "wsu": "www.weber.edu"
    }

    print(urls, type(urls))
    #access by key: [key]
    print(urls["wsu"])
    #build dict with dict() constructor
    names_age = [('alice',32),("mario", 23), ('Hugo',21)]
    d = dict(names_age)
    print(d)
    # another method
    phonetic = dict(a='alpha', b='bravo', c='charlie', d='delta')
    print(phonetic)
    # copy a dict
    e = phonetic.copy()
    print(e)
    # updating a dictionary
    stocks = {'goog':891, 'appl':416, 'ibm':194}
    print(stocks)
    for key in stocks:
        print("{k} => {v}".format(k=key, v=stocks[key]))
    for val in stocks.values():
        print("val = ",val)
    for items in stocks.items():
        print(items)
    for key,val in stocks.items():
        print(key,val)
    #testing for membership
    print('goog' in stocks)
    print(891 in stocks)
    # deleting  del key word
    print(stocks)
    del stocks['ibm']
    print(stocks)
    #mutability of dictionaries
    isotopes = {
        'h' : [1,2,3],
        'he': [3,4],
        'li': [6, 7],
        'be': [7, 9, 10],
        'b': [10, 11],
        'c': [11, 12, 13, 14],
    }
    pp(isotopes)
    isotopes['h'] += [4,5,6,7]
    pp(isotopes)
    isotopes['n'] = [13,14,15]
    pp(isotopes)



if __name__ == '__main__':
    main()
    exit(0)