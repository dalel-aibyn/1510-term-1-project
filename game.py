"""
AIBYN DALEL
A01311270
"""
import random
from random import randint


def make_board(columns, rows):
    """
    Generate a game board.

    Creates a board with a given number of rows and columns. Returns the board
    in terms of a dictionary, each key being a coordinate and each value describing
    what is in that coordinate. Goal is in the bottom right corner.
    Items are randomly placed everywhere but the goal space. An empty
    space has a value of --.

    :param rows: The number of rows in the board
    :param columns: The number of columns in the board
    :precondition: rows and columns must be positive integers
    :postcondition: Create a board with specified rows and columns, placing items randomly
                    with goal in the bottom right corner
    :return: A dictionary representing the board

    >>> doctest_board = make_board(3, 3)
    >>> len(doctest_board) # Includes the 9 spaces, maximum X-value, maximum Y-value, and coordinates of the goal.
    12
    >>> doctest_board["goal_pos"]
    (2, 2)
    """
    goal_pos = (columns - 1, rows - 1)
    items = ['rock', 'paper', 'scissors']
    items_at = add_items_to_board(columns, rows, items, goal_pos)
    board = {"max_x": columns, "max_y": rows, "goal_pos": goal_pos}
    for row in range(rows):
        for column in range(columns):
            if (column, row) in items_at:
                board[(column, row)] = items_at[(column, row)]
            else:
                board[(column, row)] = '--'
    return board


def add_items_to_board(columns, rows, items, goal_pos):
    """
    Add random items to the board.

    Places items from the list of items, each in a unique coordinate and
    avoids placing an item at the goal position.

    :param rows: The number of rows in the board
    :param columns: The number of columns in the board
    :param items: A list of items to place on the board
    :param goal_pos: A tuple representing the coordinates of the goal position
    :precondition: rows and columns must be positive integers, items must be a list of strings
    :postcondition: Create a dictionary with items placed on the board
    :return: A dictionary with positions as keys and items as values

    >>> items_are_here = add_items_to_board(2, 2, ['rock', 'paper', 'scissors'], (1, 1))
    >>> len(items_are_here)  # In this case, there will be 2 items on the board + goal.
    3
    >>> items_are_here[(1, 1)]
    'GOAL'
    """
    limit = int(round((columns * rows) ** 0.5, 0))
    num_of_items = 0
    items_at = {goal_pos: "GOAL"}
    while num_of_items < limit:
        random_x = randint(0, columns - 1)
        random_y = randint(0, rows - 1)
        if (random_x, random_y) not in items_at:
            items_at[(random_x, random_y)] = random.choice(items)
            num_of_items += 1
    return items_at


def make_character():
    """
    Create characters stats.

    The character starts at coordinates (0,0) with 5 HP and an empty inventory.

    :return: A dictionary representing the character's attributes

    >>> character = make_character()
    >>> character['x_position']
    0
    >>> character['y_position']
    0
    >>> character['Current HP']
    5
    >>> character['inventory']
    []
    """
    start_x = 0
    start_y = 0
    start_health = 5
    inventory = [] # I can make this a dictionary instead where items are keys and values are how many of them you have.
                   # Maybe in the term project, I'm too lazy to change this now
                   # Also, you don't do anything with the items you've collected.
    return {"x_position": start_x, "y_position": start_y, "Current HP": start_health, "inventory": inventory}


def print_board(board, player_pos):
    """
    Print the game board

    Shows the board with either a player, an item, or a goal in each space; or -- if the space is empty.

    :param board: The game board
    :param player_pos: Player's current position on the board
    :precondition: board must be a dictionary with valid board structure
                   player_pos must be within the board's dimensions
    :postcondition: Print the current state of the board
    :return: None
    """
    slot_wideness = 5
    cyan = "\033[36m"
    reset = "\033[0m"
    print(f'\n{cyan}* {f'=' * ((slot_wideness + 1) * board['max_x'] - 1)} *')
    for row in range(board['max_y']):
        print_info_row(board, player_pos, slot_wideness, row)
        if row != board['max_y'] - 1:
            print_inbetween_info(board, player_pos, slot_wideness, row)
    print(f'* {f'=' * ((slot_wideness + 1) * board['max_x'] - 1)} *{reset}\n')


