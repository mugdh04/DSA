def bit_finder(x,n):
    mask = 1
    x = x >> (n - 1)
    bit_val = x & mask
    print(f"The {n}th Bit is {bit_val}")

x = int(input("Enter any Number: "))
n = int(input("Enter the position: "))
bit_finder(x,n)