"""Cyber Tic-Tac-Toe: a first-year Python portfolio project.

The game is deliberately self-contained and uses only the Python standard
library. It supports three AI difficulty levels and a simple score board.
"""

from __future__ import annotations

import random
from typing import Optional

EMPTY = " "
HUMAN = "X"
COMPUTER = "O"
BOARD_SIZE = 9
WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def new_board() -> list[str]:
    """Return a fresh empty board."""
    return [EMPTY] * BOARD_SIZE


def available_moves(board: list[str]) -> list[int]:
    """Return zero-based indexes that are still available."""
    return [index for index, cell in enumerate(board) if cell == EMPTY]


def winner(board: list[str]) -> Optional[str]:
    """Return the winning symbol, or None when there is no winner."""
    for a, b, c in WINNING_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board: list[str]) -> bool:
    """Return True when the board is full and nobody has won."""
    return winner(board) is None and not available_moves(board)


def game_over(board: list[str]) -> bool:
    """Return True when a game has a winner or is a draw."""
    return winner(board) is not None or is_draw(board)


def make_move(board: list[str], position: int, symbol: str) -> bool:
    """Place a symbol at a one-based position if the move is legal."""
    if symbol not in (HUMAN, COMPUTER):
        return False
    if position < 1 or position > BOARD_SIZE:
        return False
    index = position - 1
    if board[index] != EMPTY:
        return False
    board[index] = symbol
    return True


def render_board(board: list[str]) -> str:
    """Create a readable text representation of the board."""
    cells = [cell if cell != EMPTY else str(index + 1) for index, cell in enumerate(board)]
    return (
        f"\n {cells[0]} | {cells[1]} | {cells[2]}\n"
        "---+---+---\n"
        f" {cells[3]} | {cells[4]} | {cells[5]}\n"
        "---+---+---\n"
        f" {cells[6]} | {cells[7]} | {cells[8]}\n"
    )


def find_winning_move(board: list[str], symbol: str) -> Optional[int]:
    """Return a one-based winning move for symbol, if one exists."""
    for index in available_moves(board):
        board[index] = symbol
        wins = winner(board) == symbol
        board[index] = EMPTY
        if wins:
            return index + 1
    return None


def easy_move(board: list[str]) -> int:
    """Choose a random legal move."""
    return random.choice(available_moves(board)) + 1


def medium_move(board: list[str]) -> int:
    """Try to win, block the player, otherwise make a sensible move."""
    winning_move = find_winning_move(board, COMPUTER)
    if winning_move is not None:
        return winning_move

    blocking_move = find_winning_move(board, HUMAN)
    if blocking_move is not None:
        return blocking_move

    if board[4] == EMPTY:
        return 5

    corners = [index + 1 for index in (0, 2, 6, 8) if board[index] == EMPTY]
    if corners:
        return random.choice(corners)

    return easy_move(board)


def minimax(board: list[str], maximizing: bool) -> int:
    """Return the optimal minimax score for the current board."""
    result = winner(board)
    if result == COMPUTER:
        return 1
    if result == HUMAN:
        return -1
    if is_draw(board):
        return 0

    if maximizing:
        best_score = -2
        for index in available_moves(board):
            board[index] = COMPUTER
            best_score = max(best_score, minimax(board, False))
            board[index] = EMPTY
        return best_score

    best_score = 2
    for index in available_moves(board):
        board[index] = HUMAN
        best_score = min(best_score, minimax(board, True))
        board[index] = EMPTY
    return best_score


def hard_move(board: list[str]) -> int:
    """Choose the optimal move using minimax."""
    best_score = -2
    best_move = available_moves(board)[0]

    for index in available_moves(board):
        board[index] = COMPUTER
        score = minimax(board, False)
        board[index] = EMPTY
        if score > best_score:
            best_score = score
            best_move = index

    return best_move + 1


def computer_move(board: list[str], difficulty: str) -> int:
    """Select a computer move for the chosen difficulty."""
    if not available_moves(board):
        raise ValueError("No legal moves remain.")
    if difficulty == "easy":
        return easy_move(board)
    if difficulty == "medium":
        return medium_move(board)
    if difficulty == "hard":
        return hard_move(board)
    raise ValueError("Difficulty must be easy, medium or hard.")


def choose_difficulty() -> str:
    """Read a valid difficulty selection from the player."""
    options = {"1": "easy", "2": "medium", "3": "hard"}
    while True:
        print("\nChoose AI difficulty:")
        print("1. Easy   - random moves")
        print("2. Medium - attacks and blocks")
        print("3. Hard   - minimax AI")
        choice = input("Select 1-3: ").strip()
        if choice in options:
            return options[choice]
        print("Invalid selection. Please choose 1, 2 or 3.")


def play_round(difficulty: str) -> str:
    """Play one round and return 'human', 'computer' or 'draw'."""
    board = new_board()
    print(render_board(board))

    while not game_over(board):
        while True:
            raw = input("Your move (1-9): ").strip()
            if raw.isdigit() and make_move(board, int(raw), HUMAN):
                break
            print("Invalid move. Choose an empty position from 1 to 9.")

        print(render_board(board))
        if winner(board) == HUMAN:
            return "human"
        if is_draw(board):
            return "draw"

        move = computer_move(board, difficulty)
        make_move(board, move, COMPUTER)
        print(f"Cyber AI chose position {move}.")
        print(render_board(board))

        if winner(board) == COMPUTER:
            return "computer"
        if is_draw(board):
            return "draw"

    return "draw"


def main() -> None:
    """Run the game session."""
    scores = {"human": 0, "computer": 0, "draw": 0}

    print("=" * 40)
    print("        CYBER TIC-TAC-TOE")
    print("=" * 40)
    print("Defend the grid. Outsmart the Cyber AI.")

    difficulty = choose_difficulty()

    while True:
        result = play_round(difficulty)
        scores[result] += 1

        messages = {
            "human": "You secured the grid! You win.",
            "computer": "The Cyber AI breached the grid. Computer wins.",
            "draw": "The grid is locked. It's a draw.",
        }
        print(messages[result])
        print(
            f"Score — You: {scores['human']} | "
            f"AI: {scores['computer']} | Draws: {scores['draw']}"
        )

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Session terminated. Thanks for playing Cyber Tic-Tac-Toe!")
            break


if __name__ == "__main__":
    main()
