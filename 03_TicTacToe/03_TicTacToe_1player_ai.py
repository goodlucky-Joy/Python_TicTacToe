import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from random import randint
#from randomai import Ai
#from rulebasedai import Ai
from minimaxai import Ai

WINNING_LINES = (
    ((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),
    ((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),
    ((0,0),(1,1),(2,2)),((0,2),(1,1),(2,0))
)

SYMBOLS = ('X', 'O')

def symbol_generator():
    while True:
        for symbol in SYMBOLS:
            yield symbol


class Board(GridLayout):

    grid = None
    symbols = None

    def __init__(self, cols=3, **kwargs):
        super(Board, self).__init__(**kwargs)

        self.cols = cols
        self.rows = cols
        self.symbols = symbol_generator()

        self.grid = [[None for col in range(self.cols)] for row in range(self.rows)]

        self.draw_tiles()
        self.init_players()

    def init_players(self):
        # Who is the first?
        self.bot = Ai(SYMBOLS[randint(0,1)], self.grid)

        if self.bot.symbol == 'X':
            (r,c) = self.bot.play_move(self.grid)
            self.grid[r][c].text = next(self.symbols)
            self.grid[r][c].font_size = 100

    def draw_tiles(self):
        for row in range(self.rows):
            for col in range(self.cols):
                tile = Button()
                tile.bind(on_release=self.on_click)
                self.grid[row][col] = tile
                self.add_widget(tile)

    def on_click(self, instance):
        # if it is already taken
        if instance.text:
            return None

        #if it is an empty(available) cell
        instance.text = next(self.symbols)
        #instance.text = self.symbols.next()
        instance.font_size = 100
        if not self.is_finished():
            # HUMAN이 둔 후, 게임이 끝나지 않았으면 AI가 수를 둔다
            (r, c) = self.bot.play_move(self.grid)
            self.grid[r][c].text = next(self.symbols)
            self.grid[r][c].font_size = 100
            self.is_finished()

    def is_finished(self):
        winner = self.check_winner()

        if winner:
            content = BoxLayout(orientation='vertical')
            if winner == 'D' :
                content.add_widget(Label(text='Draw'))
            else:
                content.add_widget(Label(text='%s won the game!' % winner))
            restart_button = Button(text='Game restart!!')
            content.add_widget(restart_button)

            popup = Popup(title='Game Ends', content=content, auto_dismiss=False, size_hint=(.5,.5))
            popup.open()

            restart_button.bind(on_press=lambda *args: self.restart_board(popup, *args))
            return True
        else:
            return False

    def check_winner(self):
        for line in WINNING_LINES:
            row = []
            for cell in line:
                row.append(self.grid[cell[0]][cell[1]].text)

            for symbol in SYMBOLS:
                if all([s==symbol for s in row]):
                    return symbol  
        #game is on going
        for row in self.grid:
            for col in row:
                if col.text == '':
                    return None
        # Draw
        return 'D'

    def restart_board(self, *args):
        # print("args", args)
        args[0].dismiss()
        
        #clear board
        for row in self.grid:
            for col in row:
                col.text = ''

        #initialize symbol
        if next(self.symbols) =='O':
            return
        else:
            next(self.symbols)
            return

        self.init_players()

class TicTacToe(App):
    def build(self):
        self.board = Board()
        return self.board

if __name__ == '__main__':
    TicTacToe().run()  
