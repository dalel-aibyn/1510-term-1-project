"""
AIBYN DALEL
A01311270
"""
import random
from random import randint
from time import sleep
from time import time
import math


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
            board[(column, row)] = {
                "tier_name": tiers[tier]["name"],
                "tier_color": tiers[tier]["color"]
            }

    return board


def has_adjacent_item(position, items_locations):
    column, row = position
    adjacent_positions = [
        (column, row - 1),
        (column + 1, row),
        (column, row + 1),
        (column - 1, row)
    ]
    
    for adj_pos in adjacent_positions:
        if adj_pos in items_locations:
            return True
    return False


def get_tier_positions(tier):
    tier_positions = []
    for column in range(7):
        for row in range(7):
            if determine_tier(column, row) == tier:
                if tier == 0 and column == 0 and row == 6:
                    continue
                tier_positions.append((column, row))
    return tier_positions


def place_tier_items(tier_positions, item_name, item_quantity, items_locations):
    items_placed = 0
    attempts = 0
    max_attempts = 69
    
    while items_placed < item_quantity and attempts < max_attempts and tier_positions:
        position = random.choice(tier_positions)
        
        if not has_adjacent_item(position, items_locations):
            items_locations[position] = item_name
            tier_positions.remove(position)
            items_placed += 1
        
        attempts += 1


def add_items_to_board():
    items_by_tier = {
        0: {"pen and paper": 1},
        1: {"maths textbook": 5},
        2: {"manual of logarithms and roots": 4},
        3: {"calculator": 3}
    }
    
    items_locations = {}
    
    for tier in range(4):
        tier_positions = get_tier_positions(tier)
        tier_items = items_by_tier[tier]
        
        for item_name, item_quantity in tier_items.items():
            place_tier_items(tier_positions, item_name, item_quantity, items_locations)
    
    return items_locations


def make_character():
    name = input("Enter your character's name: ")
    inventory = {
        "pen and paper": False,
        "maths textbook": False,
        "manual of logarithms and roots": False,
        "calculator": False
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
        "Number Theory": False
    }

    return {
        "name": name,
        "column": 0,
        "row": 6,
        "Current HP": 5,
        "mood": 20,
        "max_mood": 20,
        "damage": 3,
        "inventory": inventory,
        "areas_visited": areas_visited,
        "opponents_encountered": opponents_encountered,
        "opponents_bested": 0,
        "steps_taken": 0,
        "level": 0.0,
        "opponent_encounter_cooldown": 1,
        "current_location": "Entrance"
    }


def get_user_choice():
    valid_inputs = {'n': (-1, 0), 's': (1, 0), 'e': (0, 1), 'w': (0, -1)}
    while True:
        choice = input("Enter direction (n/s/e/w): ").lower()
        if choice in valid_inputs:
            return valid_inputs[choice]
        print("Invalid direction. Please enter n, s, e, or w.")


def validate_move(board, character, direction):
    delta_row, delta_column = direction
    new_row = character["row"] + delta_row
    new_column = character["column"] + delta_column
    
    if 0 <= new_row < board["max_y"] and 0 <= new_column < board["max_x"]:
        return delta_row, delta_column
    return False


def move_character(character, direction):
    delta_row, delta_column = direction
    character["row"] += delta_row
    character["column"] += delta_column
    character["steps_taken"] += 1


