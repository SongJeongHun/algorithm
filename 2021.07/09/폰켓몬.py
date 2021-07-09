def solution(nums):
    mid = int(len(nums) / 2)
    nums = len(set(nums))
    if mid > nums:
        return nums
    else:
        return mid
