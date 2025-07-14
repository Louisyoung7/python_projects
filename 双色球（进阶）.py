'''
双色球是由中国福利彩票发行管理中心发售的乐透型彩票，每注投注号码由6个红色球和1个蓝色球组成。
红色球号码从1到33中选择，蓝色球号码从1到16中选择。
每注需要选择6个红色球号码和1个蓝色球号码
'''

import random

n = int(input("生成几注号码："))

# 红球和蓝球的所有情况
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

for _ in range(n):

    # 利用sample随机无放回抽样
    selected_balls = random.sample(red_balls,6)

    # 对选中的红色球排序
    selected_balls.sort()

    # 输出选中的红色球
    for ball in selected_balls:
        print(f'\033[031m{ball:0>2d}\033[0m',end = ' ')

    # 随机选择一个蓝球
    blue_ball = random.choice(blue_balls)

    # 输出选中的蓝色球
    print(f'\033[034m{blue_ball}\033[0m')

