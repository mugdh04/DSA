n = int(input('Enter any number to be reversed: '))
x = n
y = 0
m = 0
while x > 0:
    y = x % 10
    m = (m * 10) + y
    x = x // 10
print(f'Reverse of {n} is {m}.')