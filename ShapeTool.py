import numpy
# Using shape to get array dimensions
my_1D_array = numpy.array([1, 2, 3, 4, 5])
print(my_1D_array.shape)     #(5,) -> 1 row and 5 columns

my_2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print(my_2D_array.shape)     #(3, 2) -> 3 rows and 2 columns

# Using shape to change array dimensions
change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print(change_array)

# Reshape (creates a new array and does not modify the original array itself)
my_array = numpy.array([1,2,3,4,5,6])
print(numpy.reshape(my_array,(3,2)))

# Exercise Print the 3X3 NumPy array.

def Func(arr):
    arr2 = numpy.array(arr, int)
    return arr2.reshape((3,3))

arr = input().strip().split()
result = Func(arr)
print(result)


