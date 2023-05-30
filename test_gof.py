import gof
import pytest


# Tests for create_board

def test_create_board_size():
    board = gof.create_board(3, 4)
    assert len(board) == 3
    assert len(board[0]) == 4


def test_create_board_initialize_to_zero():
    board = gof.create_board(2, 4)
    for i in range(2):
        for j in range(2):
            assert board[i][j] == 0

##