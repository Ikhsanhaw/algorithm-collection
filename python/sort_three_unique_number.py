def sortNums(nums):
    arr_ = [0] * 3
    for x in nums:
        arr_[x - 1] += 1

    for i in range(1, len(arr_)):
        arr_[i] += arr_[i - 1]

    arr2_ = [0] * len(nums)
    for x in reversed(nums):
        arr2_[arr_[x - 1] - 1] = x
        arr_[x - 1] -= 1
    return arr2_