num = int(input("请输入一个正整数："))
# 194327
reversed_num = 0
while num != 0:
    reversed_num = num % 10 + reversed_num * 10
    num //= 10
print(reversed_num)

