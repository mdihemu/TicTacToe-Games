# Tic-Tac-Toe Games

<h2>
Now, I'm trying to give it a interface. </br>
Without interface it's Look Like:</br>

</h2>

<h2>Sample Case: 1 <br>Play with Computer and You won the match!</h2>
<pre>
Do you want to play again? (Y/N): Y
Want to play with Computer or Friend! (C/F): C
Welcome to play with Computer!
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
Please select a position to place an 'X' (1-9): 1
   |   |
 X |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
Computer take 'O' at position:  3
   |   |
 X |   | O
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
Please select a position to place an 'X' (1-9): 9
   |   |
 X |   | O
   |   |
   |   |
   |   |
   |   |
   |   |
   |   | X
   |   |
Computer take 'O' at position:  5
   |   |
 X |   | O
   |   |
   |   |
   | O |
   |   |
   |   |
   |   | X
   |   |
Please select a position to place an 'X' (1-9): 7
   |   |
 X |   | O
   |   |
   |   |
   | O |
   |   |
   |   |
 X |   | X
   |   |
Computer take 'O' at position:  4
   |   |
 X |   | O
   |   |
   |   |
 O | O |
   |   |
   |   |
 X |   | X
   |   |
Please select a position to place an 'X' (1-9): 8
   |   |
 X |   | O
   |   |
   |   |
 O | O |
   |   |
   |   |
 X | X | X
   |   |
Hurray! You Won the match.
</pre>

<h2>Sample Case: 2 <br>Playing with Friend and Friend win the match!</h2>
<pre>
Do you want to play again? (Y/N): Y
Want to play with Computer or Friend! (C/F): F
Welcome to You & Your friend to play the Tic-Tac-Toe Games!
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
Please select a position to place an 'X' (1-9): 1
   |   |
 X |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
Please select a position to place an 'O' (1-9): 9
   |   |
 X |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   | O
   |   |
Please select a position to place an 'X' (1-9): 2
   |   |
 X | X |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   | O
   |   |
Please select a position to place an 'O' (1-9): 3
   |   |
 X | X | O
   |   |
   |   |
   |   |
   |   |
   |   |
   |   | O
   |   |
Please select a position to place an 'X' (1-9): 6
   |   |
 X | X | O
   |   |
   |   |
   |   | X
   |   |
   |   |
   |   | O
   |   |
Please select a position to place an 'O' (1-9): 7
   |   |
 X | X | O
   |   |
   |   |
   |   | X
   |   |
   |   |
 O |   | O
   |   |
Please select a position to place an 'X' (1-9): 5
   |   |
 X | X | O
   |   |
   |   |
   | X | X
   |   |
   |   |
 O |   | O
   |   |
Please select a position to place an 'O' (1-9): 8
   |   |
 X | X | O
   |   |
   |   |
   | X | X
   |   |
   |   |
 O | O | O
   |   |
Friends Win the match!
</pre>
## Tic-Tac-Toe Games

A command-line Tic-Tac-Toe game written in Python. Version 2.1 includes computer opponents, two-player matches, match replay, a scoreboard, match history, and input validation.

## Requirements

- Python 3

## Run the game

From this directory, run:

```bash
python TicTacToev2.0.py
```

## Main menu

When the game starts, choose one of these options:

1. **Imran vs Computer**
2. **Imran vs Emu**
3. **View Scoreboard**
4. **View Match History**
5. **Show Position Guide**
6. **Exit**

The default players are:

- Player 1: Imran
- Player 2: Emu

## Playing a match

The board uses positions 1 through 9:

```text
       |     |
   1  |  2  |  3
-----|-----|-----
   4  |  5  |  6
-----|-----|-----
   7  |  8  |  9
```

Player 1 chooses `X` or `O` at the start of a game mode. `X` always takes the first turn. Enter an available position from 1 to 9 when prompted.

In computer mode, choose one of three difficulty levels:

- **Easy**: chooses an available position randomly.
- **Medium**: tries to win, block the player, take the center, then choose a corner or edge.
- **Hard**: uses the minimax algorithm to select the strongest move.

After each match, choose `Y` or `N` to play another match. The selected symbols and computer difficulty remain in effect while replaying that game mode.

## Scores and history

The scoreboard tracks wins for Imran, Emu, and the Computer, plus draws. Match history records the result of every match. Both are kept in memory while the program is running and reset when the program exits.

## Project files

- `TicTacToev2.0.py`: Current version of the command-line game.
- `TicTacToeWithComputerAndFriend.py`: Earlier computer-and-friend version.
