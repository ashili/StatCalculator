import Calculator
import math
import random


def isEven(num):
    if (num % 2) == 0:
        return True


class StatCalc(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def median(self, nums):
        nums.sort()
        if isEven(len(nums) + 1):
            r = nums[len(nums) / 2]
        else:
            r = (nums[len(nums) / 2] + nums[(len(nums) / 2) - 1]) / 2.00
        return float(r)

    def mean(self, nums):
        return sum(nums) / float(len(nums))

    def mode(self, nums):
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

    def variance(self, nums):
        total = 0
        m = self.mean(nums)
        for i in nums:
            total += ((i - m) * (i - m))
        c = total / len(nums)
        return c

    def stdDev(self, nums):
        return math.sqrt(self.variance(nums))

    def zScore(self, num, nums):
        z = (float(num) - self.mean(nums)) / self.stdDev(nums)
        return z

    def simpleRandomSample(self, num, nums):
        return random.sample(nums, num)

    def confidenceInterval(self, nums):
        length = len(nums)
        numsMean = self.mean(nums)
        stanDev = self.stdDev(nums)
        lowerBound = numsMean + 1.96 * (stanDev / math.sqrt(length))
        upperBound = numsMean - 1.96 * (stanDev / math.sqrt(length))
        returnResult = [lowerBound, upperBound]
        return returnResult

    def marginOfError(self, nums):
        length = len(nums)
        stanDev = self.stdDev(nums)
        stanError = stanDev/math.sqrt(length)
        margin = stanError * 1.96
        return margin

    def cochranSampleSize(self, marginOfError, estimatedProportion):
        return ((1.96 ^ 2) * estimatedProportion * (1 - estimatedProportion)) / (marginOfError ^ 2)

    def sampleSize(self, confidenceInterval, width):
        marginOfError = width / 2
        pHat = .5
        qHat = 1 - pHat
        return (pHat * qHat) * ((1.96 / marginOfError) ^ 2)