def countYesAnswers(input):
    totalCommon, totalUnique = 0, 0
    groupAnswers = []

    for line in input:
        personAnswers = set()
        if len(line):
            for char in line:
                personAnswers.add(char)
            groupAnswers.append(personAnswers)
        else:
            totalCommon += len(groupAnswers[0].intersection(*groupAnswers))
            totalUnique += len(groupAnswers[0].union(*groupAnswers))
            groupAnswers = []

    return totalUnique, totalCommon



if __name__ == '__main__':
    with open('input.txt') as f:
        input = [line.strip() for line in f]

    input.append('') # Used to complete the last group

    print('Part 1: %d\nPart 2: %d' % countYesAnswers(input))
