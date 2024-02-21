from spin import spin
from genStats import register

def testDalambert(downAmount, spins, startingBet, start, twelve = '2nd12'):
    old_balance = start; balance = start
    registerHold = []
    max_balance = balance
    won = 0
    bet = startingBet
    down = downAmount
    for i in range(1, spins+1):
        balance = spin(balance, bet, twelve)[0]
        if balance < 10*down:
            break

        # If you won, subtract 10 from bet
        if balance > old_balance:
            # reduce bet by 10-30% if won
            bet -= int(bet*0.1*down) if bet > 10*down else 0 # if not back to start, subtract ten * down amount
            (10*down) if bet > (10*down) else 0 # if not back to start, add ten * down amount
            won = 1

        # If you lost, increase bet by 10-30%
        elif balance < old_balance:
            bet += int(bet*0.1*down)
            if bet >= balance:
                bet = 10*down
            won = 0
        max_balance = max(max_balance, balance)
        registerHold.append([i, balance, won, max_balance]) # Spin no.,  balance, win/lose, max
        old_balance = balance
    
    # Add iteration details to register
    register[f'dalambertUp1Down{down}'].append(registerHold)