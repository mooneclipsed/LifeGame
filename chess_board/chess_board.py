from chess_board.cell import Cell


class ChessBoard:
    def __init__(self):
        self.length = 20
        self.cells = [[Cell() for i in range(self.length)] for i in range(self.length)]

    def update(self):
        """update the whole chessboard and the status of the cell"""
        pass

    def show_cell_status(self):
        for i in range(self.length):
            raw=[]
            for j in range(self.length):
                if self.cells[i][j].status:
                    print('*\t', end='')
                else:
                    print(' \t', end='')
            print('\n')

# [[Cell() for i in range(10)] for i in range(10)]