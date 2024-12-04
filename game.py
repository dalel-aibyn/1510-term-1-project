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
        0: {"Pen and paper": 1},
        1: {"Textbook": 5},
        2: {"Manual": 4},
        3: {"Calculator": 3}
    }

    items_locations = {(0, 5): "Pen and paper"}

    for tier in range(1, 4):
        tier_positions = get_tier_positions(tier)
        tier_items = items_by_tier[tier]

        for item_name, item_quantity in tier_items.items():
            place_tier_items(tier_positions, item_name, item_quantity, items_locations)

    return items_locations


def make_character():
    name = input("Enter your character's name: ")
    inventory = {
        "Pen and paper": False,
        "Textbook": False,
        "Manual": False,
        "Calculator": True
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

            if item == "Pen and paper":
                character["time given to solve"] = 10
                print("Your time to solve problems has increased from 8 seconds to 16 seconds!")
            elif item == "Textbook":
                print("You will now get hints on how to solve the problem!")
            elif item == "Manual":
                print("You will now see the range within which the correct answer lies!")
            elif item == "Calculator":
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


def addition_problem():
    number1 = randint(-10000, 10000)
    number2 = randint(-10000, 10000)
    number3 = randint(-10000, 10000)

    sign1 = "+" if number2 == abs(number2) else "-"
    sign2 = "+" if number3 == abs(number3) else "-"

    problem = f"{number1} {sign1} {abs(number2)} {sign2} {abs(number3)} = ?"
    answer = number1 + number2 + number3

    return problem, answer


def multiplication_problem():
    number1 = randint(1, 1000)
    number2 = randint(1, 1000)
    number3 = randint(1, 1000)

    problem = f"{number1} * {number2} * {number3} = ?"
    answer = number1 * number2 * number3

    return problem, answer


def easy_power_problem():
    base = randint(2, 10)
    power = randint(2, 5)

    problem = f"{base}^{power} = ?"
    answer = base ** power

    return problem, answer


def hard_power_problem():
    base = randint(5, 25)
    power = randint(5, 10)
    multiplier = randint(2, 9)

    problem = f"{multiplier} * {base}^{power} = ?"
    answer = multiplier * (base ** power)

    return problem, answer


def easy_log_problem():
    base = random.choice([2, 3, 5, 10])
    power = randint(3, 8)
    multiplier = randint(2, 5)

    number = multiplier * (base ** power)

    if base == 10:
        problem = f"log({number}) = ?"
    else:
        problem = f"log{base}({number}) = ?"
    answer = power + math.log(multiplier, base)

    return problem, answer


def hard_log_problem():
    base = random.choice([2, 3, 5, 10])
    power1 = randint(2, 6)
    power2 = randint(2, 6)

    x = randint(2, 5)

    if base == 10:
        problem = f"log({x}^{power1}) + log({x}^{power2}) = ?"
    else:
        problem = f"log{base}({x}^{power1}) + log{base}({x}^{power2}) = ?"
    answer = power1 + power2

    return problem, answer


def quadratic_problem():
    solution1 = randint(-10, 10)
    solution2 = randint(-10, 10)

    term_b = -(solution1 + solution2)
    term_c = solution1 * solution2

    term_b_string = f"+ {term_b}" if term_b >= 0 else f"- {abs(term_b)}"
    term_c_string = f"+ {term_c}" if term_c >= 0 else f"- {abs(term_c)}"

    problem = f"x² {term_b_string}x {term_c_string} = 0"

    return problem, (solution1, solution2)


def cubic_problem():
    solution1 = randint(-10, 10)
    solution2 = randint(-10, 10)
    solution3 = randint(-10, 10)

    term_b = -(solution1 + solution2 + solution3)
    term_c = (solution1 * solution2 + solution2 * solution3 + solution1 * solution3)
    term_d = -(solution1 * solution2 * solution3)

    term_b_string = f"+ {term_b}" if term_b >= 0 else f"- {abs(term_b)}"
    term_c_string = f"+ {term_c}" if term_c >= 0 else f"- {abs(term_c)}"
    term_d_string = f"+ {term_d}" if term_d >= 0 else f"- {abs(term_d)}"

    problem = f"x³ {term_b_string}x² {term_c_string}x {term_d_string} = 0"

    return problem, (solution1, solution2, solution3)


def factorial_term(answer):
    term = randint(1, 10)

    try:
        value = term * math.gamma(answer + 1)
    except ValueError:
        value = float('inf')
    
    term_string = "x!" if term == 1 else f"{term}x!"
    return [value, term_string]


def x_raised_to_power_term(answer):
    term1 = randint(1, 10)
    term2 = randint(2, 10)

    value = term1 * (answer ** term2)

    term_string = f"x^{term2}" if term1 == 1 else f"{term1}x^{term2}"
    return [value, term_string]


def term_raised_to_x_term(answer):
    term = randint(2, 10)
    
    value = term ** answer

    term_string = f"{term}^x"
    return [value, term_string]


def simple_term(answer):
    term = randint(1, 10)

    value = term * answer

    term_string = "x" if term == 1 else f"{term}x"
    return [value, term_string]


def generate_term3(term1_value, term2_value, has_solution):
    if has_solution:
        value = 0 - term1_value - term2_value
        sign = "+" if value == abs(value) else "-"
        term3_string = f"{sign} {abs(value):.2f}"
        return [value, term3_string]
    else:
        return [float('inf'), "+ 69^420"]  # this will like never happen, but just in case


def extreme_diophantine_problem():
    answer = random.uniform(-10, 10)
    terms = [factorial_term(answer), x_raised_to_power_term(answer), term_raised_to_x_term(answer), simple_term(answer)]
    signs = ("+", "-")

    has_solution = False
    term1, term2 = random.sample(terms, 2)
    if term1[0] != float('inf') and term2[0] != float('inf'):
        has_solution = True

    sign = random.choice(signs)
    if sign == "-":
        term2[0] *= -1

    term3 = generate_term3(term1[0], term2[0], has_solution)

    problem = f"{term1[1]} {sign} {term2[1]} {term3[1]} = 0"
    return problem, answer if has_solution else None  # on a rare occasion that the problem is unsolvable


def get_problem(current_area):
    problem = None
    answer = None
    hint = None
    
    if current_area == "Entrance":
        problem, answer = addition_problem()
        hint = "Tip: Add up the significant digits, while keeping track of their signs"
        
    elif current_area == "Arithmetics":
        func = random.choice([multiplication_problem, easy_power_problem])
        problem, answer = func()
        if func == multiplication_problem:
            hint = "Tip: Round the numbers to the nearest multiple of 50, then multiply"
        else:
            hint = "Tip: Multiply the base by itself the specified number of times"
            
    elif current_area == "Algebra":
        func = random.choice([hard_power_problem, easy_log_problem])
        problem, answer = func()
        if func == hard_power_problem:
            hint = "Tip: First calculate the power, then multiply by the coefficient"
        else:
            hint = "Tip: For log(x), find the power that raises the base to get x"
            
    elif current_area == "Calculus":
        func = random.choice([hard_log_problem, quadratic_problem])
        problem, answer = func()
        if func == hard_log_problem:
            hint = "Tip: log(a) + log(b) = log(a*b)"
        else:
            hint = (f"Tip: x² + bx + c = (x + m)(x + n)\n"
                    f"m + n = b\n"
                    f"m * n = c\n"
                    f"x1 = -m and x2 = -n")
            
    elif current_area == "Number Theory":
        func = random.choice([cubic_problem, extreme_diophantine_problem])
        problem, answer = func()
        if func == cubic_problem:
            hint = (f"Tip: Use the Rational Root Theorem\n"
                    f"Any possible rational root of the cubic equation must be a factor of the constant term")
        else:
            hint = "Tip: Good luck"
    return problem, answer, hint


def get_timed_answer(thinking_time, problem=None, has_Calculator=False):
    try:
        end_time = time() + thinking_time
        if has_Calculator:
            print(f"Your answer (you have {thinking_time} seconds): ")
            answer = input()
            if time() > end_time:
                return None
    
            cleaned_input = "".join(answer.lower().split())
            cleaned_problem = "".join(problem.lower().split())
            return {"answer": cleaned_input == cleaned_problem}
        else:
            answer = input(f"Your answer (you have {thinking_time} seconds): ")
            if time() > end_time:
                return None
            return float(answer)
    except ValueError:
        return "critical"


def generate_opponent_guess(correct_answer):
    if correct_answer is None:
        return None
    elif isinstance(correct_answer, tuple):
        chosen_solution = random.choice(correct_answer)
        delta = max(abs(chosen_solution) * 0.1, 2)
        anchor = random.uniform(chosen_solution - delta, chosen_solution + delta)
        return random.uniform(anchor - delta * 2, anchor + delta * 2)
    else:
        delta = max(abs(correct_answer) * 0.1, 2)
        anchor = random.uniform(correct_answer - delta, correct_answer + delta)
        return random.uniform(anchor - delta * 2, anchor + delta * 2)
    

def generate_answer_range(correct_answer):
    if correct_answer is None:
        return None
    elif isinstance(correct_answer, tuple):
        chosen_solution = random.choice(correct_answer)
        delta = max(abs(chosen_solution) * 0.125, 5)
        anchor = random.uniform(chosen_solution - delta, chosen_solution + delta)
        return anchor - delta * 2, anchor + delta * 2
    else:
        delta = max(abs(correct_answer) * 0.125, 5)
        anchor = random.uniform(correct_answer - delta, correct_answer + delta)
        return anchor - delta * 2, anchor + delta * 2


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
    elif isinstance(player_answer, dict):  # Calculator case
        if player_answer["answer"]:  # Typed problem correctly
            print(f"You typed the problem correctly! Opponent takes damage! (-{character['damage']} mood)")
            opponent_stats["mood"] -= character["damage"]
            return True
        else:  # Typed problem incorrectly
            print(f"You typed the problem incorrectly! You take damage! (-{opponent_stats['damage']} mood)")
            character["mood"] -= opponent_stats["damage"]
            return False

    # For unsolvable problems
    if correct_answer is None:
        print("\nThe problem was particularly challenging!")
        print(f"You've provided a valid answer! Opponent takes damage! (-{character['damage']} mood)")
        opponent_stats["mood"] -= character["damage"]
        return True

    if isinstance(correct_answer, tuple):
        player_difference = min(abs(player_answer - correct_answer[0]),
                                abs(player_answer - correct_answer[1]))
        opponent_difference = min(abs(opponent_guess - correct_answer[0]),
                                  abs(opponent_guess - correct_answer[1]))
    else:
        player_difference = abs(player_answer - correct_answer)
        opponent_difference = abs(opponent_guess - correct_answer)

    print(f"\nOpponent guessed: {opponent_guess:.2f}")

    if player_difference < opponent_difference:
        print(f"You were closer! Opponent takes damage! (-{character['damage']} mood)")
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
        problem, correct_answer, hint = get_problem(current_area)
        thinking_time = 16 if character["inventory"]["Pen and paper"] else 8

        print(f"\nProblem: {problem}")
        if character["inventory"]["Textbook"]:
            print(f"{hint}")
        if character["inventory"]["Manual"]:
            answer_range = generate_answer_range(correct_answer)
            if answer_range:
                print(f"The answer lies between {answer_range[0]:.2f} and {answer_range[1]:.2f}")
            else:
                print("Unable to find the answer range!")
        if character["inventory"]["Calculator"]:
            print("Type in the problem instead of solving it!")

        player_answer = get_timed_answer(thinking_time, problem, character["inventory"]["Calculator"])
        opponent_guess = generate_opponent_guess(correct_answer)

        handle_duel_result(character, player_answer, opponent_guess, correct_answer, opponent_stats)

    if opponent_stats["mood"] <= 0:
        print(f"\nYou won the duel! You replenish 5 mood. \nYour mood is currently at "
              f"{character['mood']}/{character["max_mood"]}")
        character["opponents_bested"] += 1
        level_up(character, opponent_stats["experience"])
        character["mood"] = min(character["max_mood"], character["mood"] + 5)
        return True
    else:
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


def is_alive(character):
    return character["mood"] > 0


def is_goal(character):
    return character["row"] == 6 and character["column"] == 6


def recap(character):
    if is_alive(character):
        print(f"\nCongratulations, {character['name']}! You've reached the goal!")
    else:
        print(f"\n{character['name']}, you've been bested...")

    print("\nFinal Stats:")
    print(f"Level: {math.floor(character['level'])}")
    print(f"Mood: {character['mood']}/{character['max_mood']}")
    print(f"Damage: {character['damage']}")
    print(f"Steps taken: {character['steps_taken']}")
    print(f"Opponents defeated: {character['opponents_bested']}")

    print("\nItems collected:")
    collected_items = [item for item, has_item in character["inventory"].items() if has_item]
    if collected_items:
        for item in collected_items:
            print(f"- {item}")
    else:
        print("None!")

    print("\nAreas visited:")
    for area, visited in character["areas_visited"].items():
        print(f"- {area}: {'✓' if visited else '✗'}")


def get_encounter_probability(character, current_area):
    area_difficulty = {
        "Entrance": 1,
        "Arithmetics": 2,
        "Algebra": 3,
        "Calculus": 4,
        "Number Theory": 5
    }

    difficulty = area_difficulty[current_area]
    level = math.floor(character["level"])

    probability = character["opponent_encounter_cooldown"] + (level // 2) - (difficulty // 2)

    return max(1, min(5, probability))


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

            if is_goal(character):
                break

            current_pos = (character["column"], character["row"])
            current_location = board[current_pos]
            current_area = current_location["tier_name"]

            if not character["areas_visited"][current_area]:
                character["opponent_encounter_cooldown"] = 1
                character["areas_visited"][current_area] = True

            encounter_chance = get_encounter_probability(character, current_area)
            if randint(1, encounter_chance) == 1:
                math_duel(character, current_area)
                character["opponents_encountered"][current_area] = True
                character["opponent_encounter_cooldown"] = 5
            else:
                character["opponent_encounter_cooldown"] -= 1

            if not is_alive(character):
                break

            handle_item_pickup(character, items_locations, current_pos)
        else:
            print("Invalid move - out of bounds!")
        sleep(2)
    recap(character)


def main():
    """
        Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
