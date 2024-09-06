from typing import Optional
from support import *

# Functions Implementation

def create_empty_board(board_size: int) -> list[str]:
    """Generates a new empty board.

    Parameters:
        board_size: The size of the board (number of rows and columns).

    Returns:
        A list of strings representing an empty board.
    """
    # Hint: Use a loop to create a list with `board_size` elements, 
    # where each element is a string of `board_size` EMPTY_SQUARE characters.

def get_square(board: list[str], position: tuple[int, int]) -> str:
    """Returns the character present at the given (row, column) position within the given board.

    Parameters:
        board: The current board state as a list of strings.
        position: The position on the board (row, column).

    Returns:
        The character at the specified position on the board.
    """
    # Hint: Extract the row and column from the position tuple.
    # Then, use them to access the correct character in the board.

def change_square(board: list[str], position: tuple[int, int], new_square: str) -> None:
    """Replaces the character at the given (row, column) position with new_square.

    Parameters:
        board: The current board state as a list of strings.
        position: The position on the board (row, column) to be changed.
        new_square: The new character to place at the specified position.

    Returns:
        None. The board is modified in place.
    """
    # Hint: Extract the row and column from the position tuple.
    # Modify the string at the specified row by replacing the character at the column with `new_square`.
    # Remember that strings are immutable, so you need to create a new string for the row.

def coordinate_to_position(coordinate: str) -> tuple[int, int]:
    """Returns the (row, column) position tuple corresponding to the given coordinate.

    Parameters:
        coordinate: The string representing the coordinate (e.g., 'A1').

    Returns:
        A tuple of integers representing the (row, column) position.
    """
    # Hint: Convert the letter (e.g., 'A') to a column number using `ord`.
    # Convert the number (e.g., '1') to a row index. Remember rows are 0-indexed.

def can_place_ship(board: list[str], ship: list[tuple[int, int]]) -> bool:
    """Returns True if the ship can be placed on the board, and False otherwise.

    Parameters:
        board: The current board state as a list of strings.
        ship: A list of tuples representing the positions of the ship.

    Returns:
        A boolean indicating whether the ship can be placed on the board.
    """
    # Hint: Iterate through the positions in the `ship` list.
    # Check if each position on the board is EMPTY_SQUARE.
    # Return False if any position is not empty; otherwise, return True.

def place_ship(board: list[str], ship: list[tuple[int, int]]) -> None:
    """Places the ship on the board.

    Parameters:
        board: The current board state as a list of strings.
        ship: A list of tuples representing the positions of the ship.

    Returns:
        None. The board is modified in place.
    """
    # Hint: Iterate through the positions in the `ship` list.
    # Use `change_square` to update each position to ACTIVE_SHIP_SQUARE.

def attack(board: list[str], position: tuple[int, int]) -> None:
    """Attempts to attack the cell at the (row, column) position within the board.

    Parameters:
        board: The current board state as a list of strings.
        position: The position on the board (row, column) to attack.

    Returns:
        None. The board is modified in place based on the result of the attack.
    """
    # Hint: Get the character at the specified position using `get_square`.
    # If it's ACTIVE_SHIP_SQUARE, change it to DEAD_SHIP_SQUARE. If it's EMPTY_SQUARE, change it to MISS_SQUARE.

def display_board(board: list[str], show_ships: bool) -> None:
    """Prints the board in a human-readable format.

    Parameters:
        board: The current board state as a list of strings.
        show_ships: A boolean indicating whether to show active ships.

    Returns:
        None. The board is printed to the console.
    """
    # Hint: First, print a header row with the column labels (A, B, C, etc.).
    # Then, iterate through each row in the board, printing the row number and the row itself.
    # If `show_ships` is False, replace ACTIVE_SHIP_SQUARE with EMPTY_SQUARE before printing.

def get_player_hp(board: list[str]) -> int:
    """Returns the player's current HP, which is the count of active ship squares.

    Parameters:
        board: The current board state as a list of strings.

    Returns:
        An integer representing the number of active ship squares remaining on the board.
    """
    # Hint: Use a loop or a list comprehension to count the number of ACTIVE_SHIP_SQUARE characters in the entire board.

def display_game(p1_board: list[str], p2_board: list[str], show_ships: bool) -> None:
    """Prints the overall game state.

    Parameters:
        p1_board: Player 1's board state as a list of strings.
        p2_board: Player 2's board state as a list of strings.
        show_ships: A boolean indicating whether to show active ships.

    Returns:
        None. The game state is printed to the console.
    """
    # Hint: Display Player 1's HP and board, followed by Player 2's HP and board.
    # Use `display_board` for each board, passing `show_ships` to control whether ships are visible.

