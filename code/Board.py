from Point import Point
from Battleship import Battleship

from dictionaries import ALLOWED_DIRECTIONS, BATTLESHIPS_INFORMATION_DICTIONARY
from shortcuts import input_number, choose_value, display_options
from CustomErrors import NotEmptyError


class Board:

    def __init__(self):
        self.__id = None
        self.__length = None
        self.__width = None
        self.__matrix = None
        self.__battleships = None

    @property
    def id(self):
        return self.__length

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def battleships(self):
        return self.__battleships

    @battleships.setter
    def battleships(self, value):
        self.__battleships = value

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, value):
        self.__matrix = value

    def create_matrix(self):
        matrix = []
        for row in range(self.length):
            columns = []
            for column in range(self.width):
                _id = column+row*10
                point = Point()
                point.id = _id
                point.row = row
                point.column = column
                columns.append(point)
            matrix.append(columns)
        self.matrix = matrix

    def create_battleships(self):
        battleships = []
        for _id in BATTLESHIPS_INFORMATION_DICTIONARY.keys():
            battleship = Battleship()
            battleship.id = _id
            battleship.type = BATTLESHIPS_INFORMATION_DICTIONARY[_id]["type"]
            battleship.length = BATTLESHIPS_INFORMATION_DICTIONARY[_id]["length"]
            battleships.append(battleship)
        self.battleships = battleships

    def locate_battleships(self, automatic):
        for battleship in self.battleships:
            print(f"Locating battleship {battleship.type}")
            row = None
            column = None
            valid = False
            while not valid:
                try:
                    if automatic:
                        import random
                        battleship.direction = random.randint(0, 1)
                        row = random.randint(0, self.length - 1)
                        column = random.randint(0, self.width - 1)
                    else:
                        display_options(ALLOWED_DIRECTIONS)
                        battleship.direction = choose_value(ALLOWED_DIRECTIONS)
                        row = input_number("Locating: row -> ")
                        column = input_number("Locating: column -> ")

                    targets = []
                    start = column if battleship.direction == 0 else row
                    for index in range(start, start + battleship.length):
                        target = self.matrix[row if battleship.direction == 0 else index][index if battleship.direction == 0 else column]
                        if target.status:
                            raise NotEmptyError
                        targets.append(target)

                    for target in targets:
                        target.status = True
                        target.sign = battleship.id

                    battleship.points = targets

                    self.display_matrix()
                    valid = True
                except NotEmptyError:
                    print(f"Point [{row}, {column}] is not empty")
                except IndexError:
                    print(f"[{row}, {column}] is out of the board\n"
                          f"HINT: Point must be within [0, 0] and [{self.length}, {self.width}]\n")

    def display_matrix(self):
        matrix = self.matrix
        column_index = "    "
        for t in range(0, self.width):
            if t < 10:
                column_index += (str(t) + "  ")
            elif t >= 10 or t < 100:
                column_index += (str(t) + " ")

        print(column_index + "\n")

        for i in range(0, self.length):
            row = None

            if i < 10:
                row = f"{i}   "
            elif i >= 10 or i < 100:
                row = f"{i}  "

            for j in range(0, self.width):
                row += str(matrix[i][j].sign)
                row += "  "
            row += " " + str(i)
            print(row)

        print("\n" + column_index)
        print("\n")


