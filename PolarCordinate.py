# import math
# import cmath

# complex_number = complex(input())
# x = complex_number.real
# y = complex_number.imag

# z = math.sqrt(x**2 + y**2)
# print(z)
# a = cmath.phase(complex(x, y))
# print(a)

import cmath 
a = complex(input()) 
b =cmath.polar(a) 
for i in b: print(i)

