#输出100以内的素数
for num in range(2,100):
    is_res = True
    for i in range(2,num):
        if num % i == 0:
            is_res = False
            break
    if is_res:
        print(num)