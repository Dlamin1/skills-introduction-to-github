# Cyber Tic-Tac-Toe

A polished Python Tic-Tac-Toe game developed as a first-year Computer Science portfolio project. It now includes both a command-line interface and a desktop **Tkinter graphical interface** while sharing the same tested game engine.

## Overview

Cyber Tic-Tac-Toe is a cybersecurity-themed strategy game where the player competes against a computer opponent. The project intentionally demonstrates first-year programming fundamentals while introducing a clean separation between **game logic** and **user interface**.

## Features

- 🖥️ Polished Tkinter desktop interface
- 🎮 Human vs computer gameplay
- 🤖 Three AI difficulty levels
  - Easy — random legal moves
  - Medium — attacks, blocks and prioritises useful positions
  - Hard — minimax-based optimal play
- 🏆 Session score tracking
- 🔄 New-round support
- 🛡️ Cybersecurity-themed status messages
- 🎨 Responsive hover and winner highlighting
- ❌ Input/move validation
- 🧪 Automated tests with pytest
- 🧩 Shared game engine used by both CLI and GUI

## Architecture

The project separates presentation from game logic:

```text
                 ┌─────────────────────┐
                 │   Game Engine       │
                 │  cyber_tic_tac_toe  │
                 └──────────┬──────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
      ┌───────▼────────┐        ┌────────▼─────────┐
      │ Command Line   │        │ Tkinter Desktop  │
      │ Interface      │        │ Interface        │
      └────────────────┘        └──────────────────┘
```

The GUI does **not** duplicate the AI or board rules. It imports the existing engine, making the project easier to test and maintain.

## Project Structure

```text
cyber-tic-tac-toe/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── cyber_tic_tac_toe.py
│   └── cyber_tic_tac_toe_gui.py
└── tests/
    ├── test_game.py
    └── test_gui_helpers.py
```

## Requirements

- Python 3.10+
- Tkinter — normally included with standard Python installations
- `pytest` — required for automated tests

No third-party package is required to run the actual game.

## Run the Graphical Version

From the project directory:

```bash
python src/cyber_tic_tac_toe_gui.py
```

## Run the Command-Line Version

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

The tests cover board creation, legal moves, winners, draws, AI decisions and safe GUI-module importing.

## AI Difficulty

| Level | Behaviour |
|---|---|
| Easy | Selects a random legal move |
| Medium | Attempts to win, blocks the player, then chooses strategic positions |
| Hard | Uses minimax to select an optimal move |

## Learning Objectives

This project demonstrates:

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists
- Input validation
- Randomisation
- Game-state management
- Modular Python code
- Basic algorithmic reasoning
- Minimax decision-making
- GUI programming with Tkinter
- Automated testing
- Separation of concerns

## Academic Context

**Programme:** BSc Computer Science with Electronics  
**Institution:** North-West University  
**Portfolio level:** First-year / introductory programming project

The project remains intentionally appropriate for an introductory portfolio, while the GUI upgrade demonstrates progression from console programming into event-driven desktop application development.

## Author

**Sduduzo Bhekani Gumede**  
GitHub: [@Dlamin1](https://github.com/Dlamin1)
