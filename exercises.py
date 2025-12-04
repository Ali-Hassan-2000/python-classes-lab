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

        self.x_wins = 0
        self.o_wins = 0
        self.ties = 0

    
    def print_board(self):
        b = self.board
        print(f"""
              A   B   C
          1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
              ----------
          2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
              ----------
          3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):

        while True:
            move = input("Enter a valid move (example: A1): ").lower()

            if move not in self.board:
                print("That position does not exist. Try again.")
                continue

            if self.board[move] is not None:
                print("That space is already taken. Choose another one.")
                continue

            self.board[move] = self.turn
            break

    def check_winner(self):
        b = self.board

        winning_combinations = [
            # Rows
            ('a1', 'b1', 'c1'),
            ('a2', 'b2', 'c2'),
            ('a3', 'b3', 'c3'),

            # Columns
            ('a1', 'a2', 'a3'),
            ('b1', 'b2', 'b3'),
            ('c1', 'c2', 'c3'),

            # Diagonals
            ('a1', 'b2', 'c3'),
            ('c1', 'b2', 'a3'),
        ]

        for combo in winning_combinations:
            p1, p2, p3 = combo

            if b[p1] and (b[p1] == b[p2] == b[p3]):
                self.winner = b[p1]
                return

    def check_tie(self):
        
        # .values() get all the values in the board Object
        # all() checks if every item in an iterable is True.
        board_full = all(value is not None for value in self.board.values())
        no_winner = self.winner is None

        if board_full and no_winner:
            self.tie = True
    
    def switch_turns(self):

        # if statement will work also
        lookup = {
            'X': 'O',
            'O': 'X',
        }
        self.turn = lookup[self.turn]
    
    # ------------------------------------------
    
    def play_game(self):

        print("🎮 Welcome to Tic-Tac-Toe! Type positions like A1, B2, C3.\n")

        while not self.winner and not self.tie:

            self.render()        
            self.get_move()      
            self.check_winner()  
            self.check_tie()

            if not self.winner and not self.tie:
                self.switch_turns()

        if self.winner == 'X':
            self.x_wins += 1
        elif self.winner == 'O':
            self.o_wins += 1
        elif self.tie:
            self.ties += 1

        self.render()

        print(f"\nScoreboard:")
        print(f"X wins: {self.x_wins}")
        print(f"O wins: {self.o_wins}")
        print(f"Ties: {self.ties}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        
        if play_again == 'y':
            self.reset_game()
            self.play_game()
        else:
            print("Thanks for playing (;")

    def reset_game(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {key: None for key in self.board}



# --------------------------------------------------------
player = Game()

player.play_game()