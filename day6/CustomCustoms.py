def countDistinctYes(input):
    totalDistinct = 0
    uniqueQuestions = set()

    for line in input:
        if len(line):
            for char in line:
                uniqueQuestions.add(char)
        else:
            totalDistinct += len(uniqueQuestions)
            uniqueQuestions = set()

    return totalDistinct

def countCommonYes(input):
    totalCommon = 0
    groupAnswers = []

    for line in input:
        personAnswers = set()
        if len(line):
            for char in line:
                personAnswers.add(char)
            groupAnswers.append(personAnswers)
        else:
            totalCommon += len(groupAnswers[0].intersection(*groupAnswers))
            groupAnswers = []

    return totalCommon



if __name__ == '__main__':
    with open('input.txt') as f:
        input = [line.strip() for line in f]

    input.append('') # Used to complete the last group

    print('Part 1: ', countDistinctYes(input))
    print('Part 2: ', countCommonYes(input))
