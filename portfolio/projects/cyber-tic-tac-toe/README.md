# Cyber Tic-Tac-Toe

A polished Python Tic-Tac-Toe game developed as a first-year Computer Science portfolio project. It includes a command-line interface and a desktop **Tkinter graphical interface** while sharing the same tested game engine.

## Demo

> **Gameplay demo:** Record a 45–90 second walkthrough using the guide in [`docs/DEMO_GUIDE.md`](docs/DEMO_GUIDE.md). Add the final video link here once it has been uploaded.

**Suggested demo flow:** launch the application → show the three difficulty levels → play several moves → show the Cyber AI response → finish a round → show the updated scoreboard.

### Demo Captions

- **Figure 1 — Main interface:** Cyber Tic-Tac-Toe desktop interface with the interactive game board, difficulty selector and scoreboard.
- **Figure 2 — Difficulty selection:** The player can choose Easy, Medium or Hard AI before starting a round.
- **Figure 3 — Active gameplay:** The player and Cyber AI alternate moves while the status panel communicates the current game state.
- **Figure 4 — Result state:** A completed round highlights the winning line and updates the session scoreboard.

## Screenshots

Add polished screenshots after running the GUI locally. Keep each image focused on one feature and crop out unrelated desktop content.

Recommended layout:

```text
cyber-tic-tac-toe/
└── docs/
    └── media/
        ├── main-interface.png
        ├── difficulty-selection.png
        ├── gameplay.png
        └── result-screen.png
```

Then embed them in this README as follows:

```markdown
![Figure 1 — Main interface](docs/media/main-interface.png)
*Figure 1 — Main interface showing the Cyber Tic-Tac-Toe board, difficulty selector and scoreboard.*

![Figure 2 — Difficulty selection](docs/media/difficulty-selection.png)
*Figure 2 — Difficulty selection showing Easy, Medium and Hard AI modes.*

![Figure 3 — Active gameplay](docs/media/gameplay.png)
*Figure 3 — Active gameplay with player and Cyber AI moves visible.*

![Figure 4 — Result screen](docs/media/result-screen.png)
*Figure 4 — Completed round with the result and updated score.*
```

**Screenshot standard:** use a clean 16:9 or 4:3 capture, keep the complete game window visible, and avoid showing private desktop information.

## Overview

Cyber Tic-Tac-Toe is a cybersecurity-themed strategy game where the player competes against a computer opponent. The project demonstrates first-year programming fundamentals while introducing a clean separation between **game logic** and **user interface**.

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
├── docs/
│   └── DEMO_GUIDE.md
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

## Recording the Demo

See [`docs/DEMO_GUIDE.md`](docs/DEMO_GUIDE.md) for the complete recording checklist and suggested narration.

For a professional portfolio demo, aim for **45–90 seconds** and show:

1. The application opening.
2. The AI difficulty selector.
3. Several moves and an AI response.
4. A completed round.
5. The updated scoreboard.

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
