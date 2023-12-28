from math import *


def main():
    expr = input("Input function to calculate its area: ")
    f_x = lambda x: eval(expr)

    print(f_x(5))

    a = float(input("Enter lower bound: "))
    b = float(input("Enter upper bound: "))
    x_k = (b - a) / 1000

    area = 0
    for i in range(1000):
        area += (x_k) * f_x(a + x_k * i)

    print(f"{area:.4f}")


if __name__ == "__main__":
    main()
