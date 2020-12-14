
def cleanInput(lines):
    bagMap = {}
    for line in lines:
        line = line.replace('bags', 'bag')
        line = line.replace(' bag contain ', '-')
        line = line.replace(' bag, ', '-')
        line = line.replace(' bag.', '')
        bags = line.split('-')
        bagContent = []
        if 'no other' not in line:
            for bag in bags[1:]:
                bagContent.append({bag[2:]:int(bag[:1])})
        bagMap[bags[0]] = bagContent
    return bagMap

def countInternal(key, bagMap):
    if key == 'shiny gold':
        return True
    elif key == 'no other':
        return False
    for bagContent in bagMap[key] :
        for bag in bagContent.keys():
            if countInternal(bag, bagMap):
                return True
    return False

def countBagsResultingInGoldenBag(bagMap):
    count = 0
    for bag in bagMap.keys():
        count += countInternal(bag, bagMap) if bag != 'shiny gold' else 0
    return count

bagContentMem = {}
def countBagContent(bag, bagMap):
    global bagContentMem
    total = 0
    for bagAndAmount in bagMap[bag]:
        for key in bagAndAmount.keys():
            total += bagAndAmount[key] + bagAndAmount[key] * countBagContent(key, bagMap)
    return total

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]
    bagMap = cleanInput(lines)

    print ('Nbr of bags that can contain golden bag: ', countBagsResultingInGoldenBag(bagMap))
    print('One shiny gold bag must contain: ', countBagContent('shiny gold', bagMap))

