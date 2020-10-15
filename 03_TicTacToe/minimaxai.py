import os
from random import randint

INFINITY = 999

SYMBOLS = ('X', 'O')

# checking winning case
WINNING_LINES = (
                    ((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),
                    ((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),
                    ((0,0),(1,1),(2,2)),((0,2),(1,1),(2,0))
                )

class Ai:

    def __init__(self, symbol, grid):
        self.symbol = symbol
        self.AI = symbol
        self.HUMAN = 'O' if self.AI == 'X' else 'X'
        self.grid = grid
        self.ai_type = os.path.splitext(os.path.basename(__file__))[0]

    def possible_moves(self, grid):
        return[(r,c) for r in range(3) for c in range(3) if grid[r][c].text =='']

    def make_move(self, r, c, symbol):
        self.grid[r][c].text = symbol

    def unmake_move(self, r, c):
        self.grid[r][c].text = ''

    def check_winner(self):
        """
            Returns winning symbol, 'D', or None
        """
        # Winning checking
        for line in WINNING_LINES:
            row = []
            for (r,c) in line:
                row.append(self.grid[r][c].text)

            for symbol in SYMBOLS:
                if all([s==symbol for s in row]):
                    return symbol

        # 게임 진행중
        for row in self.grid:
            for col in row:
                if col.text == '':
                    return None

        # Draw
        return 'D'

    def play_move(self, grid):    # game AI
        best_score = -INFINITY
        move = (-1, -1)

        for (r,c) in self.possible_moves(grid):
            self.make_move(r, c, self.AI)
            score = self.minimax(1, False, grid)
            self.unmake_move(r, c)

            if score > best_score:
                best_score = score
                move = (r, c)

        self.make_move(*move, self.AI)
        return move

    def minimax(self, depth, is_max_step, grid):
        #static evaluation
        winner = self.check_winner()
        if winner == self.AI:
            return 10
        elif winner == self.HUMAN:
            return -10
        elif winner == 'D':
            return 0

        if depth > 8:   # depth는 조정 가능
            return 0

        if is_max_step:
            best_score = -INFINITY;
            for (r,c) in self.possible_moves(grid):
                self.make_move(r, c, self.AI)
                score = self.minimax(depth + 1, False, grid)
                self.unmake_move(r, c)

                best_score = max(score, best_score)

            return best_score
        
        else:
            best_score = +INFINITY;
            for (r,c) in self.possible_moves(grid):
                self.make_move(r, c, self.HUMAN)
                score = self.minimax(depth + 1, True, grid)
                self.unmake_move(r, c)
                
                best_score = min(score, best_score)

            return best_score
