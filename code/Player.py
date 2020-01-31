from Board import Board
from Notebook import Notebook

from shortcuts import input_number, display_options, choose_value
from dictionaries import CONFIGURATION_OPTIONS


class Player:

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__board = Board()
        self.__notebook = Notebook()

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def board(self):
        return self.__board

    @property
    def notebook(self):
        return self.__notebook

    def create_board(self, length, width):
        self.board.id = self.id
        self.board.length = length
        self.board.width = width
        print("Created a board")
        self.board.create_matrix()
        print("Created a matrix for the board")
        self.board.create_battleships()
        print("Created battleships for the board")
        display_options(CONFIGURATION_OPTIONS, "How should locating be?")
        option = choose_value(CONFIGURATION_OPTIONS)
        self.board.locate_battleships(False if option == 0 else True)
        print("Located battleships on the board")

    def create_notebook(self):
        self.notebook.id = self.id

    def shoot(self):
        self.notebook.attempts += 1
        row = input_number("Row -> ")
        column = input_number("Column-> ")
        target = self.board.matrix[row][column]
        if target.sign != "+" or target.sign != "-":
            if target.status:
                target.sign = "+"
                self.notebook.hits += 1
                self.notebook.health -= 1
            else:
                target.sign = "-"
                self.notebook.misses += 1
        else:
            print("ATTEMPTED BEFORE!!!")

    def __str__(self):
        return \
            f"    ID:{self.id}\n" \
            f"    NAME:{self.name}\n" \
            f"    BOARD ID:{self.board.id}\n" \
            f"    NOTEBOOK ID:{self.notebook.id}\n"