def print_info_row(board, player_pos, slot_wideness, row):
    """
    Print a row of the game board.

    Prints a single row of the game board, showing either
    an empty space, an item, a goal, or the player's position.
    Also, highlights where the player is.

    :param board: The game board
    :param player_pos: Player's current position on the board
    :param slot_wideness: Width of each slot on the board
    :param row: Number of rows on the board
    :precondition: board must be a dictionary with valid board structure
                   player_pos must be within the board's dimensions
                   slot_wideness must be a positive integer bigger than 2
                   row must be a positive integer
    :postcondition: Print the current state of the specified row
    :return: None
    """
    yellow = "\033[33m"
    cyan = "\033[36m"
    reset = "\033[0m"
    info = f'{cyan}||'
    for column in range(board['max_x']):
        slot = ''
        slot_divider = f'{cyan}|'
        if (column, row) == player_pos:
            slot += f"YOU"
            if board[(column, row)] != '--':
                slot += f" + {board[(column, row)]}"
        else:
            slot += f"{board[(column, row)]}"
        slot = slot[:slot_wideness - 2]
        slot = (slot_wideness - len(slot)) // 2 * " " + slot
        slot += (slot_wideness - len(slot)) * " "
        info += f'{reset}{slot}'
        if column != board['max_x'] - 1:
            if (column + 1, row) == player_pos or (column, row) == player_pos:
                slot_divider = f'{yellow}#'
            info += slot_divider
    info += f'{cyan}||'
    print(info)


def print_inbetween_info(board, player_pos, slot_wideness, row):
    """
    Print the line between the rows the game board.

    Prints a line separating the rows the game board, while highlighting where the player is.

    :param board: The game board
    :param player_pos: Player's current position on the board
    :param slot_wideness: Width of each slot on the board
    :param row: Number of rows on the board
    :precondition: board must be a dictionary with valid board structure
                   player_pos must be within the board's dimensions
                   slot_wideness must be a positive integer bigger than 2
                   row must be a positive integer
    :postcondition: Print the line between rows
    :return: None
    """
    yellow = "\033[33m"
    cyan = "\033[36m"
    line = f'{cyan}||'
    for column in range(board['max_x']):
        slot_divider = f'{cyan}-'
        slot_corner = f'{cyan}+'
        if (column, row + 1) == player_pos or (column, row) == player_pos:
            slot_divider = f'{yellow}#'
        if (column + 1, row) == player_pos or (column, row) == player_pos or (column, row + 1) == player_pos or (
        column + 1, row + 1) == player_pos:
            slot_corner = f'{yellow}#'
        line += slot_divider * slot_wideness + slot_corner
        if column == board['max_x'] - 1:
            line = line[:-1] + f'{cyan}||'
    print(line)


def describe_situation(goal_pos, character):
    """
    Describe the current situation of the character.

    Shows how far away the character is from the goal, their HP, and their inventory.

    :param goal_pos: Coordinates of the goal
    :param character: Information about the character
    :precondition: goal_pos is a tuple of coordinates of the goal
                   character is a dictionary with 'x_position', 'y_position', 'Current HP' and 'inventory' keys
                   Value of 'Current HP' key must be a positive integer
    :postcondition: Print the current situation of the character
    :return: None

    >>> doctest_character = make_character()
    >>> describe_situation((5, 3), doctest_character )
    You are 8 steps away from the goal.
    You have 5 health.
    You have no items.
    <BLANKLINE>
    >>> doctest_character= {'x_position': 2, 'y_position': 1, 'Current HP': 3, 'inventory': ['rock', 'paper']}
    >>> describe_situation((5, 3), doctest_character)
    You are 5 steps away from the goal.
    You have 3 health.
    You have: rock, paper.
    <BLANKLINE>
    """
    distance_left = f'You are {distance_to_goal(goal_pos, character)} steps away from the goal.'
    hp_left = f'You have {character["Current HP"]} health.'
    if character['inventory']:
        items_on_you = 'You have: '
        for item in character['inventory']:
            items_on_you += f'{item}, '
        items_on_you = items_on_you[:-2] + '.'
    else:
        items_on_you = 'You have no items.'
    output = f'{distance_left}\n{hp_left}\n{items_on_you}\n'
    print(output)


def distance_to_goal(goal_pos, character):
    """
    Calculate number of steps away from the goal.

    :param goal_pos: Coordinates of the goal
    :param character: Information about the character
    :precondition: goal_pos is a tuple of coordinates of the goal
                   character is a dictionary with 'x_position' and 'y_position' keys
    :postcondition: Correctly calculate the number of steps between the character's position and the goal
    :return: Number of steps away from the goal

    >>> doctest_character = make_character()
    >>> distance_to_goal((5, 3), doctest_character)
    8
    >>> doctest_character  = {'x_position': 2, 'y_position': 1}
    >>> distance_to_goal((5, 3), doctest_character)
    5
    """
    x_difference = abs(goal_pos[0] - character['x_position'])
    y_difference = abs(goal_pos[1] - character['y_position'])
    return x_difference + y_difference


def check_for_foes():
    """
    Determine whether the character encounters a foe.

    Has a 25% chance of returning True, otherwise returns False.

    :return: True if a foe is encountered, False otherwise
    """
    return randint(1, 4) == 4


