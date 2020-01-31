class Notebook:

    def __init__(self):
        self.__id = None
        self.__health = 17
        self.__attempts = 0
        self.__hits = 0
        self.__misses = 0

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value
        print(f"Health is updated. Remained health: {value}")

    @property
    def attempts(self):
        return self.__attempts

    @attempts.setter
    def attempts(self, value):
        self.__attempts = value
        print(f"TOTAL ATTEMPT: {value}")

    @property
    def hits(self):
        return self.__hits

    @hits.setter
    def hits(self, value):
        self.__hits = value
        print(f"TOTAL HITS: {value}")

    @property
    def misses(self):
        return self.__misses

    @misses.setter
    def misses(self, value):
        self.__misses = value
        print(f"TOTAL MISSES: {value}")
