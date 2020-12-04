
def cleanInput(line):
    policyAmount, policyChar, password = line.split()
    policyAmount = list(map(int, policyAmount.split('-')))
    policyChar = policyChar.strip(':')
    return policyAmount, policyChar, password

def evaluatePart1(policyAmount, policyChar, password):
    policyCount = password.count(policyChar)
    return 1 if policyCount >= policyAmount[0] and policyCount <= policyAmount[1] else 0

def evaluatePart2(policyAmount, policyChar, password):
    b1 = password[policyAmount[0] - 1] == policyChar
    b2 = password[policyAmount[1] - 1] == policyChar
    return b1 ^ b2

def countValidPasswords(lines):
    p1 = 0
    p2 = 0
    for line in lines:
        policyAmount, policyChar, password = cleanInput(line)
        p1 += evaluatePart1(policyAmount, policyChar, password)
        p2 += evaluatePart2(policyAmount, policyChar, password)
    return p1, p2



if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    print('Valid passwords: ' + str(countValidPasswords(lines)))
