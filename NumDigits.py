Number=int(input("Enter the integer:"))
Count = 0
while(Number > 0):
    Number = Number // 10
    Count = Count + 1
print(Count)

