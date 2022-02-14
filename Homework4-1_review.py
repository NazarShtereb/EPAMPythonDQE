# import modules
from random import randint, randrange
from string import ascii_lowercase
from collections import OrderedDict, Counter
from logging import exception


# create a blank list for dicts
def create_list(dictCnt=3, kCnt=5, vStart=0, vEnd=10):
    """
        Create a blank list for dicts

        Parameters:
        dictCnt (int): Description of dictCnt
        kCnt (int): Description of kCnt
        vStart (int): Description of vStart 
        vEnd (int): Description of vEnd

        Returns:
        list of dictionaries: Description of returning value
    """
    try:
        dictCnt = dictCnt  # create a variable for a number of random dicts
        dictList = []
        for i in range(dictCnt):
            # create dictCnt dicts with letter keys
            dictList.append(dict.fromkeys(ascii_lowercase[0:kCnt], 0))
        for dictElement in dictList:
            for key, value in dictElement.items():  # iterate through every item of dicts in the list
                randValue = randint(vStart, vEnd)
                dictElement.update({key: randValue})  # populate dicts with random values
        print('Created a list of dicts:\n ', dictList)
        return dictList
    except TypeError:
        exception('create_list. Incorrect type of parameters')
    except ValueError:
        exception('create_list. Incorrect values')


# get all keys from dicts in the list
def get_duplicates(dict_list):
    """
        See the description of create_list() function above
    """
    try:
        duplicates = []
        for d in dict_list:
            for key, value in d.items():
                duplicates.append(key)
        # get all duplicate keys from dicts in list
        duplicates = ([item for item, count in Counter(duplicates).items() if count > 1])
        return duplicates
    except TypeError:
        exception('get_duplicates. Incorrect input')


# rename and concat all dicts
def dict_concat(dict_list):
    """
        See the description of create_list() function above
    """
    try:
        result = {}
        for i in dict_list:
            for k, v in i.items():
                if k in get_duplicates(dict_list):
                    result[k + '_' + str(dict_list.index(i) + 1)] = v
                else:
                    result[k] = v
        print('Concatenated dicts with renamed keys:\n ', result)
        return result
    except TypeError:
        exception('dict_concat. Incorrect input')


# get concatenated dict with sorted values
def get_sorted(dict_list):
    """
        See the description of create_list() function above
    """
    try:
        # sorting the dict by values desc
        result = OrderedDict(sorted(dict_concat(dict_list).items(), key=lambda x: x[1], reverse=True))
        # get first keys with max value
        finalDict = {}
        for i, v in result.items():
            if i[0] not in (x[0] for x in finalDict.keys()):
                finalDict[i] = v
        return finalDict
    except TypeError:
        exception("Incorrect list input")

if __name__ == "__main__":# pay attention to this construction
    list_dicts = create_list(dictCnt=4, kCnt=randint(2, 5), vStart=5, vEnd=10)
    print('Final dict with max values:\n ', get_sorted(dict_list=list_dicts))
