from Statistics.Mean import mean
from Statistics.StdDev import stdDev
import math


def confidenceInterval(nums):
    length = len(nums)
    numsMean = mean(nums)
    stanDev = stdDev(nums)
    lowerBound = numsMean + 1.96 * (stanDev / math.sqrt(length))
    upperBound = numsMean - 1.96 * (stanDev / math.sqrt(length))
    returnResult = [lowerBound, upperBound]
    return returnResult
