
if __name__ == '__main__':
    with open('input.txt') as f:
        input = [line.strip() for line in f]

    intInput = [int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for line in input]
    intInput.sort()
    print('Highest seat ID: ', intInput[-1])

    for i in range(len(intInput)):
        if intInput[i] + 2 == intInput[i + 1]:
            print('Your seat ID: ', intInput[i] + 1)
            break

