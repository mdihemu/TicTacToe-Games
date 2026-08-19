# Tic-Tac-Toe Game – Version 2.1

A command-line **Tic-Tac-Toe game built with Python**.  
This updated version includes Player vs Computer, Player vs Player, multiple AI difficulty levels, a scoreboard, match history, replay support, and a Minimax-based hard mode.

## Default Players

- **Player 1:** Imran
- **Player 2:** Emu

In **Player vs Computer** mode, Imran plays against the computer.

## Features

- Imran vs Computer
- Imran vs Emu
- Default player names
- Choose `X` or `O`
- Symbol selection only once per game session
- Easy, Medium, and Hard computer difficulty
- Scoreboard
- Match history
- Replay system
- Input validation
- Winning combination detection
- Position guide
- Hard AI using the Minimax algorithm
- Clean menu-based command-line interface

## Requirements

- Python 3.x

No external Python packages are required.

## How to Run

1. Clone or download this repository.
2. Open a terminal or command prompt inside the project folder.
3. Run:

```bash
python tic_tac_toe.py
```

If your Python installation uses `python3`, run:

```bash
python3 tic_tac_toe.py
```

## Main Menu

When the program starts, the menu looks like this:

```text
=============================================
      TIC-TAC-TOE GAME - VERSION 2.1
=============================================
1. Imran vs Computer
2. Imran vs Emu
3. View Scoreboard
4. View Match History
5. Show Position Guide
6. Exit
=============================================
```

## Board Positions

Use the numbers `1` to `9` to choose a position.

```text
     |     |
  1  |  2  |  3
_____|_____|_____
     |     |
  4  |  5  |  6
_____|_____|_____
     |     |
  7  |  8  |  9
     |     |
```

## Game Modes

### 1. Imran vs Computer

Imran plays against the computer.

At the beginning of the game session:

1. Imran selects `X` or `O`.
2. The computer automatically receives the other symbol.
3. Imran selects a difficulty level.
4. The same symbol and difficulty remain active while continuing to replay in that session.

`X` always makes the first move.

### 2. Imran vs Emu

Two human players play against each other.

- Imran chooses `X` or `O`.
- Emu automatically receives the other symbol.
- The selected symbols remain unchanged while replaying in the same session.
- `X` always starts first.

## Computer Difficulty Levels

### Easy

The computer selects a random available position.

This mode is suitable for beginners.

### Medium

The computer uses a basic strategy:

1. Try to make a winning move.
2. Block Imran if Imran can win on the next move.
3. Take the center position if available.
4. Take a corner if available.
5. Take an edge if necessary.

### Hard

The computer uses the **Minimax Algorithm**.

The algorithm evaluates possible future game states and selects one of the best available moves. This makes the computer significantly harder to defeat.

## Scoreboard

The game keeps track of:

- Imran wins
- Emu wins
- Computer wins
- Draws

Example:

```text
=============================================
SCOREBOARD
=============================================
Imran Wins    : 2
Emu Wins      : 1
Computer Wins : 3
Draws         : 2
=============================================
```

The scoreboard remains available while the program is running.

## Match History

Every completed match is stored in the match history.

Example:

```text
=============================================
MATCH HISTORY
=============================================
1. Imran defeated Computer (Easy Mode).
2. Computer defeated Imran (Hard Mode).
3. Imran vs Emu - Draw.
=============================================
```

Match history is stored only during the current program session.

## Replay System

After a match finishes, the program asks:

```text
Continue playing? (Y/N):
```

If you enter `Y`:

- The board is reset.
- A new match begins.
- The current symbols remain unchanged.
- In Computer mode, the selected difficulty also remains unchanged.

The game does **not** ask for the symbol again during the same game session.

If you enter `N`, you return to the main menu.

## Winning Combination Detection

The program checks all eight possible winning combinations:

### Horizontal

- `1 → 2 → 3`
- `4 → 5 → 6`
- `7 → 8 → 9`

### Vertical

- `1 → 4 → 7`
- `2 → 5 → 8`
- `3 → 6 → 9`

### Diagonal

- `1 → 5 → 9`
- `3 → 5 → 7`

When someone wins, the winning positions are displayed.

Example:

```text
=============================================
Imran WON THE MATCH!
Winning Positions: 1 -> 5 -> 9
Congratulations, Imran!
=============================================
```

## Input Validation

The game handles common invalid inputs, including:

- Entering a position outside `1-9`
- Entering text instead of a number
- Selecting an occupied position
- Entering an invalid symbol
- Entering an invalid menu option
- Entering an invalid replay response

## Main Functions

| Function | Purpose |
|---|---|
| `reset_board()` | Clears the board before a new match |
| `print_board()` | Displays the current board |
| `print_position_guide()` | Shows position numbers |
| `get_player_move()` | Reads and validates a player's move |
| `choose_symbol()` | Lets Imran select `X` or `O` |
| `choose_difficulty()` | Selects Easy, Medium, or Hard AI |
| `easy_computer_move()` | Makes a random computer move |
| `medium_computer_move()` | Uses basic attack and defense strategy |
| `minimax()` | Evaluates game states for Hard mode |
| `hard_computer_move()` | Selects an optimal Minimax move |
| `get_winning_combination()` | Detects winning positions |
| `show_scoreboard()` | Displays current scores |
| `show_match_history()` | Displays previous match results |
| `play_again()` | Controls replay behavior |
| `play_vs_computer()` | Runs Imran vs Computer mode |
| `play_vs_player()` | Runs Imran vs Emu mode |
| `main()` | Controls the main menu and program flow |

## Project Structure

A simple repository can be organized like this:

```text
tic-tac-toe/
│
├── tic_tac_toe.py
├── README.md
└── LICENSE
```

`LICENSE` is optional and should only be added if you decide to publish the project under a specific license.

## Technologies Used

- Python 3
- Python `random` module
- Minimax algorithm
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- Exception handling

## Version 2.1 Improvements

Compared with the original project, Version 2.1 adds:

- Cleaner game structure
- Fixed default player names
- Multiple computer difficulty levels
- Minimax AI
- Score tracking
- Match history
- Winning-line detection
- Better validation
- Improved replay flow
- Symbol selection only once per game session
- Improved main menu

## Future Improvements

Possible future additions include:

- Graphical User Interface using Tkinter or Pygame
- Save scoreboard and match history to a file
- Online multiplayer
- Sound effects
- Custom player names
- Theme selection
- Tournament mode

## Author

**Md. Imran Hossain Emu**

---

If you like this project, you can give the repository a ⭐ on GitHub.
