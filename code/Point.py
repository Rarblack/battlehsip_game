class Point:

    def __init__(self):
        self.__id = None
        self.__row = None
        self.__column = None
        self.__sign = 0

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, value):
        self.__row = value

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        self.__column = value

    @property
    def sign(self):
        return self.__sign

    @sign.setter
    def sign(self, value):
        self.__sign = value

    def mark_hit(self):
        self.sign = "+"
        print("YOU HIT")

    def mark_miss(self):
        self.sign = "-"
        print("YOU MISSED")

    def is_hit(self):
        if self.sign != 1:
            return False
        return True

    def is_unique(self):
        if self.sign != 0:
            return False
        return True

    def is_unique_attempt(self):
        if self.sign == "+" or self.sign == "-":
            return False
        return True

    def __str__(self):
        return f"{[self.__row, self.__column]}"

