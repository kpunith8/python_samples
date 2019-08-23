from numpy import pi
import numpy as np

array1 = np.array([2, 3, 4])

print(array1, array1.shape, array1.dtype)

# The type of the array can also be explicitly specified at creation time

complexTypeArray = np.array([[1, 2], [3, 4]], dtype=complex)
print(complexTypeArray)

# The function `zeros` creates an array full of zeros,
# the function `ones` creates an array full of ones,
# and the function `empty` creates an array whose initial content is random
# and depends on the state of the memory. By default, the `dtype` of the created array is `float64`.
arrayWithZeros = np.zeros((3, 4))
print('Array created with zeros funtion', arrayWithZeros)

arrayWithOnes = np.ones((2, 3, 4), dtype=np.int16)
print('Array created with ones function', arrayWithOnes)

emptyArray = np.empty((2, 3))
print('Array created with empty function', emptyArray)

# To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists.

# Array from 10 to 30 with a range 5
arrayRange = np.arange(10, 30, 5)
print('Array with range', arrayRange)
# it accepts float arguments
arrayRange1 = np.arange(0, 2, 0.3)
print('Array with range floating point numbers', arrayRange1)

# When `arange` is used with floating point arguments, it is generally not possible
# to predict the number of elements obtained, due to the `finite floating point precision`.
# For this reason, it is usually better to use the function `linspace` that receives as an argument the `number of elements` that we want,
# instead of the step


# 9 numbers from 0 to 2
arrayRangeWithLineSpace = np.linspace(0, 2, 9)
print('Arrange with line space for floating numbers', arrayRangeWithLineSpace)

# useful to evaluate function at lots of points
x = np.linspace(0, 2*pi, 5)
f = np.sin(x)

# print(x)

# If an array is too large to be printed, NumPy automatically
# skips the central part of the array and only prints the corners:
# print(np.arange(10000).reshape(100, 100))

# To `disable` this behaviour and force NumPy to print the entire array, you can change the printing options using set_printoptions.
# np.set_printoptions(threshold=10)

# Basic Operations

# Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result
a1 = np.array([20, 30, 40, 50])
b1 = np.arange(4)
arraySub = a1-b1

print('Actual array a1', a1)
print('Actual array b1', b1)

print('Subtract an array', arraySub)

arrayMultiplied = b1**2
print('Multiplied array', arrayMultiplied)

arraySinOperation = 10*np.sin(a1)
print(arraySinOperation)

arrayWithBoolean = a1 < 35
print(arrayWithBoolean)

# Unlike in many matrix languages, the product operator `*` operates `elementwise` in NumPy arrays.
# The matrix product can be performed using the `@` operator (in python >=3.5) or the `dot` function or method
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

print(A)
print(B)
# elementwise product
print('* operator performs elementwise product', A*B)
# matrix product
print('Matrix multiplication using @', A@B)
# another matrix product
print('Matrix multiplication using dot function', A.dot(B))

# Some operations, such as `+=` and `*=`, act in place to `modify an existing array`
# rather than create a new one.
a2 = np.ones((2, 3), dtype=int)
b2 = np.random.random((2, 3))
a2 *= 3
print('Mutated array using *=', a2)

b2 += a2
print('Mutated array using +=', b2)

# b is not automatically converted to integer type
# a += b

# Following error is throws
# Traceback (most recent call last):
#   ...
# TypeError: Cannot cast ufunc add output from
# dtype('float64') to dtype('int64') with casting rule 'same_kind'

# When operating with arrays of different types,
# the type of the resulting array corresponds to the more general or precise one
# (a behavior known as upcasting).

# Many unary operations, such as computing the
#  sum of all the elements in the array, are implemented as methods of the ndarray class.
randomArray = np.random.random((2, 3))
print('\nSum of the array:\n', randomArray.sum())

print('\nMinimum element in a array:\n', randomArray.min())

print('\nMaximum element in a array:\n', randomArray.max())

# By default, these operations apply to the array as though it were a list of numbers,
# regardless of its shape. However,
# by specifying the `axis` parameter you can apply an operation along the specified axis of an array

b3 = np.arange(12).reshape(3, 4)

print('\n Array used to apply sum, min, cumsum:\n', b3)

# axis-0 means column, axis-1 means - row
# sum of each column
print('\nSum of elements in axis-0:\n', b3.sum(axis=0))

# min of each row
print('\nMimimum of each row:\n', b3.min(axis=1))

# cumulative sum along each row
print('\nCumilative sum along each row:\n',  b3.cumsum(axis=0))

# Indexing, Slicing and Iterating
# One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences.
a3 = np.arange(10)**3
print('\nArray a3:\n', a3)

print('\nAccessing Array with index:\n', a3[2])
print('\nArray slicinng:\n', a3[2:5])
# equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
a3[:6:2] = -1000

print('\nAfter manipulating a3:\n', a3)

print('\nReversed a3:\n', a3[::-1])

# Multidimensional arrays can have 'one index per axis'. These indices are given in a tuple separated by commas


def funtion1(x, y):
    return 10*x+y


b4 = np.fromfunction(funtion1, (5, 4), dtype=int)
print('\nArray generated using fromfuntion:\n', b4)

print('\nAccessing multidimensional array with index:\n', b4[2, 3])

# each row in the second column
print('\nEach row in the second column', b4[0:5, 1])
# b[ : ,1] # equivalent to the previous example

# each column in the second and third row
print('\nEach column in the second and third row:\n', b4[1:3, :])

# a 3D array (two stacked 2D arrays)
c1 = np.array([[[0,  1,  2],
                [10, 12, 13]],
               [[100, 101, 102],
                [110, 112, 113]]])

print('\nShape of a 3D array:\n', c1.shape)

# The dots (...) represent as many colons as needed to produce a complete indexing tuple
# same as c[1,:,:] or c[1]), first row
print('\nSlicing 3D array using (...):\n', c1[1, ...])

# same as c[:,:,2]), second column
print('\nSlicing 3D array using (...):\n', c1[..., 2])

# Iterating over multidimensional arrays is done with respect to the first axis
print('\nIterating over multidimensional arrays is done with respect to the first axis:\n')
for row in b4:
    print(row)

# However, if one wants to perform an 'operation on each element' in the array,
# one can use the 'flat' attribute which is an iterator over all the elements of the array
# print('\nPrinting the array elements using flat attribute:\n')
# for element in b4.flat:
    # print(element)


# Shape manipulation
a4 = np.floor(10*np.random.random((3, 4)))
print('\nArray before manipulation:\n', a4)

# Note that the following three commands all return a modified array, but do not change the original array

# returns the array, flattened
print('\nFlattened array using ravel():\n', a4.ravel())

print('\nArray with modified shape:\n', a4.reshape(6, 2))

print('\nTransposed array:\n', a4.T)

# `ndarray.resize()` method modifies the array itself, If a dimension is given as `-1` in a reshaping operation,
# the other dimensions are automatically calculated

# Stacking together different arrays
a5 = np.floor(10*np.random.random((2, 2)))

print('\nArray-1 to stack:\n', a5)

b5 = np.floor(10*np.random.random((2, 2)))
print('\nArray-2 to stack:\n', b5)

print('\nVertical stack array-1 over array-2:\n', np.vstack((a5, b5)))

print('\nHorizontal stack array-1 before array-2:\n', np.hstack((a5, b5)))
