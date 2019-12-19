from CustomErrors import NegativeNumberError, NotInDictError


def input_number(title):
    while True:
        try:
            value = int(input(title))
            if value < 0:
                raise NegativeNumberError
            return value
        except NegativeNumberError:
            print("NEGATIVE NUMBER\n"
                  "HINT: ENTERED NUMBER MUST BE POSITIVE")
        except ValueError:
            print("WRONG INPUT!!!\n"
                  "HINT: A NUMBER MUST BE ENTERED")


def choose_value(dict, title):
    while True:
        try:
            value = input_number(title)
            if value not in dict.keys():
                raise NotInDictError
            return value
        except NotInDictError:
            print("CHOSEN VALUE IS NOT AVAILABLE \n"
                  "HINT: CHOOSE FROM DISPLAYED OPTIONS\n")


def select_point(board):
    while True:
        print("SELECTING POINT")
        try:
            column_index = input_number("ROW: ")
            print("")
            columns = board.matrix[column_index]

            column_index = input_number("COLUMN: ")
            print("")
            point = columns[column_index]

            return point
        except IndexError:
            print("NOT FOUND ERROR\n"
                  "HINT: POINT MUST BE ON THE BOARD\n")
            board.display_matrix()


def display_options(dict):
    for key, value in dict.items():
        print(f"{key}: {value}")
    print("")
