import os
from random import randint

SYMBOLS = ('X', 'O')
WINNING_LINES = (
    ((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),
    ((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),
    ((0,0),(1,1),(2,2)),((0,2),(1,1),(2,0))
)

class Ai:
    def __init__(self, symbol, grid):
        self.symbol = symbol
        self.grid = grid
        self.ai_type = os.path.splitext(os.path.basename(__file__))[0]

    def check_winner(self):
        """
            Returns winning symbol, 'D', or None
        """
        for line in WINNING_LINES:
            row = []
            for cell in line:
                row.append(self.grid[cell[0]][cell[1]].text)

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

    def play_move(self, grid):
        """
            AI가 수를 둘 위치를 찾아서 둠
        """

        def make_move(r,c, symbol):
            self.grid[r][c].text = symbol

        def unmake_move(r,c):
            self.grid[r][c].text = ""

        # list에 빈 자리를 찾음
        possible_moves = [(r,c) for r in range(3) for c in range(3) if grid[r][c].text =='']

        # 내가 뒀을 때 유리한 위치   
        def win_pos():
            print("Rule Based (%s) #1: for Winning Position" %self.symbol)
            for i in possible_moves:
                make_move(*i, self.symbol)
                # make_move(i[0], i[1], self.symbol)
                if self.check_winner() == self.symbol:
                    unmake_move(*i)
                    return i
                else:
                    unmake_move(*i)

        # 상대가 뒀을 때 내가 지는 위치   
        def lose_pos():
            print("Rule Based (%s) #2: Not for Losing Position" %self.symbol)
            human_symbol = 'O' if self.symbol == 'X' else 'X'

            for i in possible_moves:
                make_move(*i, human_symbol)
                if self.check_winner() == human_symbol:
                    unmake_move(*i)
                    return i
                else:
                    unmake_move(*i)

        # 센터, 코너, 변의중앙 순으로 중요한 위치
        def favorable_pos():
            print("Rule Based (%s) #3: Favorable Position" %self.symbol)
            center = [(1,1)]
            corners = [(0,0),(0,2),(2,0),(2,2)]
            middle_sides = [(0,1), (1,0), (1,2), (2,1)]

            candidates = list(set(center+corners+middle_sides).intersection(possible_moves))
            if candidates:
                return candidates[0]

        return  win_pos() or \
                lose_pos() or \
                favorable_pos()
