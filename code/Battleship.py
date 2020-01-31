from dictionaries import BATTLESHIPS_INFORMATION_DICTIONARY


class Battleship:

    def __init__(self):
        self.__id = None
        self.__type = None
        self.__length = None
        self.__direction = None
        self.__points = None

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

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, values):
        points = []
        for value in values:
            value.id = self.id
            points.append(value)
            print(f"BATTLESHIP IS LOCATED AT [{value.row}, {value.column}] POINTS.\n")
        self.__points = points

    def get_health(self):
        health = []
        for point in self.points:
            if point.sign == "+":
                health.append(point)
        return len(health)

    def __str__(self):
        return \
            f"    ID:{self.id}\n" \
            f"    TYPE:{BATTLESHIPS_INFORMATION_DICTIONARY[self.id]['type']}\n" \
            f"    LENGTH: {BATTLESHIPS_INFORMATION_DICTIONARY[self.id]['length']}" \
            f"    HEALTH:{self.get_health()}"

