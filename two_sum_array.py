arr = [2,7,11,15]
print(f"Array looks like: {arr}")
target = int(input("Enter the Target: "))
l = 0
r = (len(arr) -1)
while l < r:
    x = arr[l]+arr[r]
    if x == target:
        x1 = l+1
        x2 = r+1
        print(f"Answer: [{x1},{x2}]")
        break
    elif x > target:
        r -= 1
    else:
        l += 1