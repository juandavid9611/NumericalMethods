from math import exp, expm1, log


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def f1(x):
    return exp(x * -1)

def nthDrv1(n, x):
    if(n % 2 == 0):
        return exp(x * -1)
    else:
        return exp(x * -1) * -1

def taylorPoly1(x, a):
    totalSum = f1(a)
    for i in range(1,9):
        derivative = nthDrv1(i,a)
        fact = (i)
        term = (x - a)**i
        totalSum += (derivative *term) / fact
    return totalSum

print taylorPoly1(5.0, 4.5)


def f2(x):
    return exp(1 - x)

def nthDrv2(n, x):
    if(n % 2 == 0):
        return exp((1 - x))
    else:
        return exp((1 - x)) * -1

def taylorPoly2(x, a):
    totalSum = f2(a)
    for i in range(1,9):
        derivative = nthDrv2(i,a)
        fact = (i)
        term = (x - a)**i
        totalSum += (derivative *term) / fact
    return totalSum

print taylorPoly2(6.0, 4.5)
