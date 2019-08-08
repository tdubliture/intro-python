"""
module to demonstrate the use of generator executions
"""


def take(count,iterable):
    """
    take items from the front of an iterable
    :param count: maximum number of items to retrieve
    :param iterable: the source series
    :yields: at most 'count' items for iterable
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    """
    test the take function
    :return:
    """
    items = [2,4,6,8,10]
    for item in take(3,items):
        print(item)



def main():
    """
    Test function
    :return: 
    """
    run_take()
    


if __name__ == '__main__':
    main()
    exit(0)