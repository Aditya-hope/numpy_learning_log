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


