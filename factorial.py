n = int(input('Enter any Number: '))
fact = 1
for i in range(n,0,-1):
    fact = fact * i
print(f'The Factorial of {n} is {fact}.')