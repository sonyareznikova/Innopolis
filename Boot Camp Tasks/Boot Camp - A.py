import sys
import collections 
import random
sys.setrecursionlimit(30000)

def main():
    a,b,c = [float(it) for it in input().split()]
    if a == 0:
        if b == 0:
            if c == 0:
                ## There are inf roots
                sys.stdout.write('There are a lot of roots \n')
            else:
                ## There are no roots
                sys.stdout.write('There are no any roots \n')
        else:
            ## There is one root
            x = ((c/b) * (-1.0))
            ## 0 2 0 -> -0.0 ???
            if x == -0.0:
                x = 0.0
            sys.stdout.write('One Real Root:\nx1: %.5f \n'% x)
    elif a != 0:
        d = b*b - 4*a*c
        if d < 0:
            ## There are complex roots
            sys.stdout.write('There are no real roots \n')
            sys.stdout.write('Two complex roots: \n')
            real = -b/2/a
            img = ((-d) ** 0.5)/2/a
            sys.stdout.write("x1: %.5f + %.5fi\n" % (real,img))
            sys.stdout.write("x2: %.5f - %.5fi\n" % (real,img))
        elif d == 0:
            ## There is one root
            x = -b/2/a
            sys.stdout.write('One Real Root:\n \nx1: %.5f \n'% x)
        elif d > 0:
            ## There are two roots
            x1 = (-b + d**0.5)/2/a
            x2 = (-b - d**0.5)/2/a
            if x1 > x2:
                x1,x2 = x2,x1
            sys.stdout.write('Two Real Roots:\n \nx1: %.5f \nx2: %.5f \n'% (x1,x2))
if __name__ == "__main__":
    ##sys.stdin = open('f.in','r')
    ##sys.stdout = open('f.out','w')
    main()
    ##sys.stdin.close()
    ##sys.stdout.close()