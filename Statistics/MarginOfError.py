import math
from Statistics.StdDev import stdDev


def marginOfError(nums):
    length = len(nums)
    stanDev = stdDev(nums)
    stanError = stanDev / math.sqrt(length)
    margin = stanError * 1.96
    return margin
