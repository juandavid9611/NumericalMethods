from math import *

possibleValuesOfH = np.linspace(-0.8,1.000000000,1000)

def f(x):
    return log(x)

def aproxDerivative(x, h):
    if(h == 0.0): 
        return float("inf")
    parent = (-3.0)*f(x) + (4.0)*f(x + h) - f(x + h) - f(x + 2.0*h)
    firstFraction = 1.0/(2.0*h)
    return firstFraction * parent

def realDerivative(x):
    return 1.0/x

valueToAproximate = 1.8
realValue = realDerivative(valueToAproximate)

for h in possibleValuesOfH:
    aprox = aproxDerivative(valueToAproximate, h)
    real = realDerivative(valueToAproximate)
    errorPorcentual = abs(real - aprox) / real
    error = abs(real - aprox)
    if(errorPorcentual < 0.01):
        print ("H Value:", h)
        print ("Aprox Value: ", aprox)
        print ("Real Value: ", real)
        print ("Porcentual Error: ", errorPorcentual)
        print ("Absolute Error: ", error)
        print ("")

'''
Conclucion:
    
    El h es -0.618018018018 (a la izquierda) ya que con este se 
    obtuvo el menor error que fue de 0.00339362807756 que solo difiere
    del valor real por 0.00188534893198 lo cual es muy poco la variación.
    Se tomaron valores a la derecha y a la izquierda para encontrar la 
    mejor aproximación.
'''
