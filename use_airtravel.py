"""
use flight class
"""
from airtravel import Flight, Aircraft

def main():
    """
    Test function
    :return: 
    """
    f = Flight("SN066")
    print(f.number())
    f = Flight("SN665")
    print(f.number())

    # could use this notaion Flight.number(f)
    f = Flight("SN650")
    print(f.number())
    print(f.airline())

    a1 = Aircraft("G-EUP","Airbus A319",num_rows=22,num_seats_per_row=6)
    print(a1.registration(),a1.model(),a1._num_rows,a1._num_seats_per_row)


if __name__ == '__main__':
    main()
    exit(0)