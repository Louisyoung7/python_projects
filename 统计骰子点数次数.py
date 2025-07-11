# 将一颗色子掷6000次，统计每种点数出现的次数
import random

# 定义一个列表，每一个元素对应骰子的一个面
counter = [0] * 6   # *运算符能将列表中元素重复n次

# 用随机数模拟投掷
for _ in range(0,6000):
    face_val = random.randint(1,6)
    counter[face_val - 1] += 1  # python中没有自增自减运算符
# 将列表中元素打印出来
for face_val in range(1,7):
    print(f"{face_val}点出现{counter[face_val - 1]}次")
