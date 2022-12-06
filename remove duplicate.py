nums = [1,2,3,4,3,4,5,5,5,5,5,4,4,4,]
i = 1
while i < len(nums):
    nums.sort()
    if nums[i-1] == nums[i]:
        nums.pop(i-1)
    else:
        i += 1
    
print(nums)
