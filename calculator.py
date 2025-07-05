from random import choice


def calculator():
    print("欢迎使用计算器！")
    print("您可以使用+ - * / % ** 六种运算符来作用于两个数，从而得到结果")

    while 1:
        try:
            num1 = float(input("请输入第一个数字："))
            operator = input("请输入运算符：")
            num2 = float(input("请输入第二个数字："))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("除数不能为0")
                    continue
                result = num1 / num2
            elif operator == "%":
                result = num1 % num2
            elif operator == "**":
                result = num1 ** num2





        except ValueError:
            print("请输入正确的数字")
            continue

        else:
            print(f"{num1} {operator} {num2} = {result}")

        choice = input("是否继续使用计算器？（y/n）").lower()
        if choice != "y":
            print("计算器退出")
            break

if __name__ == "__main__":
    calculator()