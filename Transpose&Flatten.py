# Transpose (Generate the transposition of the following array)
import numpy
my_arr = numpy.array([[1,2,3],[4,5,6]])
print(my_arr.transpose())

# Flatten (Create a copy of the following array flattened to one dimension)
import numpy
my_arr = numpy.array([[1,2,3],[4,5,6]])
print(my_arr.flatten())

# Exercise (Print the transposed and flattened of the input array)
import numpy

def InputArray(Row, Colum):
    arrs = []
    for i in range(Row):
        arr = list(map(int, input().split()))
        arrs.append(arr)
    return numpy.array(arrs)

def Transpose(arr):
    return arr.transpose()

def Flatten(arr):
    return arr.flatten()

N, M = map(int, input().strip().split())
My_arr = InputArray(N, M)
print(Transpose(My_arr))
print(Flatten(My_arr))

