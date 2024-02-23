from spin import spin
from genStats import register

def testDalambert(downAmount = 1, spins = 100, baseBet = 10, balance = 1000, twelve = '2nd12'):
    old_balance = balance
    max_balance = balance
    registerHold = []
    bet = baseBet
    down = downAmount
    for i in range(1, spins+1):
        balance = spin(balance, bet, twelve)[0]
        if balance < baseBet*down:
            break

        # If you won, decrease bet
        if balance > old_balance:
            bet -= baseBet*down 
            if bet < baseBet*down: bet = baseBet*down
            won = 1

        # If you lost, increase bet
        elif balance < old_balance:
            bet += baseBet*down
            if bet >= balance: bet = baseBet*down
            won = 0
        
        registerHold.append([i, balance, won, max(max_balance, balance)]) # Spin no., balance, win/lose, max
        old_balance = balance
    
    # Add simulation details to register
    register[f'dalambertUp1Down{down}'].append(registerHold)