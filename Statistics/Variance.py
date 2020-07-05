from Statistics.Mean import mean


def variance(self, nums):
    total = 0
    m = mean(nums)
    for i in nums:
        total += ((i - m) * (i - m))
    c = total / len(nums)
    return c
