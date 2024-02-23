register = {'dalambertUp1Down1': [], 'dalambertUp1Down2': [], 'dalambertUp1Down3': [], 'doubleDown': [], 'fibbonacci': [], 'evans': []}

def showGambitStats():
    for system in register: # For each system type
        if register[system] == []: continue
        balances = []    # List of end balances, add once per simulation
        endBalances = 0   # Average end balance, add once per simulation
        maxBalances = 0   # Average max balance, add once per simulation
        totalSpins = 0   # Average no. of spins, add once per simulation
        totalWinChance = 0 # Average win chance, add once per spin
        simulations = len(register[system])

        for simulation in register[system]: # For each simulation in that system
            maxBalances += simulation[-1][3] 

            for spin in simulation: # For each spin in that simulation
                totalWinChance += spin[2]
                
                if spin == simulation[-1]: # If it's the last spin
                    balances.append(spin[1])
                    endBalances += spin[1]

            totalSpins += len(simulation)

        balances.sort()

        print(f"Balances Len: {len(balances)}")
        print(f"{system.title()} System:\n",
              
            f"Average End Balance: {endBalances / simulations}\n",
            f"Average Win Chance: {totalWinChance / totalSpins}\n",
            f"Average Max Balance: {maxBalances / simulations}\n",
            f"Average Spins: {totalSpins / simulations}\n",
            f"Median End Balance: {balances[int(len(balances)/2)]}\n",
            f"Mode End Balance: {max(set(balances), key=balances.count)}\n",)
        
        input("[Press Enter to continue...]")
