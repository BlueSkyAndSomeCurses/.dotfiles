"""
Calculates area under a function
"""
import numpy as np
import matplotlib.pyplot as plt
from math import *


def main():
    expr = input("Input function to calculate its area: ")
    f_x = lambda x: eval(expr)

    a = float(input("Enter lower bound: "))
    b = float(input("Enter upper bound: "))
    x_k = 1 / 1000

    area = 0
    for i in range(int(1000 * (b - a))):
        area += (x_k) * f_x(a + x_k * i)

    print(f"{area:.4f}")

    x_values = np.linspace(a, b, 1000)
    y_values = f_x(x_values)

    plt.plot(x_values, y_values, label="y = x^2 + 3x + 2")

    # Add labels and title
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Graph of the Function")

    # Display the legend
    plt.legend()

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
