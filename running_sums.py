nums = []
runningsum =[]
len = int(input("Enter the size of Array: "))
for i in range (0,len):
    a = int(input(f"Enter the Element {i+1} in the array: "))
    nums.append(a)
sum = 0
for i in range (0,len):
    sum += nums[i]
    runningsum.append(sum)
print(runningsum)