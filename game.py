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
    """
    Determine the tier of a given position on the game board.

    :param column: horizontal position on board (0-6)
    :param row: vertical position on board (0-6)
    :precondition: column and row must be integers between 0 and 6 inclusive
    :postcondition: correctly identifiy the tier of the given position
    :return: integer representing tier (0: Entrance, 1: Arithmetics, 2: Algebra, 3: Calculus, 4: Number Theory, 5: Goal)
    :raises ValueError: if column or row are outside the valid range

    >>> determine_tier(0, 6)
    0
    >>> determine_tier(6, 6)
    5
    >>> determine_tier(4, 3)
    3
    """
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
    """
    Create a 7x7 game board.

    :param columns: width of the board
    :param rows: height of the board
    :precondition: columns and rows must both be 7
    :postcondition: creates a dictionary representing the game board with proper tiers and colors
    :return: dictionary containing board dimensions and tile information
    :raises ValueError: if columns or rows are not 7

    >>> doctest_board = make_board()
    >>> doctest_board["max_x"], doctest_board["max_y"]
    (7, 7)
    >>> doctest_board[(0, 6)]["tier_name"]
    'Entrance'
    >>> doctest_board[(6, 6)]["tier_name"]
    'Goal'
    >>> doctest_board[(4, 3)]["tier_color"]
    'orange'
    """
    if columns != 7 or rows != 7:
        raise ValueError("Board dimensions must be 7x7")

    tiers = {
        0: {"name": "Entrance", "color": "blue"},
        1: {"name": "Arithmetics", "color": "green"},
        2: {"name": "Algebra", "color": "yellow"},
        3: {"name": "Calculus", "color": "orange"},
        4: {"name": "Number Theory", "color": "red"},
        5: {"name": "Goal", "color": "purple"}
    }

    board = {"max_x": columns, "max_y": rows}

    for column in range(columns):
        for row in range(rows):
            tier = determine_tier(column, row)
            board[(column, row)] = {
                "tier_name": tiers[tier]["name"],
                "tier_color": tiers[tier]["color"]
            }

    return board


def has_adjacent_item(position, items_locations):
    """
    Determine if there is an item in any adjacent position.

    :param position: tuple of (column, row) representing current position
    :param items_locations: dictionary with positions as keys and item names as values
    :precondition: position must be a tuple of two integers
    :postcondition: correctly identifies if any adjacent position has an item
    :return: True if an adjacent position has an item, False otherwise

    >>> items = {(1, 1): "Textbook", (3, 3): "Calculator"}
    >>> has_adjacent_item((1, 2), items)
    True
    >>> has_adjacent_item((0, 0), items)
    False
    >>> has_adjacent_item((2, 3), items)
    True
    """
    column, row = position
    adjacent_positions = [
        (column, row - 1),  # North
        (column + 1, row),  # East
        (column, row + 1),  # South
        (column - 1, row)   # West
    ]

    for adj_pos in adjacent_positions:
        if adj_pos in items_locations:
            return True
    return False


def get_tier_positions(tier):
    """
    Get all board positions that belong to a specific tier.

    :param tier: integer representing the tier (0-5)
    :precondition: tier must be an integer between 0 and 5 inclusive
    :postcondition: correctly identifies all positions that belong to the specified tier
    :return: list of tuples containing (column, row) coordinates for the tier

    >>> print(get_tier_positions(5))  # Goal position
    [(6, 6)]
    >>> len(get_tier_positions(1)) > 0
    True
    """
    tier_positions = []
    for column in range(7):
        for row in range(7):
            if determine_tier(column, row) == tier:
                if tier == 0 and column == 0 and row == 6:
                    continue
                tier_positions.append((column, row))
    return tier_positions


def place_tier_items(tier_positions, item_name, item_quantity, items_locations):
    """
    Attempt to place items in non-adjacent positions within a tier.

    :param tier_positions: list of tuples containing valid (column, row) positions
    :param item_name: string name of the item to place
    :param item_quantity: number of items to place
    :param items_locations: dictionary to store item positions
    :precondition: tier_positions must be a list of valid board positions
    :postcondition: places items in non-adjacent positions within the tier
    :return: None

    >>> items = {}
    >>> place_tier_items([(1, 1), (1, 2), (2, 2), (2, 1)], "Textbook", 2, items)
    >>> len(items) == 2
    True
    """
    items_placed = 0
    attempts = 0
    max_attempts = 69  # to prevent infinite loop

    while items_placed < item_quantity and attempts < max_attempts and tier_positions:
        position = random.choice(tier_positions)

        if not has_adjacent_item(position, items_locations):
            items_locations[position] = item_name
            if position in tier_positions:
                tier_positions.remove(position)
            items_placed += 1

        attempts += 1


