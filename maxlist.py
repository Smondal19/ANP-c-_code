# Write a Python program to find the maximum product of two integers in a list.

def max_product(nums):
    if len(nums) < 2:
        return None
    nums.sort()
    return max(nums[0] * nums[1], nums[-1] * nums[-2])
nums = [6,2,10,3,9]
result = max_product(nums)
print("The maximum product of two integers in the list is:",result)
