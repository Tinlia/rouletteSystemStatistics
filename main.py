# Roulette, by Evan "Tinlia" Kimpton

import random
import time
from dicts import square_types, squares

history = []
temphist = ""
top_twelve = '1st12'
last_bet = 10
name = ""

twelves = {'1st12': '0', '2nd12': '0', '3rd12': '0'}

register = {'dalambertUp1Down1': [], 'dalambertUp1Down2': [], 'dalambertUp1Down3': [], 'doubleDown': []}

for item in history:
    if item == '1st12':
        twelves['1st12'] += 1
    elif item == '2nd12':
        twelves['2nd12'] += 1
    elif item == '3rd12': 
        twelves['3rd12'] += 1

def showGambitStats():
    # Fetch dalambertUp1Down1
    for system in register: # For each system type
        if register[system] == []: # If there are no iterations of that system
            continue
        totalAvgEndBalance = 0
        totalWinChance = 0
        totalAvgMaxBalance = 0
        totalAvgSpins = 0
        for iteration in register[system]: # For each iteration of that system
            avgEndBalance = 0
            avgWinChance = 0
            avgMaxBalance = 0
            spins = 0
            for spin in iteration: # For each spin in that iteration
                avgEndBalance += spin[1]
                avgWinChance += spin[2]
                avgMaxBalance += spin[3]
                spins += 1
            avgEndBalance /= spins
            avgWinChance /= spins
            avgMaxBalance /= spins
            totalAvgEndBalance += avgEndBalance
            totalWinChance += avgWinChance
            totalAvgMaxBalance += avgMaxBalance
            totalAvgSpins += spins
        totalAvgEndBalance /= len(register[system])
        totalWinChance /= len(register[system])
        totalAvgMaxBalance /= len(register[system])
        totalAvgSpins /= len(register[system])
        print(f"{system}:\n\tAverage End Balance: {totalAvgEndBalance}\n\tAverage Win Chance: {totalWinChance}\n\tAverage Max Balance: {totalAvgMaxBalance}\n\tAverage Spins: {totalAvgSpins}\n")
        input("Press Enter to continue...")
            

def spin(bal, amount, bet_value):
    print(f"Spinning the wheel with a bet of ${amount} on {bet_value}! Current Balance is ${bal}.")
    # Subtract amount from balance
    bal -= amount
    # Roll a random choice from the squares dict
    selected_square = list(random.choice(list(squares.items())))
    # Announce the square chosen
    num = selected_square[0]
    num_values = selected_square[1]

    # Add roll info into a history list
    for value in num_values:
        history.append(value)

    # If there are more than 100 rolls in the history list, pop the oldest 5
    if len(history) > 500:
        for i in range(5):
            history.pop(0)

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
        print("You've won!")
    return bal

def testDalambert(down, spins, bet, balance):
    old_balance = balance
    registerHold = []
    max_balance = balance
    for i in range(1, spins+1):
        top_twelve = max(twelves, key=twelves.get)
        balance = spin(balance, bet, top_twelve)
        if balance < 10*down:
            print(f"You've gone bankrupt on spin {i}.")
            break

        # If you won, subtract 10 from bet
        if balance > old_balance:
            bet -= (10*down) if bet > (10*down) else 0 # if not back to start, add ten * down amount
            print(f"You've won! Bet is now {bet} and balance is {balance}.")
            won = 1

        # If you lost, add 10 to bet
        elif balance < old_balance:
            if bet >= balance:
                bet = 10
            else:
                bet += 10
            won = 0
        max_balance = max(max_balance, balance)
        registerHold.append([i, balance, won, max_balance]) # Spin no.,  balance, win/lose, max
        old_balance = balance
    
    # Add iteration details to register
    register[f'dalambertUp1Down{down}'].append(registerHold)
    with open('playerfile.txt', 'w') as player_file:
        player_file.write(f"{name}\n{balance}\n{wins}\n{' '.join(history)}")

