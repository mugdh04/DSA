
arr = []
n = int(input("Enter the number of elements in array: "))
for i in range(n):
    a = int(input())
    arr.append(a)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j+1] < arr[j]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)