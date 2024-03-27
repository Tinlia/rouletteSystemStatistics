import random
from dicts import squares, square_types

def spin(bal = 0, amount = 0, bet_value = "1"):
    # Subtract amount from balance
    bal -= amount
    # Roll a random choice from the squares dict
    selected_square = list(random.choice(list(squares.items())))
    # Announce the square chosen
    num = selected_square[0]
    num_values = selected_square[1]

    # Check for bet_type in square's list
    if bet_value in num_values:
        # If the bet_type is in the list
        # Add amount*multiplier to balance
        if bet_value == 'even' or bet_value == 'odd' or bet_value == 'high' or bet_value == 'low' or bet_value == 'red' or bet_value == 'black':
            bal += 2*amount
        elif bet_value == '1st12' or bet_value == '2nd12' or bet_value == '3rd12':
            bal += 3*amount
        elif bet_value in square_types[9:]:
            bal += 36*amount
        else: print("I don't even know how this would happen")
    return [bal, num]