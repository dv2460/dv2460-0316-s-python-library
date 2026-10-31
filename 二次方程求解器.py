import math
import cmath

cont = True
while cont:
    print("\n将方程化成标准形式 ax^2 + bx + c = 0 后输入")
    a = float(input("输入二次项系数 a:"))

    b = float(input("输入一次项系数 b:"))

    c = float(input("输入常数项 c:"))

    if a == 0:
        if b == 0 and c != 0:
            print("方程在任何已知数域内无解，请检查输入条件！")
        elif b == 0:
            print("方程对任意的x∈C均成立")
        else:
            x = -c / b
            print(f"方程为一次方程，解为 {x}")
            # 处理三种特殊情况，令进入下一步的方程一定是二次方程

    else:
        # 计算判别式
        delta = b * b - 4 * a * c

        if delta > 0:
            x1 = (math.sqrt(delta) - b) / (2 * a)
            x2 = (-1 * math.sqrt(delta) - b) / (2 * a)
            print(f"方程有两个不等实根，分别为 {max(x1, x2)} 和 {min(x1, x2)}")
            # 两个不等实根情况

        elif delta == 0:
            x = (math.sqrt(delta) - b) / (2 * a)
            print(f"方程有一个实根，为 {x}")
            # 一个实根的情况

        else:
            print("方程在实数域内无解，是否在复数域内继续求解？(回答yes/no)")
            go = input() == "yes"

            if go:
                x1 = (cmath.sqrt(delta) - b) / (2 * a)
                x2 = (-1 * cmath.sqrt(delta) - b) / (2 * a)
                print(f"方程有两个不等复根，分别为 {x1}和{x2}")
                # 用户选择继续，则换用cmath计算两根
            else:
                print("方程无解，求解结束")
                # 用户不继续求解，则结束本次计算
    cont = input("本次求解已结束，是否继续？(回答yes/no)") == "yes"
#pulltest
