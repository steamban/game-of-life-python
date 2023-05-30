import gof 
import pytest

# Tests for create_board

def test_create_board_size():
    board = gof.create_board(3, 4)
    assert len(board) == 3
    assert len(board[0]) == 4
    
    