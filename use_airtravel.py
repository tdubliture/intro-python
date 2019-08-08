"""
use flight class
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp


def make_flight():
    """

    :return:
    """

    flight = Flight("SN066", Aircraft("G-EUP", "Airbus A319",
                                  num_rows=22,
                                  num_seats_per_row=6))

    flight.allocate_seat("02A", "Guido Van Rossum")
    flight.allocate_seat("12B", "Rasmus Lerdorf")
    flight.allocate_seat("15F", "Bjanre Stroustrup")
    flight.allocate_seat("03A", "Larry Wall")
    flight.allocate_seat("16F", "Yukihiro Mastsumoto")

    return flight


def console_card_printer(passenger,seat,flight_number,aircraft):
    output = "| Name: {0}"\
            "Flight: {1}"\
            "Seat: {2}"\
            "Aircraft: {3}"\
            "|".format(passenger,seat,flight_number,aircraft)

    banner = "+" + "-" * (len(output)-2)+ "+"
    border = "|" + " " * (len(output)-2)+ "|"
    lines = [banner,border,output,border,banner]
    card = '\n'.join(lines)
    print(card)



def main():
    """
    Test function
    :return: 
    """
    flight_1 = make_flight()
    pp(flight_1._seating)
    print("available seats", flight_1.num_available_seats())

    flight_1.make_boarding_class(console_card_printer)


if __name__ == '__main__':
    main()
    exit(0)