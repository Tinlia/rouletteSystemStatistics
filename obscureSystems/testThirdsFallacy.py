from spin import spin
from genStats import register
from dicts import squares
import math
history = []
twelves = {
        '1st12': 0,
        '2nd12': 0,
        '3rd12': 0,
        '0': 0,
        '00': 0
    }

def testThirds(down = 1, spins = 100, baseBet = 10, balance = 1000, twelve = '2nd12'):
    old_balance = balance
    max_balance = balance
    registerHold = []
    bet = baseBet
    num = ''
    betAgain = False # To bet again
    betRound = False # To signify a betting round    
    lossStreak = 0
    
    # Fill history with 100 spins
    for i in range(100):
        num = spin(balance, 0, '1st12')[1]
        twelves[squares[num][1]] += 1
        history.append(squares[num][1])         # Add 0, 00, 1st12, 2nd12, or 3rd12 to the history

    for i in range(1, spins+1):
        # Find the most common twelve in history
        if not betAgain: twelve = getTwelve()

        bet = baseBet
        if lossStreak > 3: bet = math.ceil(bet * 1.5)

        # If you can't afford the bet, break
        if balance < baseBet*down:
            break

        # If 12 is in the last ten rolls, bet on it
        if twelve not in history[-3:] or betAgain:
            balance,num = spin(balance, bet, twelve)
            betRound = True

        # If not, bet nothing
        else:
            balance,num = spin(balance, 0, twelve)
            betRound = False

        # Append the result to the history and wipe the first result
        history.append(squares[num][1])
        history.pop(0)

        # If you won
        if balance > old_balance:
            won = 1
            lossStreak = 0

            # If the round was a betting round, don't bet again
            if betRound:
                betAgain = False

        # If you lost
        elif balance < old_balance:
            won = 0
            lossStreak += 1

            # If the round was a betting round, bet again
            if betRound:
                betAgain = True
        
        else:
            won = None
        
        registerHold.append([i, balance, won, max(max_balance, balance)]) # Spin no., balance, win/lose, max
        old_balance = balance
    
    # Add simulation details to register
    register['thirdsFallacy'].append(data=registerHold)

def getTwelve():
    
    return max(twelves, key=twelves.get)
