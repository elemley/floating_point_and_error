
from math import *

def f_any(x,n):
    index = n%4

    if index == 0:
        return cos(x)
    elif index == 1:
        return -sin(x)
    elif index == 2:
        return -cos(x)
    elif index == 3:
        return sin(x)


#Below is a function definition
def main():
    a = 1.0
    b = 2.0
    c = -2.5
    dx = 0.1

    #print(0%4, 1%4, 2%4, 3%4, 4%4, 5%4, 6%4)
    N =  4
    summ = 0.0
    x = pi/24
    h = pi/24
    for i in range(0,N):
        term = f_any(x,i)/factorial(i)*h**i
        print(term)
        summ +=term

    print(summ)









if __name__ == '__main__':
    main()











