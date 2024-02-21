register = {'dalambertUp1Down1': [], 'dalambertUp1Down2': [], 'dalambertUp1Down3': [], 'doubleDown': [], 'fibbonacci': [], 'evans': []}

def showGambitStats():
    # Fetch dalambertUp1Down1
    for system in register: # For each system type
        if register[system] == []: # If there are no iterations of that system
            continue
        balances = []  # List of end balances, add once per iteration
        avgEndBalance = 0 # Average end balance, add once per iteration
        totalWinChance = 0 # Average win chance, add once per spin
        totalAvgMaxBalance = 0 # 
        totalAvgSpins = 0

        for iteration in register[system]: # For each iteration of that system
            avgWinChance = 0
            avgMaxBalance = 0

            for spin in iteration: # For each spin in that iteration
                avgWinChance += spin[2]
                avgMaxBalance += spin[3]
                
                if spin == iteration[-1]: # If it's the last spin
                    balances.append(spin[1])
                    avgEndBalance += spin[1]

            avgMaxBalance /= len(iteration)
            totalWinChance += avgWinChance / len(iteration)
            totalAvgMaxBalance += avgMaxBalance
            totalAvgSpins += len(iteration)

        avgEndBalance /= len(register[system])
        totalWinChance /= len(register[system])
        totalAvgMaxBalance /= len(register[system])
        totalAvgSpins /= len(register[system])
        balances.sort()

        print(f"Balances Len: {len(balances)}")
        print(f"{system}:\nAverage End Balance: {avgEndBalance}\n",
              f"Average Win Chance: {totalWinChance}\n",
              f"Average Max Balance: {totalAvgMaxBalance}\n",
              f"Average Spins: {totalAvgSpins}\n",
              f"Median End Balance: {balances[int(len(balances)/2)]}\n",
              f"Mode End Balance: {max(set(balances), key=balances.count)}\n",)
        input("[Press Enter to continue...]")
