# import modules
from random import randint, randrange
from string import ascii_lowercase
from collections import OrderedDict, Counter

dictCnt = randrange(2, 11, 1)  # create a variable for a number of random dicts
dictList = []  # create a blank list for dicts

for i in range(dictCnt):
    # create dictCnt dicts with letter keys
    dictList.append(dict.fromkeys(ascii_lowercase[0:randint(2, 26)], 0))
for dictElement in dictList:
    for key, value in dictElement.items():  # iterate through every item of dicts in the list
        randValue = randint(0, 100)
        dictElement.update({key: randValue})  # populate dicts with random values
print('Created a list of dicts:\n ', dictList)

# get all keys from dicts in the list
duplicates = []
for d in dictList:
    for k, v in d.items():
        duplicates.append(k)

# get all duplicate keys from dicts in list
duplicates = ([item for item, count in Counter(duplicates).items() if count > 1])

# rename and concat all dicts
result = {}
for i in dictList:
    for k, v in i.items():
        if k in duplicates:
            result[k + '_' + str(dictList.index(i) + 1)] = v
        else:
            result[k] = v
print('Concatenated dicts with renamed keys:\n ', result)

# sorting the dict by values desc
result = OrderedDict(sorted(result.items(), key=lambda x: x[1], reverse=True))

# get first keys with max value
finalDict = {}
try:
    for i, v in result.items():
        if i[0] not in (x[0] for x in finalDict.keys()):
            finalDict[i] = v
    print('Final dict with max values:\n ', finalDict)
except IndexError:
    print('Index error')


