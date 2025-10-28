L, R = map(int, input().split())

count = 0

for i in range(L, R + 1):
    num = i
    rev = 0

    
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    
    if rev == i:
        count += 1


print(count)
