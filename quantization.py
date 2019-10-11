import math

# samples = [550, 600, -100, 150, -300, 900, 0, 850]
# bitLevel = 2

samples = []
bitLevel = 0

userInput = input("Enter samples:  ")
temp = ""
for i in range(0, len(userInput)):
    if userInput[i] == " ":
        samples += [int(temp)]
        temp = ""
    else:
        temp += userInput[i]
    if i == len(userInput)-1:
        samples += [int(temp)]

bitLevel = int(input("Enter bit level:  "))

numberOfLevels = int(math.pow(2, bitLevel))
minNum = 0
maxNum = 0

#find largest and smallest num
for i in range(0, len(samples)):
    if i == 0:
        minNum = samples[i]
        maxNum = samples[i]

    if samples[i] < minNum:
        minNum = samples[i]
    elif samples[i] > maxNum:
        maxNum = samples[i]

#find range and delta
sampleRange = maxNum - minNum
sampleStep = int(sampleRange / numberOfLevels)

#find the level of samples
levelsOfSamples = []
for j in range(0, numberOfLevels):
    temp = []
    for k in range(0, 2):
        temp += [minNum]
        tempNump = minNum + sampleStep
        if k != 1:
            minNum = tempNump
    temp += [str("{0:0" + str(bitLevel) + "b}").format(j)]
    levelsOfSamples += [temp]

#find the digital form
digitalForm = []
for i in range(0, len(samples)):
    if samples[i] == maxNum:
        digitalForm += [levelsOfSamples[numberOfLevels - 1][2]]
    else:
        for j in range(0, len(levelsOfSamples)):
            if levelsOfSamples[j][0] <= samples[i] < levelsOfSamples[j][1]:
                digitalForm += [levelsOfSamples[j][2]]

#find the analog form
reproducedAnalog = []
for i in range(0, len(digitalForm)):
    for j in range(0, len(levelsOfSamples)):
        if digitalForm[i] == levelsOfSamples[j][2]:
            result = int((levelsOfSamples[j][0] + levelsOfSamples[j][1]) / 2)
            reproducedAnalog += [result]

#erorr
error = 0
for i in range(0, len(reproducedAnalog)):
    error += int(math.fabs(reproducedAnalog[i] - samples[i]))

print("Level, Analog, Digital: ",levelsOfSamples)
print("Digital Form: ",digitalForm)
print("Reproduced Analog: ",reproducedAnalog)
print("Total Error: ",error)