def print_board(board, items_locations, character_pos):
    colors = {
        "blue": "\033[44m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "orange": "\033[48;5;208m",
        "red": "\033[41m",
        "purple": "\033[45m",
        "reset": "\033[0m",
        "pink": "\033[45m"
    }

    print("\n     " + "   ".join(str(i) for i in range(7)))
    print("   +" + "---+" * 7)
    
    for row in range(7):
        row_str = f" {row} |"
        for column in range(7):
            if (column, row) == character_pos:
                row_str += f"{colors[board[(column, row)]['tier_color']]} @ {colors['reset']}|"
            elif (column, row) in items_locations:
                item = items_locations[(column, row)]
                row_str += f"{colors[board[(column, row)]['tier_color']]} {item[0].upper()} {colors['reset']}|"
            else:
                row_str += f"{colors[board[(column, row)]['tier_color']]}   {colors['reset']}|"
        print(row_str)
        print("   +" + "---+" * 7)


def handle_item_pickup(character, items_locations, position):
    if position in items_locations:
        item = items_locations[position]
        if not character["inventory"][item]:
            character["inventory"][item] = True
            del items_locations[position]
            print(f"\nYou've found a \"{item}\"! Added to inventory.")

            if item == "pen and paper":
                character["time given to solve"] = 10
                print("Your time to solve problems has increased to 10 seconds!")
            elif item == "maths textbook":
                print("You will now get hints on how to solve the problem!")
            elif item == "manual of logarithms and roots":
                print("You will now see the range within which the correct answer involving those lies!")
            elif item == "calculator":
                print("Type in the problem instead of solving it!")

        else:
            print(f"\nYou already have a \"{item}\" in your inventory.")


def get_opponent_stats(area):
    return {
        "Entrance": {"mood": 6, "damage": 2, "experience": 0.1},
        "Arithmetics": {"mood": 9, "damage": 3, "experience": 0.2},
        "Algebra": {"mood": 12, "damage": 5, "experience": 0.5},
        "Calculus": {"mood": 15, "damage": 7, "experience": 1},
        "Number Theory": {"mood": 20, "damage": 11, "experience": 2}
    }[area]


def get_problem():
    # Placeholder for now
    return "1 + 1", 2


def get_timed_answer(thinking_time):
    end_time = time() + thinking_time
    
    try:
        answer = input(f"Your answer (you have {thinking_time} seconds): ")
        if time() > end_time:
            return None
        return float(answer)
    except ValueError:
        return "critical"


def generate_opponent_guess(correct_answer):
    return random.uniform(correct_answer * 0.9, correct_answer * 1.1)


def handle_duel_result(character, player_answer, opponent_guess, correct_answer, opponent_stats):
    if player_answer == "critical":
        critical_damage = opponent_stats["damage"] * 2
        print(f"Invalid input! Opponent deals CRITICAL damage! (-{critical_damage} mood)")
        character["mood"] -= critical_damage
        return False
    elif player_answer is None:
        print(f"Opponent guessed: {opponent_guess:.2f}")
        print(f"You didn't answer in time! You take damage! (-{opponent_stats['damage']} mood)")
        character["mood"] -= opponent_stats["damage"]
        return False
    
    player_difference = abs(player_answer - correct_answer)
    opponent_difference = abs(opponent_guess - correct_answer)
    
    print(f"\nOpponent guessed: {opponent_guess:.2f}")
    
    if player_difference < opponent_difference:
        print(f"You were closer! Opponent takes damage! (-{opponent_stats['damage']} mood)")
        opponent_stats["mood"] -= character["damage"]
        return True
    else:
        print(f"Opponent was closer! You take damage! (-{opponent_stats['damage']} mood)")
        character["mood"] -= opponent_stats["damage"]
        return False


def math_duel(character, current_area):
    print("MATH DUEL")
    
    opponent_stats = get_opponent_stats(current_area)
    
    while opponent_stats["mood"] > 0 and character["mood"] > 0:
        print(f"\nOpponent mood: {opponent_stats['mood']}")
        print(f"Your Mood: {character['mood']}")
        problem, correct_answer = get_problem()
        thinking_time = 10 if character["inventory"]["pen and paper"] else 5
        
        print(f"\nProblem: {problem}")
        print(f"You have {thinking_time} seconds to answer...")
        
        player_answer = get_timed_answer(thinking_time)
        opponent_guess = generate_opponent_guess(correct_answer)
        
        handle_duel_result(character, player_answer, opponent_guess, correct_answer, opponent_stats)
    
    if opponent_stats["mood"] <= 0:
        print("\nYou won the duel! You replenish 5 mood.")
        character["opponents_bested"] += 1
        level_up(character, opponent_stats["experience"])
        character["mood"] = min(character["max_mood"], character["mood"] + 5)
        return True
    else:
        print("\nYou have been bested...")
        return False


def level_up(character, experience):
    old_level = math.floor(character["level"])
    character["level"] += experience
    new_level = math.floor(character["level"])
    
    if new_level > old_level:
        levels_gained = new_level - old_level
        character["max_mood"] = character["max_mood"] + (3 * levels_gained)
        character["damage"] = character["damage"] + levels_gained
        print(f"\nLevel Up! You are now level {new_level}!")
        print(f"Max mood increased to {character['max_mood']}!")
        print(f"Damage increased to {character['damage']}!")


def game():
    board = make_board()
    items_locations = add_items_to_board()
    character = make_character()
    
    while True:
        print_board(board, items_locations, (character["column"], character["row"]))
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        
        if valid_move:
            move_character(character, valid_move)
            current_pos = (character["column"], character["row"])
            current_location = board[current_pos]
            current_area = current_location["tier_name"]

            if not character["areas_visited"][current_area]:
                character["opponent_encounter_cooldown"] = 1
                character["areas_visited"][current_area] = True
            
            if randint(1, character["opponent_encounter_cooldown"]) == 1:
                math_duel(character, current_area)
                character["opponents_encountered"][current_area] = True
                character["opponent_encounter_cooldown"] = 5
            else:
                character["opponent_encounter_cooldown"] -= 1

            handle_item_pickup(character, items_locations, current_pos)
        else:
            print("Invalid move - out of bounds!")
        print(character)
        sleep(0.5)


def main():
    """
        Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
