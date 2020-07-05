from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.SampleMean import sample_mean





class StatCalc(Calculator):
    data = []

    def __init__(self):
        super().__init__()



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
