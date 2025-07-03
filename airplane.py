dir = list(input('Enter the Directions: '))

n = s = e = w = temp = 0

for i in range (0,len(dir)):
    x = dir[i]
    if (x == 'N' or x == 'n'):
        n = n+1
    elif (x == 'E' or x == 'e'):
        e = e+1
    elif (x == 'W' or x == 'w'):
        w = w+1
    elif (x == 'S' or x == 's'):
        s = s+1
    else:
        temp = temp+1

if temp != 0:
    print(f'Entered string contains {temp} invalid Directions!!')
    # print('Showing Results on the basis of given incorrect data:')

elif n == s and e == w:
    print('The Plane has Landed.')
    
else:
    print('The Plane is still flying!!')