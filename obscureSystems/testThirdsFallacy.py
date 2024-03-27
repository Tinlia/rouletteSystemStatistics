from spin import spin
from genStats import register
from dicts import squares

history = []

def testThirds(down = 1, spins = 100, baseBet = 10, balance = 1000, twelve = '2nd12'):
    old_balance = balance
    max_balance = balance
    registerHold = []
    bet = baseBet
    num = ''
    betAgain = False # To bet again
    betRound = False # To signify a betting round
    

    # Fill history with 100 spins
    for i in range(100):
        num = spin(balance, 0, '1st12')[1]
        history.append(squares[num][1])         # Add 0, 00, 1st12, 2nd12, or 3rd12 to the history

    for i in range(1, spins+1):
        # Find the most common twelve in history
        twelve = getTwelve()

        # If you can't afford the bet, break
        if balance < baseBet*down:
            break

        # If 12 is in the last three rolls, bet on it
        if twelve in history[-3:] or betAgain:
            balance,num = spin(balance, bet, twelve)
            betRound = True

        # If not, bet nothing
        else:
            balance,num = spin(balance, 0, twelve)
            betRound = False

        # Append the result to the history and wipe the first result
        history.append(squares[num][1])
        history.pop(0)

        # If you won, decrease bet
        if balance > old_balance:
            bet -= baseBet*down 
            if bet < baseBet*down: bet = baseBet*down
            won = 1

            # If the round was a betting round, don't bet again
            if betRound:
                betAgain = False

        # If you lost, increase bet
        elif balance < old_balance:
            bet += baseBet*down
            if bet >= balance: bet = baseBet*down
            won = 0

            # If the round was a betting round, bet again
            if betRound:
                betAgain = True
        
        else:
            won = 0.5
            
        
        registerHold.append([i, balance, won, max(max_balance, balance)]) # Spin no., balance, win/lose, max
        old_balance = balance
    
    # Add simulation details to register
    register['thirdsFallacy'].append(registerHold)

def getTwelve():
    return max(set(history), key = history.count)
