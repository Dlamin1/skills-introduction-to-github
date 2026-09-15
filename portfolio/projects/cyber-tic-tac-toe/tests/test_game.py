import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cyber_tic_tac_toe import (  # noqa: E402
    COMPUTER,
    EMPTY,
    HUMAN,
    available_moves,
    computer_move,
    find_winning_move,
    game_over,
    is_draw,
    make_move,
    new_board,
    winner,
)


def test_new_board_is_empty():
    board = new_board()
    assert len(board) == 9
    assert board == [EMPTY] * 9


def test_make_move_accepts_legal_move():
    board = new_board()
    assert make_move(board, 1, HUMAN) is True
    assert board[0] == HUMAN


def test_make_move_rejects_occupied_position():
    board = new_board()
    make_move(board, 1, HUMAN)
    assert make_move(board, 1, COMPUTER) is False
    assert board[0] == HUMAN


def test_make_move_rejects_invalid_position():
    board = new_board()
    assert make_move(board, 0, HUMAN) is False
    assert make_move(board, 10, HUMAN) is False


def test_horizontal_winner():
    board = [HUMAN, HUMAN, HUMAN, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
    assert winner(board) == HUMAN


def test_diagonal_winner():
    board = [COMPUTER, EMPTY, EMPTY, EMPTY, COMPUTER, EMPTY, EMPTY, EMPTY, COMPUTER]
    assert winner(board) == COMPUTER


def test_draw_detection():
    board = [
        HUMAN, COMPUTER, HUMAN,
        HUMAN, COMPUTER, COMPUTER,
        COMPUTER, HUMAN, HUMAN,
    ]
    assert winner(board) is None
    assert is_draw(board) is True
    assert game_over(board) is True


def test_available_moves():
    board = [HUMAN, EMPTY, COMPUTER, EMPTY, EMPTY, HUMAN, EMPTY, COMPUTER, EMPTY]
    assert available_moves(board) == [1, 3, 4, 6, 8]


def test_find_winning_move():
    board = [HUMAN, HUMAN, EMPTY, EMPTY, COMPUTER, EMPTY, EMPTY, EMPTY, COMPUTER]
    assert find_winning_move(board, HUMAN) == 3


def test_medium_ai_blocks_player():
    board = [HUMAN, HUMAN, EMPTY, EMPTY, COMPUTER, EMPTY, EMPTY, EMPTY, EMPTY]
    assert computer_move(board, "medium") == 3


def test_medium_ai_takes_winning_move():
    board = [COMPUTER, COMPUTER, EMPTY, HUMAN, HUMAN, EMPTY, EMPTY, EMPTY, EMPTY]
    assert computer_move(board, "medium") == 3


def test_hard_ai_takes_immediate_win():
    board = [COMPUTER, COMPUTER, EMPTY, HUMAN, HUMAN, EMPTY, EMPTY, EMPTY, EMPTY]
    assert computer_move(board, "hard") == 3
