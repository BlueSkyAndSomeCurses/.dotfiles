def f_x(x):
    return x

def main():

    a = float(input())
    b = float(input())
    x_k = (b-a)/1000
    
    area = 0
    for i in range(1000):
        area += (a + x_k * i) * f_x()



if __name__ == "__main__":
    main()
