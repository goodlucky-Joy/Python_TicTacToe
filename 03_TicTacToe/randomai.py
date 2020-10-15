import os
from random import randint

class Ai:
    def __init__(self, symbol, grid):
        self.symbol = symbol
        self.grid = grid
        self.ai_type = os.path.splitext(os.path.basename(__file__))[0]

    def play_move(self, grid):
        def random_ai():
            # list에 빈 자리를 찾음
            possible_moves = [(r,c) for r in range(3) for c in range(3) if grid[r][c].text =='']
            # 빈 자리 중에서 random 한 자리를 반환
            print("Random (%s)" %self.symbol)
            return possible_moves[randint(0, len(possible_moves)-1)]

        return random_ai()
