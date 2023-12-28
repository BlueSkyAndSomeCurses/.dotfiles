from math import *


def main():
    f_x = lambda x: eval(input())

    a = float(input())
    b = float(input())
    x_k = (b - a) / 1000

    area = 0
    for i in range(1000):
        area += (x_k) * f_x(a + x_k * i)

    print(f"{area:.4f}")


if __name__ == "__main__":
    main()