def add_items_to_board():
    """
    Put the items on the game board.

    :precondition: none
    :postcondition: creates a dictionary with items placed
    :return: dictionary mapping (column, row) positions to item names

    >>> items = add_items_to_board()
    >>> (0, 5) in items and items[(0, 5)] == "Pen and paper"
    True
    >>> sum(1 for item in items.values() if item == "Manual") == 3
    True
    """
    items_by_tier = {
        0: {"Pen and paper": 1},
        1: {"Textbook": 5},
        2: {"Manual": 3},
        3: {"Calculator": 2}
    }

    items_locations = {(0, 5): "Pen and paper"}

    for tier in range(1, 4):
        tier_positions = get_tier_positions(tier)
        tier_items = items_by_tier[tier]

        for item_name, item_quantity in tier_items.items():
            if item_name == "Manual":
                tier_positions = [(x, y) for x, y in tier_positions if y != 4]
            if item_name == "Calculator":
                tier_positions = [(x, y) for x, y in tier_positions if y != 5]
            
            place_tier_items(tier_positions, item_name, item_quantity, items_locations)

    return items_locations


def make_character():
    """
    Create a new character with initial stats.

    :precondition: none
    :postcondition: creates a dictionary with character's initial stats
    :return: dictionary containing character stats

    >>> character = make_character() # doctest: +SKIP
    >>> character["mood"] # doctest: +SKIP
    20
    >>> character["inventory"]["Pen and paper"] # doctest: +SKIP
    False
    >>> character["areas_visited"]["Entrance"] # doctest: +SKIP
    True
    >>> character["column"] == 0 and character["row"] == 6  # doctest: +SKIP
    True
    """
    name = input("Enter your character's name: ")
    inventory = {
        "Pen and paper": False,
        "Textbook": False,
        "Manual": False,
        "Calculator": False
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
    """
    Get and validate user's movement direction.

    :precondition: none
    :postcondition: returns valid movement direction
    :return: tuple of (row_delta, column_delta) representing movement direction

    >>> get_user_choice()  # doctest: +SKIP
    (-1, 0) # n
    >>> get_user_choice()  # doctest: +SKIP
    (1, 0) # s
    >>> get_user_choice()  # doctest: +SKIP
    (0, 1) # e
    >>> get_user_choice()  # doctest: +SKIP
    (0, -1) # w
    """
    valid_inputs = {'n': (-1, 0), 's': (1, 0), 'e': (0, 1), 'w': (0, -1)}
    while True:
        choice = input("Enter direction (n/s/e/w): ").lower()
        if choice in valid_inputs:
            return valid_inputs[choice]
        print("Invalid direction. Please enter n, s, e, or w.")


def validate_move(board, character, direction):
    """
    Validate if a move stays within the board boundaries.

    :param board: dictionary containing board information
    :param character: dictionary containing character's stats
    :param direction: tuple of (row_delta, column_delta) for movement, character must have row and column stats
    :precondition: board must be properly initialized with max_x and max_y
    :postcondition: determines if the move stays within board boundaries
    :return: direction tuple if move is valid, False otherwise

    >>> doctest_board = {"max_x": 7, "max_y": 7}
    >>> doctest_character = {"row": 0, "column": 0}
    >>> validate_move(doctest_board, doctest_character, (-1, 0))
    False
    >>> validate_move(doctest_board, doctest_character, (0, 1))
    (0, 1)
    """
    delta_row, delta_column = direction
    new_row = character["row"] + delta_row
    new_column = character["column"] + delta_column

    if 0 <= new_row < board["max_y"] and 0 <= new_column < board["max_x"]:
        return delta_row, delta_column
    return False


def move_character(character, direction):
    """
    Update character's position based on movement direction.

    :param character: dictionary containing character's stats
    :param direction: tuple of (row_delta, column_delta) for movement
    :precondition: character must have row and column stats, direction must be a valid movement tuple
    :postcondition: updates character's position and increments steps taken
    :return: None

    >>> char = {"row": 0, "column": 6, "steps_taken": 0}
    >>> move_character(char, (1, 0))
    >>> char["row"], char["column"], char["steps_taken"]
    (1, 6, 1)
    >>> move_character(char, (0, -1))
    >>> char["row"], char["column"], char["steps_taken"]
    (1, 5, 2)
    """
    delta_row, delta_column = direction
    character["row"] += delta_row
    character["column"] += delta_column
    character["steps_taken"] += 1


def print_board(board, items_locations, character_pos):
    """
    Display the game board.

    :param board: dictionary containing board information
    :param items_locations: dictionary of items locations on the board
    :param character_pos: tuple of (column, row) for character position
    :precondition: board and items_locations must be properly initialized dictionaries
    :postcondition: prints formatted board to console
    :return: None

    >>> test_board = {(0, 0): {"tier_name": "Arithmetics", "tier_color": "green"}, "max_x": 1, "max_y": 1}
    >>> test_items = {(1, 0): "Manual"}
    >>> print_board(test_board, test_items, (0, 1))  # doctest: +SKIP
    """
    colors = {
        "blue": "\033[44m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "orange": "\033[48;5;208m",
        "red": "\033[41m",
        "purple": "\033[45m",
        "reset": "\033[0m",
        "pink": "\033[45m",
        "black": "\033[30m"
    }
    
    item_short_names = {
        "Pen and paper": "P & P",
        "Textbook": "TBOOK",
        "Manual": "MNUAL",
        "Calculator": "CLCTR"
    }

    print("\n       " + "       ".join(str(i) for i in range(7)))
    print("   +" + "=======+" * 7)

    for row in range(7):
        row_str = f" {row} |"
        for column in range(7):
            if (column, row) == character_pos:
                row_str += f"{colors[board[(column, row)]['tier_color']]}{colors['black']} *YOU* {colors['reset']}|"
            elif column == 6 and row == 6:
                row_str += f"{colors[board[(column, row)]['tier_color']]}{colors['black']} *END* {colors['reset']}|"
            elif (column, row) in items_locations:
                item = items_locations[(column, row)]
                short_name = item_short_names.get(item, item)
                row_str += (f"{colors[board[(column, row)]['tier_color']]}"
                            f"{colors['black']} {short_name} {colors['reset']}|")
            else:
                row_str += f"{colors[board[(column, row)]['tier_color']]}       {colors['reset']}|"
        print(row_str)
        print("   +" + "=======+" * 7)


def handle_item_pickup(character, items_locations, position):
    """
    Handle the item pickup event.

    :param character: dictionary containing character's stats
    :param items_locations: dictionary of items locations on the board
    :param position: tuple of (column, row) representing current position,
    :precondition: character and items_locations must be properly initialized dictionaries, character must have inventory
    :postcondition: updates character inventory and items_locations if item is picked up
    :return: boolean indicating if an item event occurred

    >>> char = {"inventory": {"Textbook": False}}
    >>> items = {(1, 1): "Textbook"}
    >>> handle_item_pickup(char, items, (1, 1))
    <BLANKLINE>
    An ancient mathematical tome! Its pages contain helpful tips for solving problems.
    True
    >>> char["inventory"]["Textbook"]
    True
    >>> (1, 1) in items
    False
    >>> handle_item_pickup(char, items, (1, 1))  # No item at position anymore
    False
    >>> items = {(2, 2): "Textbook"}
    >>> handle_item_pickup(char, items, (2, 2))  # Already have item
    <BLANKLINE>
    You already have a "Textbook" in your inventory.
    True
    """
    if position in items_locations:
        item = items_locations[position]
        if not character["inventory"][item]:
            character["inventory"][item] = True
            del items_locations[position]
            print_item_found(item)
            return True
        else:
            print(f"\nYou already have a \"{item}\" in your inventory.")
            return True
    return False


def get_opponent_stats(area):
    """
    Get the stats for an opponent in a given area.

    :param area: string name of the area
    :precondition: area must be one of the following: Entrance, Arithmetics, Algebra, Calculus, Number Theory
    :postcondition: returns dictionary with appropriate opponent stats for the area
    :return: dictionary containing mood, damage, and experience that the character gains after defeating the opponent
    :raises KeyError: if area is not valid

    >>> print(get_opponent_stats("Entrance"))
    {'mood': 6, 'damage': 2, 'experience': 0.1}
    >>> print(get_opponent_stats("Number Theory"))
    {'mood': 20, 'damage': 11, 'experience': 2}
    """
    return {
        "Entrance": {"mood": 6, "damage": 2, "experience": 0.1},
        "Arithmetics": {"mood": 9, "damage": 3, "experience": 0.2},
        "Algebra": {"mood": 12, "damage": 5, "experience": 0.5},
        "Calculus": {"mood": 15, "damage": 7, "experience": 1},
        "Number Theory": {"mood": 20, "damage": 11, "experience": 2}
    }[area]


def addition_problem():
    """
    Generate an addition problem with three integers.

    :precondition: none
    :postcondition: creates a problem string and its solution
    :return: (problem string, answer) tuple

    >>> problem, answer = addition_problem()
    >>> isinstance(problem, str) and isinstance(answer, int)  # Example: 123 - 456 + 789 = ?, 456
    True
    """
    number1 = randint(-1000, 1000)
    number2 = randint(-1000, 1000)
    number3 = randint(-1000, 1000)

    sign1 = "+" if number2 == abs(number2) else "-"
    sign2 = "+" if number3 == abs(number3) else "-"

    problem = f"{number1} {sign1} {abs(number2)} {sign2} {abs(number3)} = ?"
    answer = number1 + number2 + number3

    return problem, answer


def multiplication_problem():
    """
    Generate a multiplication problem with three integers.

    :precondition: none
    :postcondition: creates a problem string and its solution
    :return: (problem string, answer) tuple

    >>> problem, answer = multiplication_problem()
    >>> isinstance(problem, str) and isinstance(answer, int)  # Example: 12 * 34 * 56 = ?, 22848
    True
    """
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    number3 = randint(1, 100)

    problem = f"{number1} * {number2} * {number3} = ?"
    answer = number1 * number2 * number3

    return problem, answer


def easy_power_problem():
    """
    Generate a simple exponentiation problem.

    :precondition: none
    :postcondition: creates a problem string and its solution
    :return: (problem string, answer) tuple

    >>> problem, answer = easy_power_problem()
    >>> isinstance(problem, str) and isinstance(answer, int)  # Example: 2^3 = ?, 8
    True
    """
    base = randint(2, 10)
    power = randint(2, 5)

    problem = f"{base}^{power} = ?"
    answer = base ** power

    return problem, answer


def hard_power_problem():
    """
    Generate a bit more complex exponentiation problem with a multiplier.

    :precondition: none
    :postcondition: creates a problem string and its solution
    :return: (problem string, answer) tuple

    >>> problem, answer = hard_power_problem()
    >>> isinstance(problem, str) and isinstance(answer, int)  # Example: 3 * 10^6 = ?, 3000000
    True
    """
    base = randint(5, 25)
    power = randint(5, 10)
    multiplier = randint(2, 9)

    problem = f"{multiplier} * {base}^{power} = ?"
    answer = multiplier * (base ** power)

    return problem, answer


def easy_log_problem():
    """
    Generate a simple logarithm problem.

    :precondition: none
    :postcondition: creates a problem string and its solution
    :return: (problem string, answer) tuple

    >>> problem, answer = easy_log_problem()
    >>> isinstance(problem, str) and isinstance(answer, float)  # Example: log5(625) = ?, 4
    True
    """
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
    """
    Generate a complex logarithm problem.

    :precondition: none
    :postcondition: creates a problem string and its solution
    :return: (problem string, answer) tuple

    >>> problem, answer = hard_log_problem()
    >>> isinstance(problem, str) and isinstance(answer, int)  # Example: log2(5^3) + log2(5^5) = ?, 18.575...
    True
    """
    base = random.choice([2, 3, 5, 10])
    power1 = randint(2, 6)
    power2 = randint(2, 6)

    raised_term = randint(2, 5)

    if base == 10:
        problem = f"log({raised_term}^{power1}) + log({raised_term}^{power2}) = ?"
    else:
        problem = f"log{base}({raised_term}^{power1}) + log{base}({raised_term}^{power2}) = ?"
    answer = power1 + power2

    return problem, answer


def quadratic_problem():
    """
    Generate a quadratic equation problem.

    :precondition: none
    :postcondition: creates a problem string and its solutions
    :return: (problem string, answer) tuple

    >>> problem, answer = quadratic_problem()
    >>> isinstance(problem, str) and isinstance(answer, tuple) and len(answer) == 2  # Example: x² - 3x + 2 = 0, (1, 2)
    True
    """
    solution1 = randint(-10, 10)
    solution2 = randint(-10, 10)

    term_b = -(solution1 + solution2)
    term_c = solution1 * solution2

    term_b_string = f"+ {term_b}" if term_b >= 0 else f"- {abs(term_b)}"
    term_c_string = f"+ {term_c}" if term_c >= 0 else f"- {abs(term_c)}"

    problem = f"x² {term_b_string}x {term_c_string} = 0"

    return problem, (solution1, solution2)


def cubic_problem():
    """
    Generate a cubic equation problem.

    :precondition: none
    :postcondition: creates a problem string and its solutions
    :return: (problem string, answer) tuple

    >>> problem, answer = cubic_problem()
    >>> isinstance(problem, str) and isinstance(answer, tuple) and len(answer) == 3  # Example: x³ - 6x² + 11x - 6 = 0, (1, 2, 3)
    True
    """
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
    """
    Generate a factorial term.

    :param answer: number representing the answer
    :precondition: answer must be a positive number
    :postcondition: creates a term string and its value
    :return: [value, term string] list

    >>> print(factorial_term(5)  # doctest: +SKIP
    [120.0, 'x!']
    >>> print(factorial_term(4))  # doctest: +SKIP
    [144.0, '6x!']
    """
    term = randint(1, 10)

    try:
        value = term * math.gamma(answer + 1)
    except ValueError:
        value = float('inf')
    
    term_string = "x!" if term == 1 else f"{term}x!"
    return [value, term_string]


def x_raised_to_power_term(answer):
    """
    Generate a term with x raised to a power.

    :param answer: number representing the answer
    :precondition: answer must be a positive number
    :postcondition: creates a term string and its value
    :return: [value, term string] list

    >>> print(x_raised_to_power_term(5))  # doctest: +SKIP
    [75, '3x^2']
    >>> print(x_raised_to_power_term(10))  # doctest: +SKIP
    [1000, '10x^3']
    """
    term1 = randint(1, 10)
    term2 = randint(2, 10)

    value = term1 * (answer ** term2)

    term_string = f"x^{term2}" if term1 == 1 else f"{term1}x^{term2}"
    return [value, term_string]


def term_raised_to_x_term(answer):
    """
    Generate a term with a base raised to x.

    :param answer: number representing the answer
    :precondition: answer must be a positive number
    :postcondition: creates a term string and its value
    :return: [value, term string] list

    >>> print(term_raised_to_x_term(5))  # doctest: +SKIP
    [3125, '5^x']
    >>> print(term_raised_to_x_term(10))  # doctest: +SKIP
    [1024, '2^x']
    """
    term = randint(2, 10)
    
    value = term ** answer

    term_string = f"{term}^x"
    return [value, term_string]


def simple_term(answer):
    """
    Generate a simple term with x.

    :param answer: number representing the answer
    :precondition: answer must be a positive number
    :postcondition: creates a term string and its value
    :return: [value, term string] list

    >>> print(simple_term(5))  # doctest: +SKIP
    [5, 'x']
    >>> print(simple_term(10))  # doctest: +SKIP
    [10, '2x']
    """
    term = randint(1, 10)

    value = term * answer

    term_string = "x" if term == 1 else f"{term}x"
    return [value, term_string]


def generate_term3(term1_value, term2_value, has_solution):
    """
    Generate a third term with a sign and a value.

    :param term1_value: number representing the value of the first term
    :param term2_value: number representing the value of the second term
    :param has_solution: boolean indicating if the problem has a solution
    :precondition: term1_value and term2_value must be numbers
    :postcondition: creates a term string and its value
    :return: [value, term string with sign] list

    >>> print(generate_term3(5.0, 10.0, True))
    [-15.0, '- 15.00']
    """
    if has_solution:
        value = 0 - term1_value - term2_value
        sign = "+" if value == abs(value) else "-"
        term3_string = f"{sign} {abs(value):.2f}"
        return [value, term3_string]
    else:
        return [float('inf'), "+ 69^420"]  # this will like never happen, but just in case


def extreme_diophantine_problem():
    """
    Generate an extreme diophantine problem.
    
    :precondition: none
    :postcondition: creates a problem string and its solution
    :return: (problem string, answer) tuple by default, None if the problem is unsolvable

    >>> problem, answer = extreme_diophantine_problem()        # doctest: +SKIP
    >>> isinstance(problem, str) and isinstance(answer, float) # doctest: +SKIP
    True  # Example: x! + 5^x - 15 = 0, 1.619...
    """
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
    """
    Generate a problem based on the current area.

    :param current_area: string representing the current area
    :precondition: current_area must be a valid area name
    :postcondition: creates a problem string and its solution
    :return: (problem string, answer, hint) tuple

    >>> print(get_problem("Entrance"))  # doctest: +SKIP
    ('1 + 2 + 3 = ?', 6, 'Tip: Add up the significant digits, while keeping track of their signs')
    """
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
            hint = "Tip: Round the numbers to the nearest multiple of 10, then multiply"
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


def get_timed_answer(thinking_time, problem=None, has_calculator=False):
    """
    Get user's answer to a given problem within a time limit.

    :param thinking_time: amount of seconds given for the user to answer
    :param problem: string containing the problem, used for when the user has a calculator
    :param has_calculator: boolean indicating if the user has a calculator
    :precondition: thinking_time must be positive number
    :postcondition: returns user's answer if provided within time limit, or None if time expired, or "critical" if invalid input
    :return: float for most cases, dict for when the user has a calculator, None if time expired, "critical" if invalid input

    >>> doctest_answer = get_timed_answer(8)  # doctest: +SKIP
    >>> isinstance(doctest_answer, float)  # doctest: +SKIP
    True
    >>> doctest_answer = get_timed_answer(10, "2+2", True)  # doctest: +SKIP
    >>> isinstance(doctest_answer, dict) and "answer" in doctest_answer  # doctest: +SKIP
    True
    >>> doctest_answer = get_timed_answer(0)  # doctest: +SKIP
    None  # for no answer given in time
    >>> doctest_answer = get_timed_answer(10)  # doctest: +SKIP
    'critical'  # for invalid input
    """
    try:
        end_time = time() + thinking_time
        if has_calculator:
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
    """
    Generate an opponent's guess.

    :param correct_answer: number or tuple of numbers representing solutions
    :precondition: correct_answer must be a number or a tuple of numbers
    :postcondition: creates a range around one of the answers as a hint
    :return: tuple of (min_value, max_value)

    >>> opponent_answer = generate_opponent_guess(10)
    >>> 4 <= opponent_answer <= 16
    True
    >>> opponent_answer = generate_opponent_guess((5, 10))  # Multiple solutions
    >>> -1 <= opponent_answer <= 16
    True
    """
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
    """
    Generate a range that contains the correct answer.

    :param correct_answer: number or tuple of numbers representing solutions
    :precondition: correct_answer must be a number or a tuple of numbers
    :postcondition: creates a range around one of the answers as a hint
    :return: tuple of (min_value, max_value)

    >>> range_min, range_max = generate_answer_range(10)
    >>> -5 <= range_min <= range_max <= 25
    True
    >>> range_min, range_max = generate_answer_range((5, 10))  # Multiple solutions
    >>> -10 <= range_min <= range_max <= 25
    True
    """
    if isinstance(correct_answer, tuple):
        chosen_solution = random.choice(correct_answer)
        delta = max(abs(chosen_solution) * 0.125, 5)
    else:
        delta = max(abs(correct_answer) * 0.125, 5)
        chosen_solution = correct_answer
        
    anchor = random.uniform(chosen_solution - delta, chosen_solution + delta)
    return anchor - delta * 2, anchor + delta * 2


def handle_duel_result(character, player_answer, opponent_guess, correct_answer, opponent_stats):
    """
    Handle the result of a duel.
    
    :param character: dictionary containing character's stats
    :param player_answer: float or dict or None representing the player's answer
    :param opponent_guess: float representing the opponent's guess
    :param correct_answer: number or tuple of numbers representing the correct answer
    :param opponent_stats: dictionary containing opponent's stats
    :precondition: all parameters must be valid
    :postcondition: handles the result of a duel
    :return: boolean indicating if the player won the duel

    >>> handle_duel_result(character, 5.21, 6.9, 4.2, opponent_stats)  # doctest: +SKIP
    True
    """
    if player_answer == "critical":
        critical_damage = opponent_stats["damage"] * 2
        print(f"Invalid input! Opponent deals CRITICAL damage! (-{critical_damage} mood)")
        character["mood"] -= critical_damage
        return False
    if player_answer is None:
        print(f"Opponent guessed: {opponent_guess:.2f}")
        print(f"You didn't answer in time! You take damage! (-{opponent_stats['damage']} mood)")
        character["mood"] -= opponent_stats["damage"]
        return False
        
    if isinstance(player_answer, dict):
        if player_answer["answer"]:
            print(f"You typed the problem correctly! Opponent takes damage! (-{character['damage']} mood)")
            opponent_stats["mood"] -= character["damage"]
            return True
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
        player_difference = min(abs(player_answer - solution) for solution in correct_answer)
        opponent_difference = min(abs(opponent_guess - solution) for solution in correct_answer)
    else:
        player_difference = abs(player_answer - correct_answer)
        opponent_difference = abs(opponent_guess - correct_answer)

    print(f"\nOpponent guessed: {opponent_guess:.2f}")
    
    if player_difference < opponent_difference:
        print(f"You were closer! Opponent takes damage! (-{character['damage']} mood)")
        opponent_stats["mood"] -= character["damage"]
        return True
    
    print(f"Opponent was closer! You take damage! (-{opponent_stats['damage']} mood)")
    character["mood"] -= opponent_stats["damage"]
    return False


def math_duel(character, current_area):
    """
    Conduct a math duel.
    
    :param character: dictionary containing character's stats
    :param current_area: string representing the current area
    :precondition: character must be properly initialized, current_area must be a valid area name
    :postcondition: conducts a math duel
    :return: boolean indicating if the player won the duel
    """
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

        player_answer = get_timed_answer(thinking_time, problem if character["inventory"]["Calculator"]
                                         else None, character["inventory"]["Calculator"])
        opponent_guess = generate_opponent_guess(correct_answer)

        handle_duel_result(character, player_answer, opponent_guess, correct_answer, opponent_stats)

    if opponent_stats["mood"] <= 0:
        print(f"\nYou won the duel! You replenish 10 mood. \nYour mood is currently at "
              f"{character['mood']}/{character["max_mood"]}")
        character["opponents_bested"] += 1
        level_up(character, opponent_stats["experience"])
        character["mood"] = min(character["max_mood"], character["mood"] + 10)
        return True
    else:
        return False


def level_up(character, experience):
    """
    Level up the character and increase their stats.

    :param character: dictionary containing character's stats
    :param experience: float representing the amount of experience gained
    :precondition: character must be properly initialized, experience must be a positive number
    :postcondition: levels up the character and increases their stats
    :return: None

    >>> character = {"level": 2.5, "max_mood": 20, "damage": 5}
    >>> level_up(character, 1.8)  # doctest: +SKIP
    Level Up! You are now level 4!
    Max mood increased to 32!
    Damage increased to 8!
    """
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
    """
    Check if the character is still alive.

    :param character: dictionary containing character's stats
    :precondition: character must have a mood stat
    :postcondition: checks if the character is alive
    :return: boolean indicating if the character is alive

    >>> is_alive({"mood": 5})
    True
    >>> is_alive({"mood": 0})
    False
    """
    return character["mood"] > 0


def is_goal(character):
    """
    Check if the character has reached the goal position.

    :param character: dictionary containing character's stats
    :precondition: character must have row and column stats
    :postcondition: checks if the character has reached the goal position
    :return: boolean indicating if the character has reached the goal position

    >>> is_goal({"row": 6, "column": 6})
    True
    >>> is_goal({"row": 5, "column": 6})
    False
    """
    return character["row"] == 6 and character["column"] == 6


def get_encounter_probability(character, current_area):
    """
    Calculate probability of encountering an opponent in current area.

    :param character: dictionary containing character's level and cooldown
    :param current_area: string name of the current area
    :precondition: character must have level and cooldown attributes
    :postcondition: calculates encounter probability based on area difficulty and character level
    :return: integer between 1 and 5 representing encounter probability

    >>> char = {"level": 2.2, "opponent_encounter_cooldown": 4}
    >>> get_encounter_probability(char, "Entrance")  # Easiest area, 1 in 4 chance
    4
    >>> char = {"level": 2.2, "opponent_encounter_cooldown": 4}
    >>> get_encounter_probability(char, "Number Theory")  # Hardest area, 1 in 1 chance
    1
    >>> char = {"level": 2.2, "opponent_encounter_cooldown": 4}
    >>> get_encounter_probability(char, "Algebra")  # Mid-level area, 1 in 2 chance
    2
    """
    area_difficulty = {
        "Entrance": 1,
        "Arithmetics": 2,
        "Algebra": 3,
        "Calculus": 4,
        "Number Theory": 5
    }
    
    difficulty = area_difficulty[current_area]
    level = math.floor(character["level"])
    return max(1, min(5, character["opponent_encounter_cooldown"] + (level // 2) - difficulty))


def print_intro():
    """
    Print the introduction to the game.

    :return: None
    """
    colors = {
        "blue": "\033[44m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "orange": "\033[48;5;208m",
        "red": "\033[41m",
        "purple": "\033[45m",
        "reset": "\033[0m",
        "pink": "\033[45m",
        "black": "\033[30m"
    }
    print(f"""
╔════════════════════════════════════════════════════════════════════╗
║                  WELCOME TO THE MATHEMATICS REALM                  ║
╚════════════════════════════════════════════════════════════════════╝
          
You find yourself in the Mathematics Realm, a realm where numbers and expressions reign supreme.
Your goal is to reach the end by navigating through increasingly challenging mathematical territories.
You are allowed to, but not discouraged to jump into difficult areas.

Each area presents unique challenges:
• {colors['blue']}{colors['black']}Entrance     {colors['reset']} - Basic arithmetic
• {colors['green']}{colors['black']}Arithmetics  {colors['reset']} - A bit more challenging arithmetic
• {colors['yellow']}{colors['black']}Algebra      {colors['reset']} - Complex algebraic expressions
• {colors['orange']}{colors['black']}Calculus     {colors['reset']} - Difficult equations and functions
• {colors['red']}{colors['black']}Number Theory{colors['reset']} - Complex mathematical problems

Collect items to aid your journey:
• Pen and Paper - Doubles your thinking time
• Textbook      - Provides helpful tips
• Manual        - Shows the range where within which, the answer lies
• Calculator    - Lets you type problems instead of solving them

Good luck and have fun!
""")


def print_area_description(area_name, first_visit=False):
    """
    Print the description of an area.

    :param area_name: string representing the area name
    :param first_visit: boolean indicating if it's the first visit to the area
    :precondition: area_name must be a valid area name
    :postcondition: prints the description of the area
    :return: None

    >>> print_area_description("Entrance", True)
    <BLANKLINE>
    You stand at the beginning of your mathematical journey.
    >>> print_area_description("Entrance", False)
    <BLANKLINE>
    The familiar territory of addition and subtraction surrounds you.
    """
    descriptions = {
        "Entrance": [
            "\nYou stand at the beginning of your mathematical journey.",
            "\nThe familiar territory of addition and subtraction surrounds you."
        ],
        "Arithmetics": [
            "\nNumbers float in the air around you. The fundamental laws of mathematics are strong here.",
            "\nYou've returned to the domain of core mathematical operations."
        ],
        "Algebra": [
            "\nLetters and numbers intertwine in the space around you.",
            "\nYou've stepped back into the realm of algebraic mysteries."
        ],
        "Calculus": [
            "\nThe very space seems to curve and flow here.",
            "\nFunctions flow like rivers around you."
        ],
        "Number Theory": [
            "\nThe deepest mysteries await.",
            "\nThe very foundations of numbers surround you."
        ],
    }
    if area_name in descriptions:
        print(descriptions[area_name][0] if first_visit else descriptions[area_name][1])


def print_duel_start():
    """
    Select and print the initial message of a duel.

    :return: None
    """
    duel_starts = [
        "\nA mathematical entity materializes before you...",
        "\nThe air crackles with mathematical energy as a challenger appears...",
        "\nNumbers swirl and coalesce into a challenging form...",
        "\nA guardian of mathematical truth blocks your path...",
        "\nThe mathematical realm itself challenges your knowledge..."
    ]
    print(random.choice(duel_starts))


def print_item_found(item_name):
    """
    Print the message when an item is found.

    :param item_name: string representing the item name
    :precondition: item_name must be a valid item name
    :postcondition: prints the message when an item is found
    :return: None

    >>> print_item_found("Pen and paper")
    <BLANKLINE>
    You have found a trusty pen and paper! Now you'll have more time to solve problems.
    >>> print_item_found("Textbook")
    <BLANKLINE>
    An ancient mathematical tome! Its pages contain helpful tips for solving problems.
    """
    item_messages = {
        "Pen and paper": "\nYou have found a trusty pen and paper! Now you'll have more time to solve problems.",
        "Textbook": "\nAn ancient mathematical tome! Its pages contain helpful tips for solving problems.",
        "Manual": "\nA manual of mathematical wisdom! It will show you the range where answers lie.",
        "Calculator": "\nA mystical Calculator! You can now type in the problems instead of solving them."
    }
    print(item_messages.get(item_name, f"\nYou found a {item_name}!"))


def print_outro(character, victory=True):
    """
    Print the outro message based on the character's victory status.

    :param character: dictionary containing character's stats
    :param victory: boolean indicating if the character won the game
    :precondition: character must have name, level, steps_taken, opponents_bested, mood, and max_mood stats
    :postcondition: prints the outro message based on the character's victory status
    :return: None
    """
    if victory:
        print(f"""
╔════════════════════════════════════════════════════════════════════╗
║                              VICTORY!                              ║
╚════════════════════════════════════════════════════════════════════╝

Congratulations, {character['name']}! You've conquered the Mathematical Realm!

Your journey by the numbers:
• Reached Level: {math.floor(character['level'])}
• Steps Taken: {character['steps_taken']}
• Opponents Bested: {character['opponents_bested']}
• Final Mood: {character['mood']}/{character['max_mood']}
""")
    else:
        print(f"""
╔════════════════════════════════════════════════════════════════════╗
║                             GAME OVER!                             ║
╚════════════════════════════════════════════════════════════════════╝

Alas, {character['name']}, the mathematical challenges proved too great.

Your journey ended with:
• Level: {math.floor(character['level'])}
• Steps Taken: {character['steps_taken']}
• Opponents Bested: {character['opponents_bested']}
""")
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


def game():
    print_intro()
    board = make_board()
    items_locations = add_items_to_board()
    character = make_character()
    
    last_area = "Entrance"

    while is_alive(character):
        print_board(board, items_locations, (character["column"], character["row"]))
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        event_occurred = False

        if valid_move:
            move_character(character, valid_move)

            if is_goal(character):
                break

            current_pos = (character["column"], character["row"])
            current_location = board[current_pos]
            current_area = current_location["tier_name"]

            if current_area != last_area:
                print_area_description(current_area, not character["areas_visited"][current_area])
                last_area = current_area
                if not character["areas_visited"][current_area]:
                    character["opponent_encounter_cooldown"] = 1
                    character["areas_visited"][current_area] = True
                event_occurred = True

            encounter_chance = get_encounter_probability(character, current_area)
            if randint(1, encounter_chance) == 1:
                print_duel_start()
                math_duel(character, current_area)
                character["opponents_encountered"][current_area] = True
                character["opponent_encounter_cooldown"] = 5
                event_occurred = True
            else:
                character["opponent_encounter_cooldown"] -= 1

            if not is_alive(character):
                break

            if current_pos in items_locations:
                event_occurred = handle_item_pickup(character, items_locations, current_pos)

        else:
            print("Invalid move - out of bounds!")
            event_occurred = True

        sleep(2 if event_occurred else 0.5)
    
    print_outro(character, is_alive(character))


def main():
    """
        Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
