from math import exp, expm1, log
def f(x):
    return 8**x - 25

def df(x):
    return (8**x) * log(8)

def newtonMethod(p0, TOL, maxIterations):
    for i in range(0, maxIterations):
        p = p0 - (f(p0)/df(p0))
        if(abs(p - p0) < TOL):
            print "Iteration: ", i
            return p
        p0 = p
    return "Error: Max iterations exided"

print newtonMethod(1, 0.0000001, 100)
