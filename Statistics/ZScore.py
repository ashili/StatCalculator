from Statistics.Mean import mean
from Calculator.Substraction import subtraction
from Calculator.Division import division


def zScore(self, num, nums):
    z = division((subtraction(float(num), mean(nums))), self.stdDev(nums))
    return z
