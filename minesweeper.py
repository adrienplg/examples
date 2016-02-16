from random import randrange
from collections import deque

class Game(object):

    def __init__(self):
        self.rows = 9
        self.columns = 9
        self.density = 20

    def initialize(self):
        self.board = Board(self.rows, self.columns, self.density)
        self.game_status = 'RUNNING'

    def start(self):
        while self.game_status == 'RUNNING':
            self.print_user_board()

            coord_y = input('Enter X:\n')
            try:
                coord_y = int(coord_y)
            except ValueError:
                print('X must be between 0 and {}'.format(self.columns))
                continue
            if not 0 < coord_y <= self.columns:
                print('X must be between 0 and {}'.format(self.columns))
                continue

            coord_x = input('Enter Y:\n')
            try:
                coord_x = int(coord_x)
            except ValueError:
                print('Y must be between 0 and {}'.format(self.rows))
                continue
            if not 0 < coord_x <= self.rows:
                print('Y must be between 0 and {}'.format(self.rows))
                continue

            flag = input('Flag it? (y or f for yes):\n')
            flag = True if flag == 'y' or flag == 'f' else False
            if flag:
                self.flag_cell(coord_x - 1, coord_y - 1)
            else:
                self.flip_cell(coord_x - 1, coord_y - 1)
            self.check_win()

        if self.game_status == 'LOST':
            self.print_user_board()
            print('--------------------------------')
            print('-------- YOU LOST! :\'( --------')
            print('--------------------------------')


        elif self.game_status == 'WON':
            self.print_user_board()
            self.print_full_board()
            print('--------------------------------')
            print('-- YOU WON!! Congratulations! --')
            print('--------------------------------')

        else:
            print('Unexpected state')

        self.ask_play_again()

    def ask_play_again(self):
        onemore = input('Play again? (y/n):\n')
        if onemore == 'y':
            self.initialize()
            self.start()
        else:
            quit()

    def check_win(self):
        #print('Remaining number of cells to reveal:', self.board.n_cells_toreveal)
        if self.board.n_cells_toreveal == 0:
            self.game_status = 'WON'

    def flip_cell(self, x, y):
        cell = self.board.cells[x][y]
        # Only decrease n_cells_toreveal if the cell has not been revealed yet
        cell.is_flagged = False # Remove the flag if any
        if not cell.revealed:
            cell.revealed = True
            self.board.n_cells_toreveal -= 1
        if cell.is_bomb:
            self.game_status = 'LOST'
        elif cell.value == 0:
            self.board.expand_blank(cell)

    def flag_cell(self, x, y):
        cell = self.board.cells[x][y]
        if not cell.revealed:
            cell.is_flagged = True

    def print_user_board(self):
        print('--------- GAME BOARD --------')
        print('    ' + '  '.join([str(index + 1) for index in range(len(game.board.cells[0]))]))
        print('   ' + ''.join(['___' for index in range(len(game.board.cells[0]))]))
        print ('\n'.join([str(index + 1) + ' | ' + '  '.join([cell.display() for cell in row]) for index, row in enumerate(game.board.cells)]))

    def print_full_board(self):
        print('--------- DEV BOARD ---------')
        print('    ' + '  '.join([str(index + 1) for index in range(len(game.board.cells[0]))]))
        print('   ' + ''.join(['___' for index in range(len(game.board.cells[0]))]))
        print ('\n'.join([str(index + 1) + ' | ' + '  '.join([cell.display(True) for cell in row]) for index, row in enumerate(game.board.cells)]))

class Board(object):

    def __init__(self, rows, columns, density):
        """
        Args:
            rows (int): number of rows
            columns (int): number of columns
            density (int): mine density of the board (in percentage)
        """

        self.rows = rows
        self.columns = columns
        self.density = density
        self.n_bombs = int((rows * columns) * (self.density / 100))
        self.n_cells_toreveal = self.rows * self.columns - self.n_bombs
        self.cells = [ [Cell(i,j) for j in range(columns)] for i in range(rows) ]
        self.bombs = []
        self.place_mines()
        self.shuffle_board()
        self.set_numbered_cells()

        #print('nb of bombs:', self.n_bombs)
        #print('nb of other cells:', self.n_cells_toreveal)

    def place_mines(self):
        local_n_bombs = self.n_bombs
        for i in range(len(self.cells)): # Iterates on rows
            for j in range(len(self.cells[0])): # Iterates on columns
                self.cells[i][j].is_bomb = True
                self.bombs.append(self.cells[i][j]) # Add the cell to the list of bombs
                local_n_bombs -= 1
                if local_n_bombs == 0: # All mines are placed
                    return

    def shuffle_board(self):
        for i in range(len(self.cells)): # Iterates on rows
            for j in range(len(self.cells[0])): # Iterates on columns
                rand_i = randrange(self.rows)
                rand_j = randrange(self.columns)
                #print('rand_i, rand_j: {}, {}'.format(rand_i, rand_j))
                if i != rand_i and j != rand_j:
                    temp_cell = self.cells[rand_i][rand_j]
                    self.cells[rand_i][rand_j] = self.cells[i][j]
                    self.cells[rand_i][rand_j].row = rand_i
                    self.cells[rand_i][rand_j].column = rand_j
                    self.cells[i][j] = temp_cell
                    self.cells[i][j].row = i
                    self.cells[i][j].column = j

    def set_numbered_cells(self):
        deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)] # Offsets of 8 surrounding cells
        for bomb in self.bombs:
            #print('bomb:{},{}'.format(bomb.row,bomb.column))
            for delta in deltas:
                current_row = bomb.row + delta[0]
                current_column = bomb.column + delta[1]
                if current_row > -1 and current_column > -1:
                    try:
                        self.cells[current_row][current_column].value += 1
                        #print('cell:{},{}'.format(bomb.row + delta[0],bomb.column + delta[1]))
                    except IndexError:
                        pass


    def expand_blank(self, cell):
        deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)] # Offsets of 8 surrounding cells
        queue = deque() # Queue holding the current blank cell and all surrounding blank cells
        visited_cells = [] # List holding the visited cells
        queue.append(cell) # Add the current blank cell to the empty queue
        while queue:
            current_blank = queue.popleft()
            for delta in deltas:
                surround_row = current_blank.row + delta[0]
                surrounding_col = current_blank.column + delta[1]
                if surround_row > -1 and surrounding_col > -1:
                    try:
                        surrounding_cell = self.cells[surround_row][surrounding_col]
                        if not surrounding_cell.revealed: # Prevents from decreasing the counter more than once for the same cell
                            surrounding_cell.revealed = True
                            self.n_cells_toreveal -= 1
                        if surrounding_cell.value == 0 and surrounding_cell not in visited_cells:
                            queue.append(surrounding_cell)
                            visited_cells.append(surrounding_cell)
                    except IndexError:
                            pass

class Cell(object):

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.is_bomb = False
        self.is_flagged = False
        self.value = 0
        self.revealed = False

    def display(self, reveal_all=False):
        if self.is_flagged and self.is_bomb and reveal_all:
            return 'X'
        elif self.is_flagged and not reveal_all:
            return 'F'
        elif self.is_bomb and (reveal_all or self.revealed):
            return '@'
        elif self.revealed or reveal_all:
            return str(self.value)
        else:
            return '_'

    def __repr__(self):
        return '{}(value:{}, is_bomb:{}, is_flagged:{})'.format(self.__class__.__name__, self.value, self.is_bomb, self.is_flagged)


if __name__ == '__main__':
    game = Game()
    game.initialize()
    game.start()






