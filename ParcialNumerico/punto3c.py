from math import exp, expm1, log
def f(x):
    return x**4 - x - 1

def f1(x):
    return x**4

def f2(x):
    return x

def df(x):
    return 4*(x**3) - 1

def newtonMethod(p0, TOL, maxIterations):
    for i in range(0, maxIterations):
        p = p0 - (f(p0)/df(p0))

        if(abs(p - p0) < TOL):
            print "Iteration: ", i
            return p
        p0 = p
    return "Error: Max iterations exided"

solution = newtonMethod(1.0, 0.0000001, 100)

print "Solution: ", solution
print "Distance in Y: ", abs(f1(solution) - f2(solution))
