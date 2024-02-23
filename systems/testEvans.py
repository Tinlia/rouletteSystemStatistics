from dicts import squares
from genStats import register
from spin import spin

def testEvans(spins, baseBet, balance, num = '1'):
    old_balance = balance
    max_balance = balance
    registerHold = []
    bet = baseBet
    previousColour = 'red'
    for i in range(1, spins+1):
        numColor = squares[num][0]
        bet = 0 if numColor == previousColour else baseBet # Bet only when the colour changes
        if numColor != previousColour:
            previousColour = numColor
        [balance, num] = spin(balance, bet, 'red' if squares[num][0] == 'black' else 'black')
        
        if balance < baseBet:
            break

        # If you won
        if balance > old_balance:
            won = 1
        # If you lost
        elif balance < old_balance:
            won = 0
        else:
            won = 0.5
        
        max_balance = max(max_balance, balance)
        registerHold.append([i, balance, won, max_balance]) # Spin no., balance, win/lose
        old_balance = balance
    
    # Add simulation details to register
    register['evans'].append(registerHold)
    