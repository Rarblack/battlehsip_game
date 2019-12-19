from Player import Player

from dictionaries import MENU
from shortcuts import input_number, display_options, choose_value

from CustomErrors import MoreThanNinetyNineError, LessThanTenError


class Game:

    def __init__(self):
        self.__players = []

    def set_up(self, number_of_players=2):

        def input_board_parameters():
            print("SETTING BOARD LENGTH AND WIDTH FOR ALL PLAYERS")
            while True:
                try:
                    length = input_number("BOARD LENGTH: ")
                    if length < 10:
                        raise LessThanTenError
                    if length > 99:
                        raise MoreThanNinetyNineError

                    width = input_number("BOARD WIDTH: ")
                    if width < 10:
                        raise LessThanTenError
                    if width > 99:
                        raise MoreThanNinetyNineError
                    print("")

                    return length, width
                except LessThanTenError:
                    print("INPUT IS NOT ALLOWED \n"
                          "HINT: INPUT VALUE MUST BE OVER OR EQUAL TO 10")
                except MoreThanNinetyNineError:
                    print("INPUT IS NOT ALLOWED \n"
                          "HINT: INPUT VALUE MUST BE LESS OR EQUAL TO 99")

        def create_player(id, length, width):
            player = Player()
            player.id = id
            player.name = input("NAME: ")
            player.create_board(length, width)
            self.__players.append(player)
            print(f"PLAYER {id} IS ON GAME NOW \n"
                  f"CREATION COMPLETED!\n")

        length, width = input_board_parameters()
        for id in range(1, number_of_players + 1):
            create_player(id, width, length)

    def play(self):
        print("GAME TIME \n")
        winner = False
        command = None
        player_number = 0
        opponent_number = 1
        while not winner or command == 8:
            player = self.__players[player_number]
            opponent = self.__players[opponent_number]
            print(f"CURRENT PLAYER: {player.name}")

            display_options(MENU)
            command = choose_value(MENU, "COMMAND: ")
            if command == 1:
                player.board.display_matrix()
            elif command == 2:
                print(f"HEALTH: {player.board.health}")
            elif command == 3:
                player.board.display_area()
            elif command == 4:
                print(f"NUMBER OF ATTEMPTS: {player.board.attempts}")
            elif command == 5:
                print(f"NUMBER OF HITS: {player.board.hits}")
            elif command == 6:
                print(f"NUMBER OF MISSES: {player.board.misses}")
            elif command == 7:
                opponent.shoot()
                if opponent.board.health == 0:
                    print(f"PLAYER {player.name} WON THE GAME")
                    quit()
                if player_number == 0 and opponent_number == 1:
                    player_number = 1
                    opponent_number = 0
                elif player_number == 1 and opponent_number == 0:
                    player_number = 0
                    opponent_number = 1
            elif command == 8:
                print(f"PLAYER {player.name} LOST THE GAME")
                quit()





