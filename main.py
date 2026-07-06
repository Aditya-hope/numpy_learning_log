
import numpy as np
print(np.__version__)

#vectorized calc

my_list=[1,2,3,4]
print(my_list*2)

array=np.array(my_list)
print(array*2)
print(type(array))



'''multidimensional array with chain and md indexing'''

array=np.array([[[1,2,3],[4,5,6],[7,8,9]],
                [[10,11,13],[13,14,15],[16,17,18]],
                [[19,20,21],[21,22,23],[24,25,26]]])


#chain indexing

print(array[0][0][1])

#
# #multidimensional indexing --faster
#
print(array[1,0,1])
#


'''slicing using numpy'''

array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

#array[start:end:step]

print(array[0:3,0:2])




'''scalar arithmetic'''
array=np.array([1,2,3])
print(array+1)
print(array-2)
print(array*3)
print(array/4)
print(array**5)


#vectorized math function

temp=np.sqrt(array)
print((np.round(temp)))
print(np.pi)


#exercise
radii=np.array([1,2,3])
print(np.pi*radii**2)


#element wise arithmetic

array1=np.array([1,2,3])
array2=np.array([4,5,6])

print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1**array2)


#comparison operators

scores=np.array([91,55,100,64,78,82])

#who scored full
print(scores==100)

#who scored passing >=60
print(scores>=60)

#who fails
print(scores<60)


scores[scores<60]=0


'''broadcasting in numpy'''

#broadcasting allows numpy to perform operations on arrays
#with different shapes by virtually expanding dimensions
#so they match the larger array's shape


#criteria for broadcast

#1.the dimension have the same size
#or
#one of the dimension has a size of 1


array1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
array2=np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])
print(array1.shape)
print(array2.shape)
print(array1*array2)

#exercise creating a multiplication table from 1 to 10

array1=np.array([[1,2,3,4,5,6,7,8,9,10]])
array2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(array1.shape)
print(array2.shape)
print(array2*array1)
