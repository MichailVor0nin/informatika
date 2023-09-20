from math import *

x = float(input())
y = float(input())
z = float(input())

a = sin(sqrt(abs(x-1))) * cos((abs(y))**(1/3))/(1+((x)**1/3)+sqrt(y))
b = log1p(abs(x-1)) - (sqrt(abs(y))) * (sqrt(x)) + ((abs(z))**0.25)

print(a,b)