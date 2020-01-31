from Player import Player

from dictionaries import MENU
from shortcuts import input_number, display_options, choose_value


class Game:

    def __init__(self):
        self.__players = None
        self.__command = None
        self.__winner = False

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, value):
        self.__command = value

    @property
    def winner(self):
        return self.__winner

    @winner.setter
    def winner(self, value):
        self.__winner = value

    def set_players_up(self):
        print("Length and width for both boards")
        length = input_number("Length -> ")
        width = input_number("Width -> ")
        print("Setting players up")
        players = []
        for _id in range(2):
            print(f"Setting player {_id} up")
            player = Player()
            player.id = _id
            player.name = input(f"Name -> ")
            player.create_board(length, width)
            player.create_notebook()
            print("Created a notebook")
            players.append(player)
        self.players = players

    def play(self):
        player_number = 0
        opponent_number = 1
        while not self.winner or self.command == 8:
            player = self.__players[player_number]
            opponent = self.__players[opponent_number]
            print(f"CURRENT PLAYER: {player.name}")

            display_options(MENU, "What command do you wish to choose?")
            command = choose_value(MENU)
            if command == 1:
                player.board.display_matrix()
            elif command == 2:
                print(f"HEALTH: {player.notebook.health}")
            elif command == 3:
                print(player.board.length * player.board.width)
            elif command == 4:
                print(f"NUMBER OF ATTEMPTS: {player.notebook.attempts}")
            elif command == 5:
                print(f"NUMBER OF HITS: {player.notebook.hits}")
            elif command == 6:
                print(f"NUMBER OF MISSES: {player.notebook.misses}")
            elif command == 7:
                opponent.shoot()
                if opponent.notebook.health == 0:
                    print(f"Player {player.name} won the game")
                    quit()
                if player_number == 0 and opponent_number == 1:
                    player_number = 1
                    opponent_number = 0
                elif player_number == 1 and opponent_number == 0:
                    player_number = 0
                    opponent_number = 1
            elif command == 8:
                print(f"Player {player.name} lost the game")
                quit()
