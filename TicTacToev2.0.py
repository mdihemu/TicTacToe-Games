# ============================================================
# TIC-TAC-TOE GAME - VERSION 2.1
#
# Default Players:
# Player 1: Imran
# Player 2: Emu
#
# Features:
# 1. Imran vs Computer
# 2. Imran vs Emu
# 3. Default Player Names
# 4. Symbol Selection - Only Once Per Game Session
# 5. Easy, Medium and Hard Computer Difficulty
# 6. Scoreboard
# 7. Match History
# 8. Replay System
# 9. Input Validation
# 10. Winning Combination Detection
# 11. Hard AI using Minimax
# ============================================================

import random


# ============================================================
# DEFAULT PLAYER NAMES
# ============================================================

PLAYER_1 = "Imran"
PLAYER_2 = "Emu"


# ============================================================
# GLOBAL VARIABLES
# ============================================================

board = [' ' for _ in range(10)]

scores = {
    "Imran": 0,
    "Emu": 0,
    "Computer": 0,
    "Draw": 0
}

match_history = []


# ============================================================
# BOARD FUNCTIONS
# ============================================================

def reset_board():
    global board
    board = [' ' for _ in range(10)]


def print_board():

    print()

    print("     |     |")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print("_____|_____|_____")

    print("     |     |")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print("_____|_____|_____")

    print("     |     |")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print("     |     |")

    print()


def print_position_guide():

    print("\nPosition Guide")

    print("     |     |")
    print("  1  |  2  |  3")
    print("_____|_____|_____")

    print("     |     |")
    print("  4  |  5  |  6")
    print("_____|_____|_____")

    print("     |     |")
    print("  7  |  8  |  9")
    print("     |     |")

    print()


# ============================================================
# BASIC GAME FUNCTIONS
# ============================================================

def space_is_free(position):
    return board[position] == ' '


def insert_letter(letter, position):
    board[position] = letter


def is_board_full():
    return board.count(' ') == 1


def get_available_moves(current_board):

    available_moves = []

    for position in range(1, 10):

        if current_board[position] == ' ':
            available_moves.append(position)

    return available_moves


# ============================================================
# WIN CHECKING
# ============================================================

def get_winning_combination(current_board, letter):

    winning_combinations = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],

        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],

        [1, 5, 9],
        [3, 5, 7]
    ]


    for combination in winning_combinations:

        if (
            current_board[combination[0]] == letter
            and current_board[combination[1]] == letter
            and current_board[combination[2]] == letter
        ):
            return combination


    return None


def is_win(current_board, letter):

    return get_winning_combination(
        current_board,
        letter
    ) is not None


# ============================================================
# PLAYER MOVE
# ============================================================

def get_player_move(player_name, symbol):

    while True:

        move = input(
            f"{player_name}, select a position "
            f"for '{symbol}' (1-9): "
        ).strip()


        try:

            move = int(move)


            if move < 1 or move > 9:

                print(
                    "Please enter a number between 1 and 9."
                )


            elif not space_is_free(move):

                print(
                    "That position is already occupied!"
                )


            else:

                return move


        except ValueError:

            print(
                "Invalid input. Please enter a number."
            )


# ============================================================
# SYMBOL SELECTION
# ============================================================

def choose_symbol(player_name):

    while True:

        symbol = input(
            f"{player_name}, choose your symbol (X/O): "
        ).strip().upper()


        if symbol == 'X':

            return 'X', 'O'


        elif symbol == 'O':

            return 'O', 'X'


        else:

            print(
                "Invalid choice. Please enter X or O."
            )


# ============================================================
# DIFFICULTY
# ============================================================

def choose_difficulty():

    while True:

        print("\nChoose Computer Difficulty")
        print("--------------------------")

        print("1. Easy")
        print("2. Medium")
        print("3. Hard")


        choice = input(
            "Enter your choice (1-3): "
        ).strip()


        if choice == '1':

            return "Easy"


        elif choice == '2':

            return "Medium"


        elif choice == '3':

            return "Hard"


        else:

            print(
                "Invalid choice. Please enter 1, 2 or 3."
            )


# ============================================================
# EASY COMPUTER AI
# ============================================================

def easy_computer_move():

    possible_moves = get_available_moves(board)


    if possible_moves:

        return random.choice(possible_moves)


    return None


