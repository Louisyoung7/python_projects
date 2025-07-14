'''
双色球是由中国福利彩票发行管理中心发售的乐透型彩票，每注投注号码由6个红色球和1个蓝色球组成。
红色球号码从1到33中选择，蓝色球号码从1到16中选择。
每注需要选择6个红色球号码和1个蓝色球号码
'''

import random

# 红球的所有情况
red_balls = list(range(1,34))

# 用于存放选中的红球
selected_balls = []

# 添加随机选中的6个球到selected_balls列表
for _ in range(6):
    # 从33个红球中随机选，把选中红球的索引赋值给index
    index = random.randrange(len(red_balls))
    # 利用pop方法，把index对应的红球移动到selected_balls列表中
    selected_balls.append(red_balls.pop(index))

# 对选中的红色球排序
selected_balls.sort()

# 输出选中的红色球
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m',end = ' ')

# 随机选择一个蓝球
blue_ball = random.randrange(1,17)
print(f'\033[034m{blue_ball}\033[0m')

