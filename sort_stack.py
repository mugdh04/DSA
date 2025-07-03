stack = [22, 12, 10, 47, 23]
array = []

print(f"Unsorted Stack looks like: {stack}")

while len(stack) != 0:
    array.append(stack.pop())

array.sort()

for i in range(len(array)):
    stack.append(array[i])

print(f"Sorted Stack looks like: {stack}")