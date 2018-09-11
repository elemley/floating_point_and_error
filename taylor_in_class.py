from math import *


#return the correct thing
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
    else:
        return "AHHHH"


def main():
    print(cos(pi/12))

    N = 12
    summ = 0.0
    x = 0
    h = pi/12
    #put a loop here..
    for n in range(0,N):
        term = f_any(x,n)*h**n / factorial(n)
        print(term)
        summ+=term
    print(summ)



if __name__ == '__main__':
    main()











