"""
get a file from the web:
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

task 1: count the number of words in a document
"""
from urllib.request import urlopen
from functions import even_or_odd


def fetch_words(filename):
    """
    count words in a url file
    :param filename url to file
    :return: a list of items
    """

    count = 0
    data = []   # empty list
    with urlopen(filename) as story:
        for line in (story):
            words = line.decode('utf-8').split()
            print(words)
            for word in (words):
                data.append(word)
    return data


def print_items(items):
    """
    Prints elements of the collection
    :param items
    :return: nothing
    """
    for item in items:
        print(item)


def main():
    """
    test function words library
    :returns nothing
    """
    filename = r"http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    words = fetch_words(filename)
    print_items(words)


if __name__ == '__main__':
    main()
    exit(0)