# ============================================================
# MEDIUM COMPUTER AI
# ============================================================

def medium_computer_move(
    computer_symbol,
    player_symbol
):

    possible_moves = get_available_moves(board)


    # --------------------------------------------------------
    # Try to win
    # --------------------------------------------------------

    for position in possible_moves:

        board_copy = board[:]

        board_copy[position] = computer_symbol


        if is_win(
            board_copy,
            computer_symbol
        ):

            return position


    # --------------------------------------------------------
    # Block Imran
    # --------------------------------------------------------

    for position in possible_moves:

        board_copy = board[:]

        board_copy[position] = player_symbol


        if is_win(
            board_copy,
            player_symbol
        ):

            return position


    # --------------------------------------------------------
    # Take center
    # --------------------------------------------------------

    if 5 in possible_moves:

        return 5


    # --------------------------------------------------------
    # Take corner
    # --------------------------------------------------------

    corners = [
        position
        for position in [1, 3, 7, 9]
        if position in possible_moves
    ]


    if corners:

        return random.choice(corners)


    # --------------------------------------------------------
    # Take edge
    # --------------------------------------------------------

    edges = [
        position
        for position in [2, 4, 6, 8]
        if position in possible_moves
    ]


    if edges:

        return random.choice(edges)


    return None


# ============================================================
# HARD COMPUTER AI - MINIMAX
# ============================================================

def minimax(
    current_board,
    is_maximizing,
    computer_symbol,
    player_symbol
):

    # Computer wins
    if is_win(
        current_board,
        computer_symbol
    ):

        return 10


    # Imran wins
    if is_win(
        current_board,
        player_symbol
    ):

        return -10


    # Draw
    if len(
        get_available_moves(current_board)
    ) == 0:

        return 0


    # --------------------------------------------------------
    # COMPUTER TURN
    # --------------------------------------------------------

    if is_maximizing:

        best_score = -1000


        for position in get_available_moves(
            current_board
        ):

            current_board[position] = computer_symbol


            score = minimax(
                current_board,
                False,
                computer_symbol,
                player_symbol
            )


            current_board[position] = ' '


            best_score = max(
                best_score,
                score
            )


        return best_score


    # --------------------------------------------------------
    # HUMAN TURN
    # --------------------------------------------------------

    else:

        best_score = 1000


        for position in get_available_moves(
            current_board
        ):

            current_board[position] = player_symbol


            score = minimax(
                current_board,
                True,
                computer_symbol,
                player_symbol
            )


            current_board[position] = ' '


            best_score = min(
                best_score,
                score
            )


        return best_score


def hard_computer_move(
    computer_symbol,
    player_symbol
):

    best_score = -1000

    best_moves = []


    for position in get_available_moves(board):

        board[position] = computer_symbol


        score = minimax(
            board,
            False,
            computer_symbol,
            player_symbol
        )


        board[position] = ' '


        if score > best_score:

            best_score = score

            best_moves = [position]


        elif score == best_score:

            best_moves.append(position)


    if best_moves:

        return random.choice(best_moves)


    return None


# ============================================================
# COMPUTER MOVE CONTROLLER
# ============================================================

def get_computer_move(
    difficulty,
    computer_symbol,
    player_symbol
):

    if difficulty == "Easy":

        return easy_computer_move()


    elif difficulty == "Medium":

        return medium_computer_move(
            computer_symbol,
            player_symbol
        )


    else:

        return hard_computer_move(
            computer_symbol,
            player_symbol
        )


# ============================================================
# WIN MESSAGE
# ============================================================

def display_winning_line(
    winner_name,
    winning_combination
):

    print("\n" + "=" * 45)

    print(
        f"{winner_name} WON THE MATCH!"
    )


    print(
        "Winning Positions: "
        f"{winning_combination[0]} "
        f"-> {winning_combination[1]} "
        f"-> {winning_combination[2]}"
    )


    print(
        f"Congratulations, {winner_name}!"
    )

    print("=" * 45)


# ============================================================
# MATCH HISTORY
# ============================================================

def record_match(result):

    match_history.append(result)


def show_match_history():

    print("\n" + "=" * 45)

    print("MATCH HISTORY")

    print("=" * 45)


    if len(match_history) == 0:

        print(
            "No matches have been played yet."
        )


    else:

        for number, match in enumerate(
            match_history,
            start=1
        ):

            print(
                f"{number}. {match}"
            )


    print("=" * 45)