def testDoubleDown(spins, baseBet, balance):
    old_balance = balance
    registerHold = []
    max_balance = balance
    bet = baseBet
    for i in range(1, spins+1):
        balance = spin(balance, bet, 'even')
        if balance < baseBet:
            print(f"You've gone bankrupt on spin {i}.")
            break

        # If you can't afford the bet, go back to baseBet
        if bet > balance:
            bet = baseBet

        # If you won, go back to old bet
        if balance > old_balance:
            bet = baseBet
            print(f"You've won! Bet is now {bet} and balance is {balance}.")
            old_balance = balance
            won = 1

        # If you lost, double your bet
        elif balance < old_balance:
            bet *= 2
            old_balance = balance
            won = 0
        max_balance = max(max_balance, balance)
        registerHold.append([i, balance, won, max_balance]) # Spin no., balance, win/lose
        old_balance = balance
    
    # Add iteration details to register
    register['doubleDown'].append(registerHold)
    with open('playerfile.txt', 'w') as player_file:
        player_file.write(f"{name}\n{balance}\n{wins}\n{' '.join(history)}")

# Player initializing
with open('playerfile.txt', 'w') as player_file:
    name = "Vinci"; balance = 1000; wins = 0; history = []

# Title Screen
while True:
    with open('playerfile.txt', 'r') as player_file:
        name = player_file.readline().strip('\n')
        balance = player_file.readline().strip('\n')
        wins = player_file.readline().strip('\n')
        history = list(player_file.readline().split(' '))
        history.pop()
    
    print(f"\n\n\n\nBalance: ${balance}\n")
    print("Please Select an option below:\n",
          "[R]un Tests\n",
          "[S]ystem Stats\n",
          "[P]lot Results\n",
          "[C]redits\n",
          "[E]xit")
    selection = input("> ").upper()

    # Starts Roulette, passing the current balance and wins
    
    if selection == 'R':
        print("\n\n\n\nPlease Choose a System to test:\n",
            "[A] dAlembert System (up 1 down 1)\n",
            "[B] dAlembert System (up 1 down 2)\n",
            "[C] dAlembert System (up 1 down 3)\n",
            "[D] Double Down System (Double on loss)\n")
        system = input("> ").upper()
        
        if system.upper() == 'A' or system.upper() == 'B' or system.upper() == 'C':
            down = 1 if system.upper() == 'A' else 2 if system.upper() == 'B' else 3
            spins = int(input(f"dAlembert System (up 1 down {down}) selected. How many spins?\n> "))
            balance = int(input("What is your starting balance?\n> "))
            bet = int(input("What is your starting bet?\n> "))
            iterations = int(input("How many iterations?\n> "))
            for i in range(iterations):
                testDalambert(down, spins, bet, balance)
            
        elif system.upper() == 'D':
            spins = int(input(f"Double Down System selected. How many spins?\n> "))
            balance = int(input("What is your starting balance?\n> "))
            bet = int(input("What is your starting bet?\n> "))
            iterations = int(input("How many iterations?\n> "))
            for i in range(iterations):
                testDoubleDown(spins, bet, balance)

        else:
            print("Invalid Selection.\n")
            time.sleep(2)

    elif selection == 'S':
        showGambitStats()

    elif selection == 'P':
        from matplotlib import pyplot as plt

        for system in register:
            if register[system] == []:
                continue
            check = input(f"Plot {system} system? (Y/N)").upper()
            if check != 'Y':
                continue
            for iter in register[system]: # For each iteration
                print(f"Plotting Iteration...")
                x = []; y=[]
                for spinNo in iter: # For each spin
                    x.append(spinNo[0])
                    y.append(spinNo[1])
                    print(f"\tPlotting ({spinNo[0]}, {spinNo[1]})")
                plt.plot(x,y)
            plt.title(f"The {system} system")
            plt.xlabel("Spin Number")
            plt.ylabel("Balance")
            plt.show()

    elif selection == 'C':
        print(f"\n\n\n\n\n\n\n\nCredits:\n\tRoulette Systems Test V1, created by Tinlia\n")
        time.sleep(3)

    elif selection == 'E':
        print("Thank you for playing!")
        break

    else:
        print("Invalid Selection.\n")
        time.sleep(3)
