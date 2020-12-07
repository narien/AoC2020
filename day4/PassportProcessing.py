import re

def special_match(strg, search=re.compile(r'[^a-f0-9]').search):
    return not bool(search(strg))

def isDigits(strg, search=re.compile(r'[^0-9]').search):
    return not bool(search(strg))

def buildRegister(input):
    passportRegister = []
    newEntry = dict()
    for word in input:
        if len(word):
            key, val = word.split(':')
            newEntry[key] = val
        else:
            passportRegister.append(newEntry)
            newEntry = dict()
    return passportRegister

def validNumber(year, lowRange, HighRange):
    return lowRange < int(year) < HighRange

def validHgt(hgt):
    if hgt[-2:] == 'cm':
        return validNumber(hgt[:-2], 149, 194)
    elif hgt[-2:] == 'in':
        return validNumber(hgt[:-2], 58, 77)
    return False 

def validHcl(hcl):
    if hcl[0] == '#' and len(hcl[1:]) == 6:
        return special_match(hcl[1:])
    return False

def validEcl(ecl):
    return ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def validPid(pid):
    return len(pid) == 9 and isDigits(pid)

def validContent(passport):
    if not validNumber(passport['byr'], 1919, 2003):
        return False
    if not validNumber(passport['iyr'], 2009, 2021):
        return False
    if not validNumber(passport['eyr'], 2019, 2031):
        return False
    if not validHgt(passport['hgt']):
        return False
    if not validHcl(passport['hcl']):
        return False
    if not validEcl(passport['ecl']):
        return False
    if not validPid(passport['pid']):
        return False
    return True

def countValidPassports(register):
    validHeaders = 0
    validContents = 0
    for passport in register:
        if {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.issubset(passport):
            validHeaders += 1
            if validContent(passport):
                validContents += 1
    return validHeaders, validContents


if __name__ == '__main__':
    with open('input.txt') as f:
        input = [line.strip() for line in f]
    cleanedInput = []
    for val in input:
        if len(val):
            cleanedInput += val.split()
        else:
            cleanedInput.append(val)
    cleanedInput.append('') # needed to add last passport

    register = buildRegister(cleanedInput)
    print('Part 1: %d\nPart 2: %d' % (countValidPassports(register)))


