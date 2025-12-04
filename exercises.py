class Game:
    def __init__(self):

        self.turn = 'X'
        self.tie = False
        self.winner = None

        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
    
    def play_game(self):
        print("🎮 Welcome to Tic-Tac-Toe! The game is starting...")


player1 = Game()

player1.play_game()