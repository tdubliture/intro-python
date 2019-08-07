"""
simulate 6000 rolls of a die (1-6)
"""
import random
import statistics


def roll_die(num):
    """
    random roll of a die
    :param num: number of rolls
    :return: a list of frequencies
    index 0 -> 1
    index 1 -> 2
    ect
    """

    freq = [0] * 6 # initial list value
    for roll in range(num):
        n = random.randrange(1,7)
        freq[n - 1] += 1
        #freq.append()
        #print(random.randrange(1, 7))
    return freq



def main():
    """
    Test function
    :return: 
    """
    num = int(input("how many times you need to roll die: "))
    result = roll_die(num)
    for roll, total in enumerate(result):
        print("Total rolls of {} = {}".format(roll + 1, total))
    print("average = {}".format((sum(result)/len(result))))
    print("average = {}".format((sum(result) / len(result))))
    print("average = {}".format((sum(result) / len(result))))



if __name__ == '__main__':
    main()
    exit(0)