import re

def cleanInput(lines):
    bagMap = {}
    for line in lines:
        line = line.replace('bags', 'bag')
        line = line.replace(' bag contain ', '-')
        line = line.replace(' bag, ', '-')
        line = line.replace(' bag.', '')
        line = re.sub(r'[0-9] +', '', line)
        bags = line.split('-')
        bagMap[bags[0]] = set(bags[1:])
    return bagMap

def countInternal(key, bagMap):
    if key == 'shiny gold':
        return True
    elif key == 'no other':
        return False
    for bag in bagMap[key]:
        if countInternal(bag, bagMap):
            return True
    return False



def countBagsResultingInGoldenBag(bagMap):
    count = 0
    for bag in bagMap.keys():
        count += countInternal(bag, bagMap) if bag != 'shiny gold' else 0
    return count

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]
    bagMap = cleanInput(lines)


    print ('Nbr of bags that can contain golden bag: ', countBagsResultingInGoldenBag(bagMap))

