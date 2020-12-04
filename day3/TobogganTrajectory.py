
def takeStep(step, x, y):
    x += step[0]
    y += step[1]
    return x, y

def traverseForest(lines):
    p1TreeCount, treeMulTot  = 0, 1
    differentSteps = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    mod = len(lines[0])

    for step in differentSteps:
        x, y, treeCount = 0, 0, 0
        while y < len(lines) - 1:
            x, y = takeStep(step, x, y)
            if lines[y][x % mod] == '#':
                treeCount += 1
        if step == [3,1]:
            p1TreeCount = treeCount
        treeMulTot *= treeCount

    return p1TreeCount, treeMulTot

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    
    print('Obstructing trees (p1 and p2): ' + str(traverseForest(lines)))
