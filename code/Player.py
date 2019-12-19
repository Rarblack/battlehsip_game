from Board import Board

from shortcuts import select_point, display_options, choose_value
from dictionaries import CONFIGURATION_OPTIONS


class Player:

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__board = None

        print("PLAYER SETUP INITIALIZED.\n")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
        print(f"SETTING PLAYER {value} UP\n")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        print(f"NAME IS SET TO {value}\n")

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, board):
        self.__board = board

    def create_board(self, length, width):
        board = Board()
        board.length = length
        board.width = width
        board.create_matrix()
        board.create_battleships()

        display_options(CONFIGURATION_OPTIONS)
        command = choose_value(CONFIGURATION_OPTIONS, "COMMAND: ")
        if command == 1:
            board.locate_battleships_automatically()
        else:
            board.locate_battleships_manually()
        board.display_matrix()

        self.board = board

    def shoot(self):
        target = select_point(self.board)
        valid = False
        while not valid:
            if target.is_unique_attempt():
                self.board.increase_attempt()
                if target.is_hit():
                    target.mark_hit()
                    self.board.increase_hit()
                    self.board.decrease_health()
                else:
                    target.mark_miss()
                    self.board.increase_miss()
                valid = True
            else:
                print("YOU HAVE ALREADY ATTEMPTED TO SHOOT AT THIS POINT\n")
                break

    def __str__(self):
        return f"I AM {self.name} AND MY PLAYER ID IS {self.id}"
