
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def length(self):
        curr = self.head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        return length

register = {'dalambertUp1Down1': LinkedList(), 
            'dalambertUp1Down2': LinkedList(), 
            'dalambertUp1Down3': LinkedList(), 
                   'doubleDown': LinkedList(), 
                   'fibbonacci': LinkedList(), 
                        'evans': LinkedList(), 
                'thirdsFallacy': LinkedList()}


def showGambitStats():
    for system in register: # For each system type
        if register[system].isEmpty(): continue
        balances = []    # List of end balances, add once per simulation
        endBalances = 0   # Average end balance, add once per simulation
        maxBalances = 0   # Average max balance, add once per simulation
        totalSpins = 0   # Average no. of spins, add once per simulation
        totalWinChance = 0 # Average win chance, add once per spin
        rollsPlayed = 0   # Total no. of rolls played, add once per spin
        simulations = register[system].length()
        
        curr = register[system].head

        while curr is not None: # For each simulation in that system
            simulation = curr.data
            maxBalances += simulation[-1][3] 

            for spin in simulation: # For each spin in that simulation
                if spin == simulation[-1]: # If it's the last spin
                    balances.append(spin[1])
                    endBalances += spin[1]
                if spin[2] is None: continue
                rollsPlayed += 1
                totalWinChance += spin[2]

            totalSpins += len(curr.data)
            curr = curr.next

        balances.sort()

        print(f"Balances Len: {len(balances)}")
        print(f"{system.title()} System:\n",
              
            f"Average End Balance: {endBalances / simulations}\n",
            f"Average Win Chance: {totalWinChance / rollsPlayed}\n",
            f"Average Max Balance: {maxBalances / simulations}\n",
            f"Average Spins: {totalSpins / simulations}\n",
            f"Median End Balance: {balances[int(len(balances)/2)]}\n",
            f"Mode End Balance: {max(set(balances), key=balances.count)}\n",)
        
        input("[Press Enter to continue...]")
