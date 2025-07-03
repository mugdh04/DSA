import random

a = int(input("Enter the no. of Upper Case Characters: "))
b = int(input("Enter the no. of Lower Case Characters: "))
c = int(input("Enter the no. of Numeric Characters: "))
d = int(input("Enter the no. of Special Characters: "))

Upcase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Lowcase = list("abcdefghijklmnopqrstuvwxyz")
Numeric = list("1234567890")
Spchrt = list("!@#$%^&*()_+-=|<>?")

Result = list()

for i in range(0,a):
    p = random.choice(Upcase)
    Result.append(p)

for i in range(0,b):
    p = random.choice(Lowcase)
    Result.append(p)

for i in range(0,c):
    p = random.choice(Numeric)
    Result.append(p)

for i in range(0,d):
    p = random.choice(Spchrt)
    Result.append(p)

random.shuffle(Result)
final_result = ""

for i in range(0,len(Result)):
    final_result = final_result+Result[i]

print(" ")
print(f"Final Password: {final_result}")