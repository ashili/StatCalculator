from Calculator.IsEven import isEven


def median(nums):
    nums.sort()
    if isEven(len(nums) + 1):
        r = nums[len(nums) / 2]
    else:
        r = (nums[len(nums) / 2] + nums[(len(nums) / 2) - 1]) / 2.00
    return float(r)
