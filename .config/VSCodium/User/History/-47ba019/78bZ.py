def f_x(x):
    return x**2


def main():
    a = float(input())
    b = float(input())
    x_k = (b - a) / 1000

    area = 0
    for i in range(1000):
        area += (x_k) * f_x(a + x_k * i)

    print(area)


if __name__ == "__main__":
    main()