def guessing_game(character):
    """
    Play a guessing game with a foe.

    Character has to guess a number between 1 and 5 to defeat the foe.
    If the guess is incorrect or invalid, the character loses health.
    If the guess is correct, the foes is defeated and the character moves on.

    :param character: Information about the character
    :precondition: Character is a dictionary with 'Current HP' key
    :postcondition: Correctly update character's health based on the player's guess
    :return: None
    """
    valid_guesses = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
    foe_number = randint(1, 5)
    prompt = 'The challenger has picked a number from 1 to 5.\n\nEnter your guess:\n'
    guess = input(prompt).strip().lower()
    if guess not in valid_guesses:
        print(f'\nYour guess was invalid!\nYou lose 1 health.\n')
        character['Current HP'] -= 1
    else:
        guess = valid_guesses[guess]
        if guess == foe_number:
            print(f'\nYour guess was correct!\nThe challenger has been defeated.\n')
        else:
            print(f'\nYour guess was incorrect!\nYou lose 1 health.\n')
            character['Current HP'] -= 1


def is_alive(character):
    """
    Check if the character is alive or not.

    :param character: Information about the character
    :precondition: Character is a dictionary with 'Current HP' key
    :postcondition: Correctly determine whether the character is alive or not
    :return: True if alive, False otherwise

    >>> doctest_character = make_character()
    >>> is_alive(doctest_character)
    True
    >>> doctest_character  = {'Current HP': 0}
    >>> is_alive(doctest_character)
    False
    """
    return character['Current HP'] > 0


def check_if_goal_attained(goal_pos, character):
    """
    Check if the character has reached the goal or not.

    :param goal_pos: Coordinates of the goal
    :param character: Information about the character
    :precondition: goal_pos is a tuple of coordinates of the goal
                   character is a dictionary with 'x_position' and 'y_position' keys
    :postcondition: Correctly determines whether the character has reached the goal or not
    :return: True if the character has reached the goal, False otherwise

    >>> doctest_character = make_character()
    >>> check_if_goal_attained((5, 3), doctest_character)
    False
    >>> doctest_character  = {'x_position': 5, 'y_position': 3}
    >>> check_if_goal_attained((5, 3), doctest_character)
    True
    """
    return goal_pos == (character['x_position'], character['y_position'])


def is_on_item_space(board, character):
    """
    Check if the character is on an item/goal space or not.

    :param board: The game board
    :param character: Information about the character
    :precondition: board must be a dictionary with valid board structure
                   character is a dictionary with 'x_position' and 'y_position' keys
    :postcondition: Correctly determines if the character is on an item space or not
    :return: True if the character is on a space containing an item, False otherwise
    >>> doctest_character = make_character()
    >>> doctest_board = {(0,0): '--', (0,1): '--', (1,0): 'rock', (1,1): 'GOAL'}
    >>> is_on_item_space(doctest_board, doctest_character)
    False
    >>> doctest_character  = {'x_position': 1, 'y_position': 0}
    >>> is_on_item_space(doctest_board, doctest_character)
    True
    >>> doctest_character  = {'x_position': 1, 'y_position': 1}
    >>> is_on_item_space(doctest_board, doctest_character)
    False
    """
    character_pos = (character['x_position'], character['y_position'])
    item = board[character_pos]
    if item != '--' and item != 'GOAL':
        return True
    return False


def action_with_item(board, character):
    """
    Inform about item found at current location and ask what to do with it.

    Will inform about what item has been found and will repeatedly ask to decide what
    to do with the item until the decision is valid.

    :param board: The game board
    :param character: Information about the character
    :precondition: board must be a dictionary with valid board structure,
                   character is a dictionary with 'x_position', 'y_position' and 'inventory' keys.
    :postcondition: Correctly update the board and character's inventory depending on user's decision.'
    :return: None
    """
    item = board[(character['x_position'], character['y_position'])]
    print(f'You have found: {item}.')
    decided = False
    while not decided:
        decided = item_decision(board, character, item)


def item_decision(board, character, item):
    """
    Ask user to decide what to do with the item.

    :param board: The game board
    :param character: Information about the character
    :param item: Item found at the character's position
    :precondition: board must be a dictionary with valid board structure
                   character is a dictionary with 'x_position', 'y_position' and 'inventory' keys
                   item must be a string
    :postcondition: Correctly update the board and character's inventory depending on user's decision
    :return: True if the decision is made, False otherwise
    """
    print(f'Would you like to take {item} with you? (y/n):')
    decision = input()
    if decision == 'y':
        character['inventory'] += [item]
        board[(character['x_position'], character['y_position'])] = '--'
        print(f'You have acquired: {item}.\n')
        return True
    elif decision == 'n':
        print(f'You decided to leave it behind.\n')
        return True
    else:
        print(f'Invalid input.\n')
        return False


