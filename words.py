"""
get a file from the web:
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

task 1: count the number of words in a document
"""
from urllib.request import urlopen
from functions import even_or_odd

def fetch_words(filename):
    """
    Finds the number of words in a text doc
    finds the number of occurrences of each word
    :param filename url to file
    :return:
    """

    count = 0
    data = []
    with urlopen(filename) as story:
        for line in (story):
            words = line.decode('utf-8').split()
            print(words)
            for word in (words):
                data.append(word)
    return data


def main():
    """
    test function
    :returns nothing
    """
    filename = r"http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    words = fetch_words(filename)
    print(words)

if __name__ == '__main__':
    main()
    exit(0)