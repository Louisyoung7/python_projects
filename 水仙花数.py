# 找出 100 到 999 范围内的所有水仙花数。
for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if low**3 + mid**3 + high**3 == num:
        print(num)