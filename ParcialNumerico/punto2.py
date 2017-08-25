import math

def f(x):
    return math.cos(4*x - 1) + 0.5

def itertiveMethon(aprox1, aprox2, low, high, tol, maxIterations):
    assert aprox1 >= low and aprox1 <= high
    assert aprox2 >= low and aprox2 <= high
    array = []
    array.append(aprox1)
    array.append(aprox2)
    for i in range(2, maxIterations + 2):
        frac = (array[i - 1] - array[i - 2])/(f(array[i - 1] - f(array[i - 2])))
        calc = array[i - 1] - (f(array[i - 1]) * frac)
        array.append(round(calc,4))
        if(abs(round(calc,4) - round(array[i-1],4) ) < tol):
            return round(calc,4)
    return "Max Iteraciones Exedidas"

root = itertiveMethon(0.77355, 0.77357, 0, 1, 0.00001, 100)

print "Root: ", root
print "Valor De Root: ", f(root)
