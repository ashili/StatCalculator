import Calculator
import math


def isEven(num):
    if (num % 2) == 0:
        return True


class StatCalc(Calculator):
    def __init__(self):
        super()

    def median(self, nums):
        nums.sort()
        if isEven(len(nums) + 1):
            r = nums[len(nums) / 2]
        else:
            r = (nums[len(nums) / 2] + nums[(len(nums) / 2) - 1]) / 2.00
        return float(r)

    def mean(self,nums):
        return sum(nums) / float(len(nums))

    def mode(self,nums):
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
