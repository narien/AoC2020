
if __name__ == '__main__':
    with open('input.txt') as f:
        pattern = str.maketrans("FBLR", "0101")
        intInput = [int(line.strip().translate(pattern), 2) for line in f]

    intInput.sort()
    print('Highest seat ID: ', intInput[-1])

    for i in range(len(intInput)):
        if intInput[i] + 2 == intInput[i + 1]:
            print('Your seat ID: ', intInput[i] + 1)
            break

