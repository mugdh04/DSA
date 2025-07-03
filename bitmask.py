def odd_even_and(x):
    x = x & 1
    if x == 1:
        print("Odd!!!")
    else:
        print("Even!!!")

def odd_even_xor(x):
    y = x
    x = x ^ 1
    if x == y + 1:
        print("Even!!!")
    else:
        print("Odd!!!")

def odd_even_bit_shift(x):
    if (x >> 1) << 1 == x:
        print("Even!!!")
    else:
        print("Odd!!!")

n = int(input("Enter the number: "))
odd_even_and(n)
odd_even_xor(n)
odd_even_bit_shift(n)