from dictionaries import BATTLESHIP_TYPES, BATTLESHIP_DIRECTIONS


class Battleship:

    def __init__(self):
        self.__id = None
        self.__direction = None
        self.__type = None
        self.__length = None
        self.__points = None

        print("BATTLESHIP SETUP INITIALIZED")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
        print(f"BATTLESHIP TYPE IS {BATTLESHIP_TYPES[value]}\n")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value
        print(f"BATTLESHIP DIRECTION IS {BATTLESHIP_DIRECTIONS[value]}\n")

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, values):
        points = []
        for value in values:
            value.id = self.id
            points.append(value)
            print(f"BATTLESHIP IS LOCATED AT {value} POINTS.")
        print("\n")
        self.__points = points

    def display_health(self):
        health = []
        for point in self.points:
            if point.sign == 1:
                health.append(point)
        print(f"THE REMAINED HEALTH OF BATTLESHIP {BATTLESHIP_TYPES[self.type]} IS {len(health)}")

    def __str__(self):
        return \
            f"BATTLESHIP: \n" \
            f"    ID:{self.id}\n" \
            f"    TYPE:{BATTLESHIP_TYPES[self.type]}\n"

