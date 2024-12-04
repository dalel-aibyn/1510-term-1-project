"""
AIBYN DALEL
A01311270
"""
import random
from random import randint


def determine_tier(column, row):
    if not (0 <= column <= 6 and 0 <= row <= 6):
        raise ValueError("Column and row must be between 0 and 6 inclusive")

    if (column == 0 and (row == 5 or row == 6)) or (column == 1 and row == 6):
        return 0  # Entrance
    elif column == 6 and row == 6:
        return 5  # Goal
    elif (row == 0) or (row == 1 and column < 4) or (row == 2 and column < 2) or (column == 0 and row < 5):
        return 1  # Arithmetics
    elif (row == 1 and column > 3) or (row == 2 and column > 1) or (row == 3 and 0 < column < 4) or (
            row == 4 and 0 < column < 3):
        return 2  # Algebra
    elif (row == 3 and column > 3) or (row == 4 and 2 < column < 6) or (row == 5 and 0 < column < 4):
        return 3  # Calculus
    else:
        return 4  # Number Theory


def make_board(columns=7, rows=7):
    if columns != 7 or rows != 7:
        raise ValueError("Board dimensions must be 7x7")

    board = {"max_x": columns, "max_y": rows}
    tiers = {
        0: {"name": "Entrance", "color": "blue"},
        1: {"name": "Arithmetics", "color": "green"},
        2: {"name": "Algebra", "color": "yellow"},
        3: {"name": "Calculus", "color": "orange"},
        4: {"name": "Number Theory", "color": "red"},
        5: {"name": "Goal", "color": "purple"}
    }
    
    for column in range(columns):
        for row in range(rows):
            tier = determine_tier(column, row)
            
            can_progress = False
            if tier < 5:
                for delta_row, delta_column in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_column = column + delta_column
                    new_row = row + delta_row
                    if 0 <= new_column < columns and 0 <= new_row < rows:
                        adj_tier = determine_tier(new_column, new_row)
                        if adj_tier > tier:
                            can_progress = True
                            break

            board[(column, row)] = {
                "tier_name": tiers[tier]["name"],
                "tier_color": tiers[tier]["color"],
                "can_progress": can_progress
            }

    return board


def add_items_to_board(columns, rows, items, goal_pos):
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
    name = input("Enter your character's name: ")
    start_x = 0
    start_y = 0
    start_health = 5
    start_mood = 25
    inventory = {
        "pen and paper": 0,
        "maths textbook": 0,
        "manual of logarithms and roots": 0,
        "calculator": 0
    }
    areas_visited = {
        "Entrance": True,
        "Arithmetics": False,
        "Algebra": False,
        "Calculus": False,
        "Number Theory": False,
        "Goal": False
    }
    opponents_encountered = {
        "Entrance": False,
        "Arithmetics": False,
        "Algebra": False,
        "Calculus": False,
        "Number Theory": False,
        "Goal": False
    }
    
    return {
        "name": name,
        "x_position": start_x, 
        "y_position": start_y,
        "Current HP": start_health,
        "mood": start_mood,
        "inventory": inventory,
        "areas_visited": areas_visited,
        "opponents_encountered": opponents_encountered,
        "opponents bested": 0,
        "steps taken": 0,
        "time given to solve": 5
    }


def print_board(board, player_pos):
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
    x_difference = abs(goal_pos[0] - character['x_position'])
    y_difference = abs(goal_pos[1] - character['y_position'])
    return x_difference + y_difference


def check_for_foes():
    return randint(1, 4) == 4


def guessing_game(character):
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
    return character['Current HP'] > 0


def check_if_goal_attained(goal_pos, character):
    return goal_pos == (character['x_position'], character['y_position'])


def is_on_item_space(board, character):
    character_pos = (character['x_position'], character['y_position'])
    item = board[character_pos]
    if item != '--' and item != 'GOAL':
        return True
    return False


def action_with_item(board, character):
    item = board[(character['x_position'], character['y_position'])]
    print(f'You have found: {item}.')
    decided = False
    while not decided:
        decided = item_decision(board, character, item)


def item_decision(board, character, item):
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
    print(f'Choose in which direction you would like to move: ')
    return input()


def validate_move(board, character, direction):
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


def print_progression_board(board):
    colors = {
        "blue": "\033[44m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "orange": "\033[48;5;208m",
        "red": "\033[41m",
        "purple": "\033[45m",
        "reset": "\033[0m"
    }
    
    print("  " + " ".join(str(i) for i in range(7)))
    print("  " + "-" * 13)
    
    for y in range(7):
        row = f"{y}|"
        for x in range(7):
            tier_color = colors[board[(x, y)]["tier_color"]]
            can_progress = "Y" if board[(x, y)]["can_progress"] else "N"
            row += f"{tier_color}{can_progress}{colors['reset']} "
        print(row)


def game():
    board = make_board()
    print_progression_board(board)
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
