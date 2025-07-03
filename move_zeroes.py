nums = [0,1,0,3,12]
if len(nums) > 2:
    for i in range(0,len(nums)-2):
        if nums[i] == 0:
            if nums[i+1] != 0:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                nums[i], nums[i+2] = nums[i+2], nums[i]
                nums[i+1], nums[i+3] = nums[i+3], nums[i+1]
elif len(nums) == 2:
    for i in range(0,len(nums)):
        if nums[i] == 0:
            nums[i],nums[i+1] = nums[i+1],nums[i]
print(nums)