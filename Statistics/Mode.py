def mode( nums):
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
