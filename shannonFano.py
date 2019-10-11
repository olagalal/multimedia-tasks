import math

# get division index to divide list to left and right
def dividerFunc(orderedListOfSequence):
    oldDecision = 0
    for i in range(0, len(orderedListOfSequence)):
        oldDecision += orderedListOfSequence[i][1]
    divider = 0
    for i in range(0, len(orderedListOfSequence)):
        divider += orderedListOfSequence[i][1]
        dividerDecision = 0
        for j in range(i + 1, len(orderedListOfSequence)):
            dividerDecision += orderedListOfSequence[j][1]
        newDecision = math.fabs(dividerDecision - divider)
        if newDecision < oldDecision:
            oldDecision = newDecision
        elif newDecision >= oldDecision:
            return i


# sequence = "acabadadeaabbaaaedcacdeaaabcdbbedcbacae"
# sequence = "bleiatsnblbe"
def shanon(sequence):
    sequenceList = list(sequence)

    # order character
    mapOfSequence = {sequenceList[0]: 1}
    for i in range(1, len(sequenceList)):
        if sequenceList[i] != sequenceList[i - 1] and sequenceList[i] not in mapOfSequence:
            mapOfSequence[sequenceList[i]] = 1
        else:
            mapOfSequence[sequenceList[i]] = mapOfSequence.get(sequenceList[i]) + 1

    orderedListOfSequence = sorted(mapOfSequence.items(), key=lambda x: x[1], reverse=True)
    print(orderedListOfSequence)
    # get char code
    mapOfChars = {}
    for i in range(0, len(orderedListOfSequence)):
        mapOfChars[orderedListOfSequence[i][0]] = "0"

    leftList = []
    for i in range(0, dividerFunc(orderedListOfSequence)):
        leftList += [orderedListOfSequence[i]]
    for k in range(0, len(leftList)):
        mapOfChars[leftList[k][0]] = "0"
    rightList = []
    for i in range(dividerFunc(orderedListOfSequence), len(orderedListOfSequence)):
        rightList += [orderedListOfSequence[i]]
    for k in range(0, len(rightList)):
        mapOfChars[rightList[k][0]] = "1"

    containerList = [leftList, rightList]
    containerListLength = len(containerList)
    containerListLengthCounter = 0
    n = 0
    while True:
        if len(containerList[n]) > 1:
            currentList = containerList[n]
            leftList = []
            for j in range(0, dividerFunc(currentList)):
                leftList += [currentList[j]]
            for k in range(0, len(leftList)):
                mapOfChars[leftList[k][0]] += "0"
            rightList = []
            for j in range(dividerFunc(currentList), len(currentList)):
                rightList += [currentList[j]]
            for k in range(0, len(rightList)):
                mapOfChars[rightList[k][0]] += "1"
            containerList += [leftList]
            containerList += [rightList]
            containerListLength = len(containerList)
        containerListLengthCounter += 1
        n += 1
        if containerListLength == containerListLengthCounter:
            break
    print(mapOfChars)

shanon(input("Enter the sequence:  "))