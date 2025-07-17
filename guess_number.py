import random

# 定义一个猜数字的函数
def guess_number():
    # 利用随机数获取数字
    number = random.randint(1,100)
    # 定义一个变量承载猜测次数
    attempts = 0

    print("猜一个1到100以内的数字：")

    while(True):
        try:
            guess_number = int(input("请输入你预测的数字："))
            attempts += 1

            if guess_number > number:
                print("数字大了")
            elif guess_number < number:
                print("数字小了")
            else:
                print(f"恭喜猜对了，数字是{number}，一共猜了{attempts}次")
                break
        except ValueError:
            print("请输入有效数字")


if __name__ == "__main__":
    guess_number()

