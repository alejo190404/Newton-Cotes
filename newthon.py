from math import e, sin, pi
import random

def evaluar(expr, x):
    return eval(expr)

def cote_cerrada_1(a, b, f):
    h = b - a
    return (h/2) * (evaluar(f, a) + evaluar(f, b))

def cote_cerrada_2(a, b, f):
    h = (b - a)/2
    return (h/3) * (evaluar(f, a) + 4*evaluar(f, a + h) + evaluar(f, b))

def cote_cerrada_3(a, b, f):
    h = (b - a)/3
    return ((3*h)/8) * (evaluar(f, a) + 3*evaluar(f, a + h) + 3*evaluar(f, a + 2*h) + evaluar(f, b))

def cote_cerrada_4(a, b, f):
    h = (b - a)/4
    return ((2*h)/45) * (7*evaluar(f, a) + 32*evaluar(f, a + h) + 12*evaluar(f, a + 2*h) + 32*evaluar(f, a + 3*h) + 7*evaluar(f, a+4*h))

def cote_abierta_0(a, b, f):
    h = (b-a)/2
    return 2*h * evaluar(f, a + h)

def cote_abierta_1(a, b, f):
    h = (b - a)/3
    return ((3*h)/2) * (evaluar(f, a + h) + evaluar(f, a + 2*h))

def cote_abierta_2(a, b, f):
    h = (b - a)/4
    return ((4*h)/3) * (2*evaluar(f, a + h) - evaluar(f, a + 2*h) + 2*evaluar(f, a + 3*h))

def cote_abierta_3(a, b, f):
    h = (b - a)/5
    return ((5*h)/24) * (11*evaluar(f, a + h) + evaluar(f, a + 2*h) + evaluar(f, a + 3*h) + 11*evaluar(f, a + 4*h))

def compuesta_simpson(a, b, f, n):
    h = (b - a)/n
    sumaImpares = 0
    for i in range(1, (int)(n/2) + 1):
        sumaImpares += evaluar(f, a + ((2*i)-1)*h)

    sumaPares = 0
    for i in range(1, (int)(n/2)):
        sumaPares += evaluar(f, a + 2*i*h)

    return (h/3) * (evaluar(f, a) + evaluar(f, b) + 4*sumaImpares + 2*sumaPares)

def compuesta_trapezoidal(a, b, f, n):
    h = (b - a)/n
    suma = 0
    for i in range(1, n):
        suma += evaluar(f, a + i*h)
    return (h/2) * (evaluar(f, a) + 2*suma + evaluar(f, b))

def compuesta_punto_medio(a, b, f, n):
    h = (b - a)/n
    suma = 0
    for i in range(0, (int)(n/2 + 1)):
        suma += evaluar(f, a + 2*i*h)
    return 2*h*suma

f = "(e**x)*sin(x)"
print("Cote cerrada 1 (Trapezoidal): ", cote_cerrada_1(0, pi, f))
print("Cote cerrada 2 (Simpson): ", cote_cerrada_2(0, pi, f))
print("Cote cerrada 3 (Simpson 3/8): ", cote_cerrada_3(0, pi, f))
print("Cote cerrada 4 (Boole): ", cote_cerrada_4(0, pi, f))
print("Cote abierta 0 (Punto medio): ", cote_abierta_0(0, pi, f))
print("Cote abierta 1: ", cote_abierta_1(0, pi, f))
print("Cote abierta 2: ", cote_abierta_2(0, pi, f))
print("Cote abierta 3: ", cote_abierta_3(0, pi, f))
print("Compuesta simpson: ", compuesta_simpson(0, pi, f, 10))
print("Compuesta trapezoidal: ", compuesta_trapezoidal(0, pi, f, 10))
print("Compuesta punto medio: ", compuesta_punto_medio(0, pi, f, 10))