# ============================================================
# SCOREBOARD
# ============================================================

def show_scoreboard():

    print("\n" + "=" * 45)

    print("SCOREBOARD")

    print("=" * 45)

    print(
        f"Imran Wins    : {scores['Imran']}"
    )

    print(
        f"Emu Wins      : {scores['Emu']}"
    )

    print(
        f"Computer Wins : {scores['Computer']}"
    )

    print(
        f"Draws         : {scores['Draw']}"
    )

    print("=" * 45)


# ============================================================
# REPLAY
# ============================================================

def play_again():

    while True:

        answer = input(
            "\nContinue playing? (Y/N): "
        ).strip().upper()


        if answer in ['Y', 'YES']:

            return True


        elif answer in ['N', 'NO']:

            return False


        else:

            print(
                "Invalid choice. Please enter Y or N."
            )


# ============================================================
# IMRAN VS COMPUTER
# ============================================================

def play_vs_computer():

    print("\n" + "=" * 45)

    print("IMRAN VS COMPUTER")

    print("=" * 45)


    # ========================================================
    # ASK SYMBOL ONLY ONE TIME
    # ========================================================

    player_symbol, computer_symbol = choose_symbol(
        PLAYER_1
    )


    # ========================================================
    # ASK DIFFICULTY ONLY ONE TIME
    # ========================================================

    difficulty = choose_difficulty()


    print("\nGame Settings")
    print("--------------------------")

    print(
        f"Imran    = {player_symbol}"
    )

    print(
        f"Computer = {computer_symbol}"
    )

    print(
        f"Difficulty = {difficulty}"
    )


    print_position_guide()


    # ========================================================
    # REPLAY LOOP
    # ========================================================

    while True:

        reset_board()


        print("\n" + "=" * 45)

        print(
            f"New Match: Imran vs Computer"
        )

        print("=" * 45)


        print(
            f"Imran = {player_symbol} | "
            f"Computer = {computer_symbol}"
        )


        # X always starts
        current_turn = 'X'


        # ====================================================
        # MATCH LOOP
        # ====================================================

        while True:

            print_board()


            # ------------------------------------------------
            # IMRAN'S TURN
            # ------------------------------------------------

            if current_turn == player_symbol:

                move = get_player_move(
                    PLAYER_1,
                    player_symbol
                )


                insert_letter(
                    player_symbol,
                    move
                )


                winning_combination = (
                    get_winning_combination(
                        board,
                        player_symbol
                    )
                )


                if winning_combination:

                    print_board()


                    display_winning_line(
                        PLAYER_1,
                        winning_combination
                    )


                    scores["Imran"] += 1


                    record_match(
                        f"Imran defeated Computer "
                        f"({difficulty} Mode)."
                    )


                    break


            # ------------------------------------------------
            # COMPUTER TURN
            # ------------------------------------------------

            else:

                print(
                    "\nComputer is making a move..."
                )


                move = get_computer_move(
                    difficulty,
                    computer_symbol,
                    player_symbol
                )


                if move is not None:

                    insert_letter(
                        computer_symbol,
                        move
                    )


                    print(
                        f"Computer placed "
                        f"'{computer_symbol}' "
                        f"at position {move}."
                    )


                winning_combination = (
                    get_winning_combination(
                        board,
                        computer_symbol
                    )
                )


                if winning_combination:

                    print_board()


                    display_winning_line(
                        "Computer",
                        winning_combination
                    )


                    scores["Computer"] += 1


                    record_match(
                        f"Computer defeated Imran "
                        f"({difficulty} Mode)."
                    )


                    break


            # ------------------------------------------------
            # DRAW
            # ------------------------------------------------

            if is_board_full():

                print_board()


                print(
                    "\nThe match is a DRAW!"
                )


                scores["Draw"] += 1


                record_match(
                    f"Imran vs Computer "
                    f"({difficulty} Mode) - Draw."
                )


                break


            # ------------------------------------------------
            # SWITCH TURN
            # ------------------------------------------------

            if current_turn == 'X':

                current_turn = 'O'

            else:

                current_turn = 'X'


        # ----------------------------------------------------
        # ASK ONLY WHETHER TO PLAY ANOTHER MATCH
        # ----------------------------------------------------

        if not play_again():

            break


