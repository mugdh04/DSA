nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]

result = []
map = []

for i in range(0, len(nums2)-1):
    for j in range(i+1, len(nums2)):
        if nums2[j] > nums2[i]:
            map.append(nums2[j])
            break
        elif j == len(nums2)-1:
            map.append(-1)
        else:
            continue

map.append(-1)

for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            result.append(map[j])
            

print(result)