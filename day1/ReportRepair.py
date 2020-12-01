from itertools import combinations
from functools import reduce

def calc2020Product(expenses, nbrOfexpenses):
    for comb in combinations(expenses, nbrOfexpenses):
        if sum(comb) == 2020:
            return (reduce((lambda x, y: x * y), comb))

if __name__ == '__main__':
    with open('input.txt') as f:
        expenses = [int(val) for val in f]

    print(calc2020Product(expenses, 2))
    print(calc2020Product(expenses, 3))


