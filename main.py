# Roulette, by Tinlia
from genStats import showGambitStats
from systems.testFibbonacci import testFibbonacci
from systems.testDoubleDown import testDoubleDown
from systems.testDalambert import testDalambert
from obscureSystems.testEvans import testEvans
from obscureSystems.testThirdsFallacy import testThirds

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    suffix = f"({iteration}/{total} Simulations)"
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

# Title Screen
def plotResults(balance):
    from matplotlib import pyplot as plt
    from genStats import register

    for system in register:
        # Skip empty systems
        if register[system].isEmpty(): continue
        # Get the longest simulation (spins) and the number of simulations
        simulations = register[system].length()
        curr = register[system].head
        maxSpins = 0
        while curr is not None:
            maxSpins = max(len(curr.data), maxSpins)
            curr = curr.next

        # Fetch the avergae line
        xyAvg = {
            'x': [i for i in range(1, maxSpins+1)],
            'y': [[] for i in range(1, maxSpins+2)]
        }

        if input(f"Plot {system} system? (Y/N)").upper() != 'Y': continue
        
        curr = register[system].head

        while curr is not None:
            x = [0]; y=[balance];
            for spin in curr.data: # For each spin
                x.append(spin[0]); y.append(spin[1])
                xyAvg["y"][spin[0]].append(spin[1])

            plt.scatter(x,y, color='blue', s=1, alpha=0.01)
            curr = curr.next

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
            "[F] Fibbonacci System\n",
            "[G] Thirds Fallacy System")

        system = input("> ").upper()

        # Basic system dictionary
        syst = {
            'A' : 1,
            'B' : 2,
            'C' : 3,
            'D' : testDoubleDown,
            'E' : testEvans,
            'F' : testFibbonacci,
            'G' : testThirds
        }

        
        if system.upper() in ['A', 'B', 'C']:
            down = syst[system.upper()]
            spins = int(input(f"dAlembert System (up 1 down {down}) selected. How many spins?\n> "))
            balance = int(input("What is your starting balance?\n> "))
            bet = int(input("What is your starting bet?\n> "))
            simulations = int(input("How many simulations?\n> "))
            
            for i in range(simulations):
                testDalambert(down, spins, bet, balance)        
            
        elif system.upper() in ['D', 'E', 'F']: 
            
            testType = syst[system.upper()]
            spins = int(input(f"System selected. How many spins?\n> "))
            balance = int(input("What is your starting balance?\n> "))
            bet = int(input("What is your starting bet?\n> "))
            simulations = int(input("How many simulations?\n> "))

            # Run simulations
            for i in range(simulations):
                testType(spins, bet, balance)

        elif system.upper() == 'G':
            down = int(input("Thirds Fallacy System selected. What is your down multiplier (Up 1 down n)?\n> "))
            spins = int(input("How many spins?\n> "))
            balance = int(input("What is your starting balance?\n> "))
            bet = int(input("What is your starting bet?\n> "))
            simulations = int(input("How many simulations?\n> "))
            
            for i in range(simulations):
                testThirds(down, spins, bet, balance)


        else:
            print("Invalid Selection.\n")
            input("[Press Enter to continue...]")

    elif selection == 'S': showGambitStats()
    elif selection == 'P': plotResults(balance)
    elif selection == 'T':
        print("Running Test Cases...")
        #       [spins, bet, balance, simulations]
        test = [300,    10,    1000,     1000]

        [spins, bet, balance, simulations] = test
        for i in range(simulations):
            printProgressBar(i, simulations)
            #testDalambert(1, spins, bet, balance)
            #testDalambert(2, spins, bet, balance)
            #testDalambert(3, spins, bet, balance)
            #testDoubleDown(spins, bet, balance)
            #testEvans(spins, bet, balance)
            #testFibbonacci(spins, bet, balance)
            testThirds(1, spins, bet, balance)
        printProgressBar(simulations, simulations)
        showGambitStats()
        plotResults(balance)


    

    elif selection == 'E':
        print("Thank you for playing!")
        break

    else:
        print("\n\n\n\nInvalid Selection.\n")
        input("[Press Enter to continue...]")