# ============================================================
# IMRAN VS EMU
# ============================================================

def play_vs_player():

    print("\n" + "=" * 45)

    print("IMRAN VS EMU")

    print("=" * 45)


    # ========================================================
    # IMRAN CHOOSES SYMBOL ONLY ONE TIME
    # ========================================================

    imran_symbol, emu_symbol = choose_symbol(
        PLAYER_1
    )


    print("\nGame Settings")
    print("--------------------------")

    print(
        f"Imran = {imran_symbol}"
    )

    print(
        f"Emu   = {emu_symbol}"
    )


    print_position_guide()


    # ========================================================
    # REPLAY LOOP
    # ========================================================

    while True:

        reset_board()


        print("\n" + "=" * 45)

        print("New Match: Imran vs Emu")

        print("=" * 45)


        print(
            f"Imran = {imran_symbol} | "
            f"Emu = {emu_symbol}"
        )


        # X starts first
        current_turn = 'X'


        # ====================================================
        # MATCH LOOP
        # ====================================================

        while True:

            print_board()


            # ------------------------------------------------
            # DETERMINE PLAYER
            # ------------------------------------------------

            if current_turn == imran_symbol:

                current_name = PLAYER_1

                current_symbol = imran_symbol


            else:

                current_name = PLAYER_2

                current_symbol = emu_symbol


            # ------------------------------------------------
            # PLAYER MOVE
            # ------------------------------------------------

            move = get_player_move(
                current_name,
                current_symbol
            )


            insert_letter(
                current_symbol,
                move
            )


            # ------------------------------------------------
            # WIN CHECK
            # ------------------------------------------------

            winning_combination = (
                get_winning_combination(
                    board,
                    current_symbol
                )
            )


            if winning_combination:

                print_board()


                display_winning_line(
                    current_name,
                    winning_combination
                )


                scores[current_name] += 1


                if current_name == PLAYER_1:

                    loser_name = PLAYER_2

                else:

                    loser_name = PLAYER_1


                record_match(
                    f"{current_name} defeated "
                    f"{loser_name}."
                )


                break


            # ------------------------------------------------
            # DRAW
            # ------------------------------------------------

            if is_board_full():

                print_board()


                print(
                    "\nThe match is a DRAW!"
                )


                scores["Draw"] += 1


                record_match(
                    "Imran vs Emu - Draw."
                )


                break


            # ------------------------------------------------
            # SWITCH TURN
            # ------------------------------------------------

            if current_turn == 'X':

                current_turn = 'O'

            else:

                current_turn = 'X'


        # ----------------------------------------------------
        # CONTINUE WITHOUT ASKING SYMBOL AGAIN
        # ----------------------------------------------------

        if not play_again():

            break


# ============================================================
# MAIN MENU
# ============================================================

def print_main_menu():

    print("\n" + "=" * 45)

    print("      TIC-TAC-TOE GAME - VERSION 2.1")

    print("=" * 45)

    print("1. Imran vs Computer")
    print("2. Imran vs Emu")
    print("3. View Scoreboard")
    print("4. View Match History")
    print("5. Show Position Guide")
    print("6. Exit")

    print("=" * 45)


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    print()

    print("*" * 45)

    print("     WELCOME TO TIC-TAC-TOE GAME")

    print("              VERSION 2.1")

    print("*" * 45)


    print(
        f"\nPlayer 1: {PLAYER_1}"
    )

    print(
        f"Player 2: {PLAYER_2}"
    )


    while True:

        print_main_menu()


        choice = input(
            "Enter your choice (1-6): "
        ).strip()


        if choice == '1':

            play_vs_computer()


        elif choice == '2':

            play_vs_player()


        elif choice == '3':

            show_scoreboard()


        elif choice == '4':

            show_match_history()


        elif choice == '5':

            print_position_guide()


        elif choice == '6':

            print("\n" + "=" * 45)

            print(
                "Thank you for playing Tic-Tac-Toe!"
            )

            print(
                "Goodbye Imran and Emu!"
            )

            print("=" * 45)

            break


        else:

            print(
                "\nInvalid choice. "
                "Please enter a number from 1 to 6."
            )


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":

    main()