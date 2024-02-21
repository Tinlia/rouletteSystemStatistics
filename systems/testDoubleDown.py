from spin import spin
from genStats import register

def testDoubleDown(spins, baseBet, balance):
    old_balance = balance
    registerHold = []
    max_balance = balance
    bet = baseBet
    for i in range(1, spins+1):
        balance = spin(balance, bet, 'even')[0]
        if balance < baseBet:
            break

        # If you won, go back to old bet
        if balance > old_balance:
            bet = baseBet
            old_balance = balance
            won = 1

        # If you lost, double your bet
        elif balance < old_balance:
            bet *= 2
            old_balance = balance
            won = 0
            # If you can't afford the bet, go back to baseBet
            if bet > balance:
                bet = baseBet

        max_balance = max(max_balance, balance)
        registerHold.append([i, balance, won, max_balance]) # Spin no., balance, win/lose
        old_balance = balance
    
    # Add iteration details to register
    register['doubleDown'].append(registerHold)
    