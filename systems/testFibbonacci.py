from spin import spin
from genStats import register


def testFibbonacci(spins, baseBet, balance):
    old_balance = balance
    registerHold = []
    max_balance = balance
    bet = baseBet
    previousbet = 0
    for i in range(1, spins+1):
        
        balance = spin(balance, bet, '2nd12')[0]
        if balance < baseBet:
            break
        # If you won, go back to old bet
        if balance > old_balance:
            bet = baseBet
            won = 1

        # If you lost, add the previous bet to your current bet
        elif balance < old_balance:
            # If you can't afford the bet, go back to baseBet
            bet += previousbet
            won = 0
            if bet > balance:
                bet = baseBet
                previousbet = 0
            
        previousbet = bet
        registerHold.append([i, balance, won, max(max_balance, balance)]) # Spin no., balance, win/lose, max
        old_balance = balance
    
    # Add iteration details to register
    register['fibbonacci'].append(registerHold)
    