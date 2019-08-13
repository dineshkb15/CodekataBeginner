p=int(input("Enter the integer:"))
r = 0
while p:
    r, p = r + p % 10, p // 10
print(r)
