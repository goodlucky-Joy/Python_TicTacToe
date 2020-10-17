import time
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from random import randint

from randomai import Ai as Ai1
from rulebasedai import Ai as Ai2
#from minimaxai import Ai as Ai2


# checking winning case
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

    def __init__(self, cols=3, **kwargs):
        super(Board, self).__init__(**kwargs)

        self.cols = cols
        self.rows = cols
        self.symbols = symbol_generator()

        self.grid = [[None for col in range(self.cols)] for row in range(self.rows)]

        self.first_turn = None
        self.second_turn = None

        self.is_draw_tiles = False;
        self.init_players()

        Window.bind(on_keyboard = self.on_keyboard)
    
    def init_players(self):

        first_turn_symbol = SYMBOLS[randint(0,1)]
        if first_turn_symbol == 'X':
            self.first_turn = Ai1(SYMBOLS[0], self.grid)
            self.second_turn = Ai2(SYMBOLS[1], self.grid)
        else:
            self.first_turn = Ai2(SYMBOLS[0], self.grid)
            self.second_turn = Ai1(SYMBOLS[1], self.grid)

        print("Tic Tac Toe First Turn : ", self.first_turn.ai_type)

        start_content = BoxLayout(orientation='vertical')
        start_content.add_widget(Label(text='First Turn ( X ) : %s \nSecond Turn ( O ) : %s ' %(self.first_turn.ai_type, self.second_turn.ai_type)))
        
        start_button = Button(text='Game start!!')
        start_content.add_widget(start_button)
        start_popup = Popup(title='Tic Tac Toe', content=start_content, auto_dismiss=False, size_hint=(.5,.5))
        start_popup.open()
        start_button.bind(on_press=lambda *args: self.draw_tiles(start_popup, *args))

    def draw_tiles(self, *args):
        args[0].dismiss()
        """
            Adds the tiles to the grid (widgets to the gridset)
        """
        if self.is_draw_tiles == False:
            for row in range(self.rows):
                for col in range(self.cols):
                    tile = Button()
                    self.grid[row][col] = tile
                    self.add_widget(tile)
            self.is_draw_tiles = True
    
    def on_keyboard(self, instance, key, scancode, codepoint, modifiers):
        # Clicked space bar
        if key == 32: 
            print ("space bar clicked")

            (r, c) = self.first_turn.play_move(self.grid)
            self.grid[r][c].text = next(self.symbols)
            self.grid[r][c].font_size = 100
            
            if not self.is_finished():
                (r, c) = self.second_turn.play_move(self.grid)
                self.grid[r][c].text = next(self.symbols)
                self.grid[r][c].font_size = 100
                self.is_finished()

    def is_finished(self):
        winner = self.check_winner()  # winning symbol(O/X), 'D' or None

        if winner:
            content = BoxLayout(orientation='vertical')
            if winner == 'D' :
                content.add_widget(Label(text='Draw'))
            elif winner == self.first_turn.symbol:
                content.add_widget(Label(text='%s (%s) won the game!' % (self.first_turn.ai_type, winner)))
            else:
                content.add_widget(Label(text='%s (%s) won the game!' % (self.second_turn.ai_type, winner)))
        
            restart_button = Button(text='Game restart!!')
            content.add_widget(restart_button)

            popup = Popup(title='Game Ends', content=content, auto_dismiss=False)
            popup.open()
            restart_button.bind(on_press=lambda *args: self.restart_board(popup, *args))
            return True
        else:
            return False

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
        if next(self.symbols) !='O':
            next(self.symbols)

        self.init_players()

class TicTacToe(App):
    def build(self):
        self.board = Board(cols=3)
        return self.board

if __name__ == '__main__':
    TicTacToe().run()  
