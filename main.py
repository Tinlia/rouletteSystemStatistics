# Roulette, by Tinlia
from genStats import showGambitStats
from systems.testFibbonacci import testFibbonacci
from systems.testDoubleDown import testDoubleDown
from systems.testDalambert import testDalambert
from systems.testEvans import testEvans

# Title Screen
def plotResults(balance):
    from matplotlib import pyplot as plt
    from genStats import register

    for system in register:
        if register[system] == []:
            continue
        if input(f"Plot {system} system? (Y/N)").upper() != 'Y':
            continue
        for iter in register[system]: # For each iteration
            x = [0]; y=[balance]
            for spinNo in iter: # For each spin
                x.append(spinNo[0])
                y.append(spinNo[1])
            plt.plot(x,y)
        plt.title(f"The {system} system")
        plt.xlabel("Spin Number")
        plt.ylabel("Balance")
        plt.show()

while True:
    print(f"\n\n\n\nBalance: $Null\n")
    print("Please Select an option below:\n",
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
            iterations = int(input("How many iterations?\n> "))
            
            for i in range(iterations):
                testDalambert(down, spins, bet, balance)
            
        elif system.upper() == 'D' or system.upper() == 'E' or system.upper() == 'F': 
            
            testType = testDoubleDown if system.upper() == 'D' else testEvans if system.upper() == 'E' else testFibbonacci
            spins = int(input(f"System selected. How many spins?\n> "))
            balance = int(input("What is your starting balance?\n> "))
            bet = int(input("What is your starting bet?\n> "))
            iterations = int(input("How many iterations?\n> "))
            for i in range(iterations):
                testType(spins, bet, balance)

        else:
            print("Invalid Selection.\n")
            input("[Press Enter to continue...]")

    elif selection == 'S': showGambitStats()
        
    elif selection == 'P':
        plotResults(balance)

    elif selection == 'T':
        print("Running Test Cases...")
        [spins, bet, balance, iterations, showPrints] = [100, 10, 1000, 100, False]
        for i in range(iterations):
            if showPrints: print("[1/6] dAlembert System (1:1)")
            testDalambert(1, spins, bet, balance)

            if showPrints: print("[2/6] dAlembert System (1:2)")
            testDalambert(2, spins, bet, balance)

            if showPrints: print("[3/6] dAlembert System (1:3)")
            testDalambert(3, spins, bet, balance)

            if showPrints: print("[4/6] Double Down System")
            testDoubleDown(spins, bet, balance)

            if showPrints: print("[5/6] Evans System")
            testEvans(spins, bet, balance)

            if showPrints: print("[6/6] Fibbonacci System")
            testFibbonacci(spins, bet, balance)

        if showPrints: print("Displaying Stats...")
        showGambitStats()

        if showPrints: print("Plotting Results...")
        plotResults(balance)

    elif selection == 'E':
        print("Thank you for playing!")
        break

    else:
        print("Invalid Selection.\n")
        input("[Press Enter to continue...]")
