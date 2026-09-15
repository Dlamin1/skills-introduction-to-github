# Cyber Tic-Tac-Toe

A beginner-friendly Python game developed as a first-year Computer Science portfolio project.

## Overview

Cyber Tic-Tac-Toe is a command-line Tic-Tac-Toe game where the player competes against a computer opponent. The project adds a simple cybersecurity theme while keeping the implementation appropriate for introductory programming.

## Learning Objectives

This project demonstrates:

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists
- Input validation
- Randomisation
- Basic game-state management
- Modular Python code
- Automated testing

## Features

- Human vs computer gameplay
- Three difficulty levels: Easy, Medium and Hard
- Random computer moves on Easy
- Basic defensive/offensive strategy on Medium
- Minimax-based optimal play on Hard
- Score tracking during a session
- Replay support
- Input validation
- Cybersecurity-themed interface

## Project Structure

```text
cyber-tic-tac-toe/
├── README.md
├── requirements.txt
├── src/
│   └── cyber_tic_tac_toe.py
└── tests/
    └── test_game.py
```

## Requirements

- Python 3.10+
- No external packages are required to play the game.
- `pytest` is required only for the automated tests.

## Run the Game

From this project directory:

```bash
python src/cyber_tic_tac_toe.py
```

## Run Tests

Install pytest if necessary:

```bash
python -m pip install pytest
```

Then run:

```bash
pytest
```

## Game Controls

- Choose a difficulty level from 1–3.
- Enter a board position from 1–9.
- Position 1 is the top-left square and position 9 is the bottom-right square.
- Complete three symbols in a row, column or diagonal to win.

## Academic Context

**Programme:** BSc Computer Science with Electronics  
**Institution:** North-West University  
**Portfolio level:** First-year / introductory programming project

This project is intentionally scoped to demonstrate foundational programming concepts rather than advanced software engineering.

## Author

**Sduduzo Bhekani Gumede**  
GitHub: [@Dlamin1](https://github.com/Dlamin1)
