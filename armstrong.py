x=int(input('Enter any number: '))
y=x
sum=0
while y > 0:
    z=y % 10
    sum=sum+(z*z*z)
    y=y//10
if (sum == x):
    print('It is an Armstrong Number.')
else:
    print('Not an Armstrong Number.')