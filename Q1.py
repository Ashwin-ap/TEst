#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

def moveZeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    for i in range(left, len(nums)):
        nums[i] = 0


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)

