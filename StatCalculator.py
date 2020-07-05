import Calculator
import math


def mean(nums):
    return sum(nums) / float(len(nums))


def isEven(num):
    if (num % 2) == 0:
        return True


def median(nums):
    nums.sort()
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
    # TODO: fix the highest number in d (f)
    f = max(d, key=d.get)
    return f


def variance(nums):
    total = 0
    m = mean(nums)
    for i in nums:
        total += ((i - m) * (i - m))
    c = total / len(nums)
    return c


def stdDev(nums):
    return math.sqrt(variance(nums))


def zScore(num, nums):
    z = (float(num) - mean(nums))/stdDev(nums)
    return z


class StatCalc(Calculator):
    def __init__(self):
        super()
