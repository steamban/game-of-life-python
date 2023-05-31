import random


# create a board and initialize with random 1s and 0s
def create_board(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]


# display board
def display_board(game_board):
    board = ""
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            board += f"{game_board[i][j]} "
        board += "\n"

    return board


# return number of live neighbours for each cell
def count_live_neighbors(grid, row, col):
    live_neighbor_count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if (i == row and j == col) or i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                continue
            if grid[i][j] == 1:
                live_neighbor_count += 1
    return live_neighbor_count


# update board
def update_board(board):
    rows = len(board)
    cols = len(board[0])
    updated_board = create_board(rows, cols)
    for i in range(rows):
        for j in range(cols):
            live_neighbors = count_live_neighbors(board, i, j)
            if board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    updated_board[i][j] = 0
                else:
                    updated_board[i][j] = 1
            else:
                if live_neighbors == 3:
                    updated_board[i][j] = 1
                else:
                    updated_board[i][j] = 0
    return updated_board


if __name__ == "__main__":
    # initialise board
    rows = 8
    cols = 8
    board = create_board(rows, cols)
    print(display_board(board))
    
    # while True:
        
