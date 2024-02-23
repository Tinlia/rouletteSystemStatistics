# Roulette, by Tinlia
from genStats import showGambitStats
from systems.testFibbonacci import testFibbonacci
from systems.testDoubleDown import testDoubleDown
from systems.testDalambert import testDalambert
from systems.testEvans import testEvans

# Title Screen
def plotResults(balance, spins, simulations):
    from matplotlib import pyplot as plt
    from genStats import register

    for system in register:
        xyAvg = {
            'x': [i for i in range(1, spins+1)],
            'y': [[] for i in range(1, spins+2)]
        }

        if register[system] == []: continue
        if input(f"Plot {system} system? (Y/N)").upper() != 'Y': continue
            
        for sim in register[system]: # For each simulation
            x = [0]; y=[balance];
            for spin in sim: # For each spin
                x.append(spin[0]); y.append(spin[1])
                xyAvg["y"][spin[0]].append(spin[1])
            plt.scatter(x,y, color='blue', s=0.2)

        plt.plot(xyAvg['x'], [sum(xyAvg['y'][i])/simulations for i in range(1, spins+1)], color='red', label='Average')
        plt.title(f"{system} system")
        plt.xlabel("Spin Number")
        plt.ylabel("Balance")
        plt.legend()
        plt.grid(axis='y', which='both')
        plt.show()

while True:
    print("\n\n\n\nPlease Select an option below:\n",
          "[R]un Tests\n",
          "[S]ystem Stats\n",
          "[P]lot Results\n",
          "[T]est Cases\n",
          "[E]xit")
    selection = input("> ").upper()
    balance = 0
    # Starts Roulette, passing the current balance and wins
    if selection == 'R':
        print("\n\n\n\nPlease Choose a System to test:\n",
            "[A] dAlembert System (up 1 down 1)\n",
            "[B] dAlembert System (up 1 down 2)\n",
            "[C] dAlembert System (up 1 down 3)\n",
            "[D] Double Down System (Double on loss)\n",
            "[E] Evans System\n",
            "[F] Fibbonacci System\n")

        system = input("> ").upper()
        
        if system.upper() == 'A' or system.upper() == 'B' or system.upper() == 'C':
            down = 1 if system.upper() == 'A' else 2 if system.upper() == 'B' else 3
            spins = int(input(f"dAlembert System (up 1 down {down}) selected. How many spins?\n> "))
            balance = int(input("What is your starting balance?\n> "))
            bet = int(input("What is your starting bet?\n> "))
            simulations = int(input("How many simulations?\n> "))
            
            for i in range(simulations):
                testDalambert(down, spins, bet, balance)
            
        elif system.upper() == 'D' or system.upper() == 'E' or system.upper() == 'F': 
            
            testType = testDoubleDown if system.upper() == 'D' else testEvans if system.upper() == 'E' else testFibbonacci
            spins = int(input(f"System selected. How many spins?\n> "))
            balance = int(input("What is your starting balance?\n> "))
            bet = int(input("What is your starting bet?\n> "))
            simulations = int(input("How many simulations?\n> "))
            for i in range(simulations):
                testType(spins, bet, balance)

        else:
            print("Invalid Selection.\n")
            input("[Press Enter to continue...]")

    elif selection == 'S': showGambitStats()
    elif selection == 'P': plotResults(balance)
    elif selection == 'T':
        print("Running Test Cases...")
        # Suggested Test Cases:
        test  = [100,  10, 10000, 10000]
        testA = [100,  10,  1000, 1000]
        testB = [200,  10,  2000, 1000]
        testC = [100,   1,   100, 1000]
        testD = [100,   2,   100, 1000]
        testE = [100, 100,  1000, 1000]
        [spins, bet, balance, simulations] = test
        for i in range(simulations):
            testDalambert(1, spins, bet, balance)
            testDalambert(2, spins, bet, balance)
            testDalambert(3, spins, bet, balance)
            testDoubleDown(spins, bet, balance)
            testEvans(spins, bet, balance)
            testFibbonacci(spins, bet, balance)
        showGambitStats()
        plotResults(balance, spins, simulations)

    elif selection == 'E':
        print("Thank you for playing!")
        break

    else:
        print("\n\n\n\nInvalid Selection.\n")
        input("[Press Enter to continue...]")
