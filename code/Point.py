class Point:

    def __init__(self):
        self.__id = None
        self.__row = None
        self.__column = None
        self.__status = False
        self.__sign = "o"

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
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def sign(self):
        return self.__sign

    @sign.setter
    def sign(self, value):
        self.__sign = value

    def __str__(self):
        return \
            f"    ID:{self.id}\n" \
            f"    ROW:{self.row}\n" \
            f"    COLUMN: {self.column}\n" \
            f"    STATUS: {self.status}\n" \
            f"    SIGN:{self.sign}\n"

