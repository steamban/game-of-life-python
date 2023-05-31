import gof
import pytest


# Tests for create_board

def test_create_board_size():
    board = gof.create_board(3, 4)
    assert len(board) == 3
    assert len(board[0]) == 4

def test_create_board_type_error():
    with pytest.raises(TypeError):
        gof.create_board('a', 'b')

def test_create_board_value_error():
    board = gof.create_board((-3), -4)
    assert len(board) == 0
    assert len(board[0]) == 0
    
##

# Tests for display_board

def test_display_board_empty_board():
    board = gof.create_board(2, 4)
    assert gof.display_board(board) == """0 0 0 0 
0 0 0 0 
"""

##

