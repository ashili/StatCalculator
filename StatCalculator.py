import Calculator


def mean(nums):
    return sum(nums) / nums


def isEven(num):
    if (num % 2) == 0:
        return True


def median(nums):
    if isEven(len(nums) + 1):
        r = nums[len(nums) / 2]
    else:
        r = (nums[len(nums) / 2] + nums[(len(nums) / 2) - 1]) / 2.00
    return float(r)


def mode(nums):
    if len(nums) == 0:
        return 0

    d = dict()
    for item in nums:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1

    f = max(d, key=d.get)
    return f


class StatCalc(Calculator):
    def __init__(self):
        super()
