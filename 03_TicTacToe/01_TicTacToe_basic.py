import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button



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

    def draw_tiles(self):
        """
            Adds the tiles to the grid (widgets to the gridset)
        """
        for row in range(self.rows):
            for col in range(self.cols):
                tile = Button()
                tile.bind(on_press=self.on_click)
                self.grid[row][col] = tile
                self.add_widget(tile)

    def on_click(self, instance):
        """
            Handles a click on a tile
        """
        # print(instance)
        
        # if it is already taken
        if instance.text:
            return None

        #if it is an empty(available) cell
        instance.text = next(self.symbols)
        #instance.text = self.symbols.next()
        instance.font_size = 100


class TicTacToe(App):

    def build(self):
        self.board = Board()
        return self.board

if __name__ == '__main__':
    TicTacToe().run()  