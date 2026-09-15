"""Tkinter graphical interface for Cyber Tic-Tac-Toe.

The board rules, AI and scoring are imported from the existing game module so
that the GUI remains a presentation layer rather than duplicating game logic.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

from cyber_tic_tac_toe import (
    COMPUTER,
    HUMAN,
    computer_move,
    game_over,
    make_move,
    new_board,
    winner,
)


class CyberTicTacToeApp:
    """Polished desktop interface for Cyber Tic-Tac-Toe."""

    BG = "#0b1020"
    PANEL = "#121a2d"
    CELL = "#17213a"
    CELL_HOVER = "#223255"
    TEXT = "#f5f7ff"
    MUTED = "#9aa8c7"
    ACCENT = "#5eead4"
    HUMAN_COLOR = "#60a5fa"
    AI_COLOR = "#f472b6"
    WIN_COLOR = "#22c55e"

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Cyber Tic-Tac-Toe")
        self.root.geometry("560x720")
        self.root.minsize(500, 650)
        self.root.configure(bg=self.BG)

        self.board = new_board()
        self.difficulty = tk.StringVar(value="medium")
        self.status = tk.StringVar(value="Your turn — choose a cell")
        self.score_vars = {
            "human": tk.IntVar(value=0),
            "computer": tk.IntVar(value=0),
            "draw": tk.IntVar(value=0),
        }
        self.buttons: list[tk.Button] = []
        self.game_active = True

        self._configure_styles()
        self._build_ui()
        self._new_round()

    def _configure_styles(self) -> None:
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure(
            "Cyber.TCombobox",
            fieldbackground=self.CELL,
            background=self.CELL,
            foreground=self.TEXT,
            arrowcolor=self.ACCENT,
        )
        style.configure(
            "Cyber.TButton",
            background=self.ACCENT,
            foreground="#06111c",
            font=("TkDefaultFont", 10, "bold"),
            padding=(14, 8),
        )

    def _build_ui(self) -> None:
        header = tk.Frame(self.root, bg=self.BG)
        header.pack(fill="x", padx=28, pady=(24, 12))

        tk.Label(
            header,
            text="CYBER TIC-TAC-TOE",
            bg=self.BG,
            fg=self.ACCENT,
            font=("TkDefaultFont", 24, "bold"),
        ).pack(anchor="w")
        tk.Label(
            header,
            text="DEFEND THE GRID • OUTSMART THE CYBER AI",
            bg=self.BG,
            fg=self.MUTED,
            font=("TkDefaultFont", 9, "bold"),
        ).pack(anchor="w", pady=(3, 0))

        controls = tk.Frame(self.root, bg=self.PANEL, padx=16, pady=12)
        controls.pack(fill="x", padx=28, pady=8)

        tk.Label(
            controls,
            text="AI DIFFICULTY",
            bg=self.PANEL,
            fg=self.MUTED,
            font=("TkDefaultFont", 9, "bold"),
        ).pack(side="left")

        difficulty = ttk.Combobox(
            controls,
            textvariable=self.difficulty,
            values=("easy", "medium", "hard"),
            state="readonly",
            width=12,
            style="Cyber.TCombobox",
        )
        difficulty.pack(side="left", padx=(10, 20))
        difficulty.bind("<<ComboboxSelected>>", self._difficulty_changed)

        ttk.Button(
            controls,
            text="NEW ROUND",
            command=self._new_round,
            style="Cyber.TButton",
        ).pack(side="right")

        status_panel = tk.Frame(self.root, bg=self.PANEL, padx=16, pady=12)
        status_panel.pack(fill="x", padx=28, pady=8)
        tk.Label(
            status_panel,
            textvariable=self.status,
            bg=self.PANEL,
            fg=self.TEXT,
            font=("TkDefaultFont", 11, "bold"),
        ).pack()

        board_frame = tk.Frame(self.root, bg=self.BG)
        board_frame.pack(padx=28, pady=18)

        for index in range(9):
            button = tk.Button(
                board_frame,
                text="",
                width=5,
                height=2,
                bg=self.CELL,
                activebackground=self.CELL_HOVER,
                fg=self.TEXT,
                activeforeground=self.TEXT,
                relief="flat",
                bd=0,
                highlightthickness=1,
                highlightbackground="#263553",
                font=("TkDefaultFont", 25, "bold"),
                cursor="hand2",
                command=lambda i=index: self._human_move(i),
            )
            row, column = divmod(index, 3)
            button.grid(row=row, column=column, padx=5, pady=5, ipadx=14, ipady=10)
            button.bind("<Enter>", lambda event, b=button: self._hover(b, True))
            button.bind("<Leave>", lambda event, b=button: self._hover(b, False))
            self.buttons.append(button)

        score_panel = tk.Frame(self.root, bg=self.PANEL, padx=18, pady=14)
        score_panel.pack(fill="x", padx=28, pady=8)

        self._score_card(score_panel, "YOU", "human", self.HUMAN_COLOR).pack(side="left", expand=True)
        self._score_card(score_panel, "CYBER AI", "computer", self.AI_COLOR).pack(side="left", expand=True)
        self._score_card(score_panel, "DRAWS", "draw", self.MUTED).pack(side="left", expand=True)

        footer = tk.Label(
            self.root,
            text="Python • Tkinter • Minimax AI • First-Year Portfolio Project",
            bg=self.BG,
            fg=self.MUTED,
            font=("TkDefaultFont", 8),
        )
        footer.pack(pady=(8, 18))

    def _score_card(self, parent: tk.Frame, title: str, key: str, color: str) -> tk.Frame:
        frame = tk.Frame(parent, bg=self.PANEL)
        tk.Label(
            frame,
            text=title,
            bg=self.PANEL,
            fg=color,
            font=("TkDefaultFont", 8, "bold"),
        ).pack()
        tk.Label(
            frame,
            textvariable=self.score_vars[key],
            bg=self.PANEL,
            fg=self.TEXT,
            font=("TkDefaultFont", 18, "bold"),
        ).pack(pady=(2, 0))
        return frame

    def _hover(self, button: tk.Button, entering: bool) -> None:
        if button["state"] == "disabled":
            return
        button.configure(bg=self.CELL_HOVER if entering else self.CELL)

    def _difficulty_changed(self, _event: object) -> None:
        self.status.set(f"Difficulty set to {self.difficulty.get().title()} — new round ready")
        self._new_round()

    def _new_round(self) -> None:
        self.board = new_board()
        self.game_active = True
        self.status.set("Your turn — choose a cell")
        for button in self.buttons:
            button.configure(text="", state="normal", bg=self.CELL, fg=self.TEXT)

    def _human_move(self, index: int) -> None:
        if not self.game_active or self.board[index] != " ":
            return

        make_move(self.board, index + 1, HUMAN)
        self._refresh_board()

        if self._finish_if_needed():
            return

        self.status.set("Cyber AI is analysing the grid…")
        self.root.after(220, self._computer_turn)

    def _computer_turn(self) -> None:
        if not self.game_active:
            return

        move = computer_move(self.board, self.difficulty.get())
        make_move(self.board, move, COMPUTER)
        self._refresh_board()

        if self._finish_if_needed():
            return
        self.status.set("Your turn — choose a cell")

    def _refresh_board(self) -> None:
        for index, value in enumerate(self.board):
            if value == " ":
                continue
            self.buttons[index].configure(
                text=value,
                state="disabled",
                fg=self.HUMAN_COLOR if value == HUMAN else self.AI_COLOR,
                bg=self.CELL,
            )

    def _finish_if_needed(self) -> bool:
        result = winner(self.board)
        if result is None and not game_over(self.board):
            return False

        self.game_active = False
        for button in self.buttons:
            button.configure(state="disabled")

        if result == HUMAN:
            self.score_vars["human"].set(self.score_vars["human"].get() + 1)
            self.status.set("SYSTEM SECURED — YOU WIN")
            self._highlight_winner(HUMAN)
            messagebox.showinfo("Grid Secured", "You defeated the Cyber AI!")
        elif result == COMPUTER:
            self.score_vars["computer"].set(self.score_vars["computer"].get() + 1)
            self.status.set("SECURITY BREACH — CYBER AI WINS")
            self._highlight_winner(COMPUTER)
            messagebox.showinfo("Security Breach", "The Cyber AI captured the grid.")
        else:
            self.score_vars["draw"].set(self.score_vars["draw"].get() + 1)
            self.status.set("GRID LOCKED — DRAW")
            messagebox.showinfo("Grid Locked", "No winner this round.")

        return True

    def _highlight_winner(self, symbol: str) -> None:
        winning_lines = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
        )
        for line in winning_lines:
            if all(self.board[index] == symbol for index in line):
                for index in line:
                    self.buttons[index].configure(bg=self.WIN_COLOR, fg="#07110a")
                break


def main() -> None:
    root = tk.Tk()
    CyberTicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
