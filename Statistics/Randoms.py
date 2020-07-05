import random


def randomRangeSeed(a, b, seed):
    result = random(a, b, seed)
    return result


def randomRange(a, b):
    result = random(a, b)
    return result


def randomList(a, b, seed, listLength):
    result = random(a, b, seed, listLength)
    return result


def randomListItem(list1):
    result = list[random(0, len(list))]
    return result


def randomListItemMultiple(self, list1, selectAmount):
    result = random.choices(list1, k=selectAmount)
    return result


def randomListItemSeedMultiple(self, list1, seed, selectAmount):
    random.seed(seed)
    result = random.choices(list1, k=selectAmount)
    return result
