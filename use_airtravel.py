"""
use flight class
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp

def main():
    """
    Test function
    :return: 
    """
    f1 = Flight("SN066",Aircraft("G-EUP","Airbus A319",
                                 num_rows=22,
                                 num_seats_per_row=6))

    f1.allocate_seat("02A", "Guido Van Rossum")
    f1.allocate_seat("12B", "Rasmus Lerdorf")
    f1.allocate_seat("15F", "Bjanre Stroustrup")
    f1.allocate_seat("03A", "Larry Wall")
    f1.allocate_seat("16F", "Yukihiro Mastsumoto")

    pp(f1._seating)

if __name__ == '__main__':
    main()
    exit(0)