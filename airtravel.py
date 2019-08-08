"""
a flight class
"""


class Flight:
    """
    a flight with a particular passenger aircraft
    """

    def __init__(self,number):
        # implementation details begin with "_"
        # validate flight number
        # 5 char long AADDD
        if len(number) != 5:
            raise ValueError("Invalid Flight number lenght".format(number))
        if not number[:2].isalpha():
            raise ValueError("first two digits mush be letters")
        if not number[:2].isupper():
            raise ValueError("use upper case")
        if not number[2:].isdigit():
            raise ValueError("last three digits must be numbers")
        self._number = number

    def airline(self):
        """
        this returns the airline first two digits
        :return:
        """
        return self._number[:2]


    def number(self):
        """
        this returns flight number, last three digits
        :return: flight number
        """

        return self._number[2:]


class Aircraft:
    """
    aircraft class

    """
    def __init__(self,registration,model,num_rows,num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows =num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model




def main():
    """
    Test function
    :return: 
    """
    pass


if __name__ == '__main__':
    main()
    exit(0)