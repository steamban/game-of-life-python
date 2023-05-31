# create a board
def create_board(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


# display board
def display_board(game_board):
    board = ""
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            board += f"{game_board[i][j]} "
        board += "\n"
    
    return board


# TODO
# initialise it with alive cells at random positions
# keep track of neighbors each cell has, pass coordinates of cell and the board
# update board
# def update_board(board):
#     rows = len(board)
#     cols = len(board[0])
#     updated_board = create_board(rows, cols)
#     for i in range(rows):
#         for j in range(cols):
#             live_neighbors = count_live_neighbors(board, i, j)
#             if board[i][j] == 1:
#                 if live_neighbors < 2 or live_neighbors > 3:
#                     updated_board[i][j] = 0
#                 else:
#                     updated_board[i][j] = 1
#             else:
#                 if live_neighbors == 3:
#                     updated_board[i][j] = 1
#                 else:
#                     updated_board[i][j] = 0
#     return updated_board

if __name__ == "__main__":
    # initialise board
    rows = 4
    cols = 5
    board = create_board(rows, cols)
    display_board(board)
