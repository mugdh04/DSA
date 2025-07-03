nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]

map = {}
stack = []
result = []

for num in nums2:
    while stack and stack[-1] < num:
        map[stack.pop()] = num
    stack.append(num)

while stack:
    map[stack.pop()] = -1

for num in nums1:
    result.append(map[num])

print(result)