def get_user_choice():
    """
    Ask user to choose the direction to move in.

    :return: The user input as string
    """
    print(f'Choose in which direction you would like to move: ')
    return input()


def validate_move(board, character, direction):
    """
    Check if a move is valid or not.

    :param board: The game board
    :param character: Information about the character
    :param direction: Direction to move in
    :precondition: board must be a dictionary with valid board structure
                   character is a dictionary with 'x_position' and 'y_position' keys
                   direction must be a string
    :postcondition: Correctly determine whether the move is valid or not
    :return: The direction as a string if the move is valid, False otherwise
    """
    modified_direction = direction.lower().strip()
    valid_directions_simple = ('up', 'down', 'right', 'left')
    valid_directions_compass = {'north': 'up', 'east': 'right', 'south': 'down', 'west': 'left'}
    valid_directions_compass_short = {'n': 'up', 'e': 'right', 's': 'down', 'w': 'left'}
    if modified_direction not in valid_directions_simple:
        if modified_direction in valid_directions_compass:
            modified_direction = valid_directions_compass[modified_direction]
        elif modified_direction in valid_directions_compass_short:
            modified_direction = valid_directions_compass_short[modified_direction]
        else:
            print(f'Invalid direction entered: {direction}')
            return False
    valid = move_doesnt_go_off_board(board, character, modified_direction)
    if not valid:
        print(f'Unable to move {modified_direction}, as it goes off the board.')
        return False
    return modified_direction


def move_doesnt_go_off_board(board, character, modified_direction):
    """
    Check if a move goes off the board or not.

    :param board: The game board
    :param character: Information about the character
    :param modified_direction: Direction to move in
    :precondition: board must be a dictionary with valid board structure
                   character is a dictionary with 'x_position' and 'y_position' keys
                   modified_direction must be up, down, left or right
    :postcondition: Correctly determine whether the move goes off the board or not
    :return: True if the move stays on board, False otherwise

    >>> doctest_character = make_character()
    >>> doctest_board = make_board(2,2)
    >>> move_doesnt_go_off_board(doctest_board, doctest_character, 'up')
    False
    >>> move_doesnt_go_off_board(doctest_board, doctest_character, 'right')
    True
    """
    if modified_direction == 'up' and character['y_position'] == 0:
        return False
    elif modified_direction == 'down' and character['y_position'] >= board['max_y'] - 1:
        return False
    elif modified_direction == 'left' and character['x_position'] == 0:
        return False
    elif modified_direction == 'right' and character['x_position'] >= board['max_x'] - 1:
        return False
    return True


def move_character(character, direction):
    """
    Move the character in the valid direction.

    :param character: Information about the character
    :param direction: Direction to move in
    :precondition: character is a dictionary with 'x_position' and 'y_position' keys
                   modified_direction must be 'up', 'down', 'left' or 'right'
                       and must be a valid direction to move in (stay on board)
    :postcondition: Correctly change characters coordinates
    :return: None

    >>> doctest_character = make_character()
    >>> move_character(doctest_character, 'down')
    >>> (doctest_character['x_position'], doctest_character['y_position'])
    (0, 1)
    >>> move_character(doctest_character, 'right')
    >>> move_character(doctest_character, 'right')
    >>> (doctest_character['x_position'], doctest_character['y_position'])
    (2, 1)
    """
    move = [0, 0]
    if direction == 'up':
        move[1] -= 1
    elif direction == 'down':
        move[1] += 1
    elif direction == 'left':
        move[0] -= 1
    elif direction == 'right':
        move[0] += 1
    character['x_position'] += move[0]
    character['y_position'] += move[1]


def game():
    rows = 7
    cols = 7
    board = make_board(cols, rows)
    character = make_character()
    while True:
        print_board(board, (character["x_position"], character["y_position"]))
        describe_situation(board["goal_pos"], character)
        there_is_a_challenger = check_for_foes()
        if there_is_a_challenger:
            print(f'You have encountered a challenger!')
            guessing_game(character)
        achieved_goal = check_if_goal_attained(board["goal_pos"], character)
        if achieved_goal or not is_alive(character):
            break
        character_on_item = is_on_item_space(board, character)
        if character_on_item:
            action_with_item(board, character)
        valid_move = False
        while not valid_move:
            direction = get_user_choice()
            valid_move = validate_move(board, character, direction)
        move_character(character, valid_move)
    print_board(board, (character["x_position"], character["y_position"]))
    if is_alive(character):
        print(f'You have reached the goal and won the game! Congratulations!')
    else:
        distance_left = distance_to_goal(board["goal_pos"], character)
        print(f'You have perished {distance_left} steps away from the goal. Better luck next time!')


def main():
    """
        Drive the program.
    """
    game()


if __name__ == '__main__':
    main()