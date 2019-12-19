from Point import Point
from Battleship import Battleship
from dictionaries import BATTLESHIP_DIRECTIONS, BATTLESHIP_LENGTHS, BATTLESHIP_TYPES

from shortcuts import choose_value, select_point, display_options
from CustomErrors import NotEmptyError


class Board:

    def __init__(self):
        self.__id = None
        self.__length = None
        self.__width = None
        self.__matrix = None

        self.__battleships = None
        self.__health = 1
        self.__attempts = 0
        self.__hits = 0
        self.__misses = 0

        print("BOARD SETUP INITIALIZED")

    @property
    def id(self):
        return self.__length

    @id.setter
    def id(self, value):
        self.__id = value
        print(f"Board length to {value} is set successfully.\n")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value
        print(f"BOARD LENGTH IS SET TO {value}\n")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        print(f"BOARD LENGTH IS SET TO {value}\n")

    @property
    def attempts(self):
        return self.__attempts

    @attempts.setter
    def attempts(self, value):
        self.__attempts = value
        print("")

    @property
    def hits(self):
        return self.__hits

    @hits.setter
    def hits(self, value):
        self.__hits = value

    @property
    def misses(self):
        return self.__misses

    @misses.setter
    def misses(self, value):
        self.__misses = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def battleships(self):
        return self.__battleships

    @battleships.setter
    def battleships(self, value):
        self.__battleships = value
        print("BATTLESHIPS HAVE BEEN CREATED \n")

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, value):
        self.__matrix = value
        print("MATRIX HAVE BEEN CREATED \n")

    def increase_attempt(self):
        self.attempts += 1
        print("ATTEMPT COUNT HAVE BEEN INCREASED \n")

    def increase_hit(self):
        self.hits += 1
        print("HIT COUNT HAVE BEEN INCREASED \n")

    def increase_miss(self):
        self.misses += 1
        print("MISS COUNT HAVE BEEN INCREASED \n")

    def decrease_health(self):
        self.health -= 1
        print("HEALTH COUNT HAVE BEEN DECREASED \n")

    def display_area(self):
        print(f"THE NUMBER OF POINTS ON BOARD IS {self.__length * self.__width}. \n")

    def create_matrix(self):
        matrix = []
        for i in range(0, self.length):
            columns = []
            for j in range(0, self.width):
                point = Point()
                point.row = i
                point.column = j
                columns.append(point)
            matrix.append(columns)

        self.__matrix = matrix

    def display_matrix(self):
        points = self.matrix
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
                row += str(points[i][j].sign)
                row += "  "
            row += " " + str(i)
            print(row)

        print("\n" + column_index)
        print("\n")

    def locate_battleships_manually(self):

        def horizontal_locating(point):
            row = point.row
            column = None
            try:
                for column in range(point.column, point.column + battleship.length):
                    choosen_point = self.matrix[row][column]
                    if choosen_point.sign == 1:
                        raise NotEmptyError
                    location_points.append(choosen_point)

                    for i in location_points:
                        i.id = battleship.id
                        i.sign = 1

                battleship.points = location_points
                return True
            except NotEmptyError:
                print(f"POINT [{row}, {column}] ALREADY EXIST \n")
            except IndexError:
                print(f"[{row}, {column}] IS OUT OF THE BOARD\n"
                      f"HINT: POINT MUST BE ON THE BOARD\n")
                self.display_matrix()

        def vertical_locating(point):
            row = None
            column = point.column
            try:
                for row in range(point.row, point.row + battleship.length):
                    choosen_point = self.matrix[row][column]
                    if choosen_point.sign == 1:
                        raise NotEmptyError
                    location_points.append(self.matrix[row][column])

                for i in location_points:
                    i.id = battleship.id
                    i.sign = 1

                battleship.points = location_points
                return True
            except NotEmptyError:
                print(f"POINT [{row}, {column}] ALREADY EXIST \n")
            except IndexError:
                print(f"[{row}, {column}] IS OUT OF THE BOARD\n"
                      f"HINT: POINT MUST BE ON THE BOARD\n")

        print("LOCATING BATTLESHIPS\n")
        for battleship in self.battleships:
            print(f"LOCATING BATTLESHIP {BATTLESHIP_TYPES[battleship.type]}")
            display_options(BATTLESHIP_DIRECTIONS)
            battleship.direction = choose_value(BATTLESHIP_DIRECTIONS, "DIRECTION: ")
            valid = False
            while not valid:
                point = select_point(self)
                location_points = []
                if battleship.direction == 1:
                    valid = horizontal_locating(point)
                elif battleship.direction == 2:
                    valid = vertical_locating(point)
            self.display_matrix()

    def locate_battleships_automatically(self):

        def horizontal_locating(point):
            row = point.row
            column = None
            try:
                for column in range(point.column, point.column + battleship.length):
                    choosen_point = self.matrix[row][column]
                    if choosen_point.sign == 1:
                        raise NotEmptyError
                    location_points.append(choosen_point)

                    for i in location_points:
                        i.id = battleship.id
                        i.sign = 1

                battleship.points = location_points
                return True
            except NotEmptyError:
                pass
            except IndexError:
                pass

        def vertical_locating(point):
            row = None
            column = point.column
            try:
                for row in range(point.row, point.row + battleship.length):
                    choosen_point = self.matrix[row][column]
                    if choosen_point.sign == 1:
                        raise NotEmptyError
                    location_points.append(self.matrix[row][column])

                for i in location_points:
                    i.id = battleship.id
                    i.sign = 1

                battleship.points = location_points
                return True
            except NotEmptyError:
                print(f"POINT [{row}, {column}] ALREADY EXIST \n")
            except IndexError:
                print(f"[{row}, {column}] IS OUT OF THE BOARD\n"
                      f"HINT: POINT MUST BE ON THE BOARD\n")

        import random
        print("LOCATING BATTLESHIPS\n")
        for battleship in self.battleships:
            print(f"LOCATING BATTLESHIP {BATTLESHIP_TYPES[battleship.type]}")
            battleship.direction = random.randint(1, 2)
            valid = False
            while not valid:
                row = random.randint(0, self.length - 1)
                column = random.randint(0, self.width - 1)
                point = self.matrix[row][column]
                location_points = []
                if battleship.direction == 1:
                    valid = horizontal_locating(point)
                elif battleship.direction == 2:
                    valid = vertical_locating(point)

    def create_battleships(self):
        battleships = []
        for i in range(1, 6):
            battleship = Battleship()
            battleship.type = i

            length = BATTLESHIP_LENGTHS[i]
            battleship.length = length

            battleships.append(battleship)

        self.battleships = battleships


