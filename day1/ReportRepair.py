
def calcPartOne (expenses):
    for i in range(len(expenses)):
        for j in range (len(expenses)):
            if i != j:
                if expenses[i] + expenses[j] == 2020:
                    print('Part 1 product is: ' + str(expenses[i] * expenses[j]))
                    return

def calcPartTwo (expenses):
    for i in range(len(expenses)):
        for j in range (len(expenses)):
            for k in range (len(expenses)):
                if i != j and i != k and j != k:
                    if expenses[i] + expenses[j] + expenses[k] == 2020:
                        print('Part 2 product is: ' + str(expenses[i] * expenses[j] * expenses[k]))
                        return

if __name__ == '__main__':
    with open('input.txt') as f:
        expenses = [int(val) for val in f]
    calcPartOne(expenses)
    calcPartTwo(expenses)