def is_valid_coordinate(coordinate: str, board_size: int) -> tuple[bool, str]:
    """Checks if the provided coordinate is valid.

    Parameters:
        coordinate: The string representing the coordinate (e.g., 'A1').
        board_size: The size of the board.

    Returns:
        A tuple containing a boolean (True if the coordinate is valid) and a string with an error message if invalid.
    """
    # Hint: Check if the coordinate string is exactly 2 characters long.
    # Ensure the letter part is within the range of valid column labels (A, B, C, ...).
    # Ensure the number part is within the valid range of row numbers (1, 2, 3, ...).

def is_valid_coordinate_sequence(coordinate_sequence: str, ship_length: int, board_size: int) -> tuple[bool, str]:
    """Checks if the provided coordinate sequence is valid.

    Parameters:
        coordinate_sequence: A comma-separated string of coordinates.
        ship_length: The expected length of the ship (number of coordinates).
        board_size: The size of the board.

    Returns:
        A tuple containing a boolean (True if the sequence is valid) and a string with an error message if invalid.
    """
    # Hint: Split the `coordinate_sequence` by commas and check if the number of coordinates matches `ship_length`.
    # Validate each coordinate using `is_valid_coordinate`. If any are invalid, return the corresponding error.

def build_ship(coordinate_sequence: str) -> list[tuple[int, int]]:
    """Returns the list of positions corresponding to the coordinate sequence.

    Parameters:
        coordinate_sequence: A comma-separated string of coordinates.

    Returns:
        A list of tuples representing the (row, column) positions of the ship.
    """
    # Hint: Split the `coordinate_sequence` by commas.
    # Convert each coordinate into a (row, column) tuple using `coordinate_to_position`.
    # Return the list of these tuples.

def is_ship_connected(ship: list[tuple[int, int]]) -> bool:
    """Returns True if the ship is connected.

    Parameters:
        ship: A list of tuples representing the positions of the ship.

    Returns:
        A boolean indicating whether all parts of the ship are connected.
    """
    # Hint: Iterate through the `ship` list and ensure each pair of consecutive positions is adjacent.
    # You can use the `manhattan_distance` function for this. If any pair is not adjacent, return False.

def is_ship_straight(ship: list[tuple[int, int]]) -> bool:
    """Returns True if the ship is straight (horizontal or vertical).

    Parameters:
        ship: A list of tuples representing the positions of the ship.

    Returns:
        A boolean indicating whether the ship is straight (not bent).
    """
    # Hint: Check if all the rows are the same (horizontal ship) or if all the columns are the same (vertical ship).
    # If either condition is true, the ship is straight; otherwise, it's bent.

def setup_board(board_size: int, ship_sizes: list[int]) -> list[str]:
    """Allows the user to set up a new board by placing ships.

    Parameters:
        board_size: The size of the board.
        ship_sizes: A list of integers representing the sizes of ships to be placed.

    Returns:
        A list of strings representing the final board setup.
    """
    # Hint: Create an empty board using `create_empty_board`.
    # For each ship size, repeatedly prompt the user to enter valid coordinates until a valid ship is placed.
    # Validate the input, build the ship, check for placement validity, and place the ship on the board.

def get_winner(p1_board: list[str], p2_board: list[str]) -> Optional[str]:
    """Returns which player has won, or None if neither has won yet.

    Parameters:
        p1_board: Player 1's board state as a list of strings.
        p2_board: Player 2's board state as a list of strings.

    Returns:
        A string representing the winner (PLAYER_ONE or PLAYER_TWO), or None if there is no winner yet.
    """
    # Hint: Check the HP of both players using `get_player_hp`.
    # If Player 1's HP is 0, return PLAYER_TWO. If Player 2's HP is 0, return PLAYER_ONE.
    # If neither player has 0 HP, return None.

def make_attack(target_board: list[str]) -> None:
    """Performs a single turn against the target board.

    Parameters:
        target_board: The board state to attack as a list of strings.

    Returns:
        None. The board is modified in place based on the attack.
    """
    # Hint: Repeatedly prompt the player to enter a valid coordinate.
    # Use `is_valid_coordinate` to validate the input. If valid, perform the attack using `attack`.

def play_game() -> None:
    """Coordinates gameplay of a single game of Battleships.

    Returns:
        None. The function manages the entire flow of the game.
    """
    # Hint: Start by getting the board size and ship sizes from the user.
    # Set up the boards for both players using `setup_board`.
    # Alternate turns between players, checking for a winner after each turn.
    # Use `display_game` to show the current game state and `make_attack` to handle player actions.

if __name__ == "__main__":
    play_game()
