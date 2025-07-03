stack = []
s_rev = ''
s = str(input("Enter any String: "))
i = 0
while i < len(s):
    stack.append(s[i])
    i += 1

while len(stack) != 0:
    s_rev = s_rev + stack.pop()

print("String: ",s_rev)