import numpy as np

arr = np.array([1,2,3,4,5])

print(type(arr))

# 0-D Arrays

arr = np.array(42)


print(arr)


arr = np.array([1,2,3,4,5], ndmin = 5)


print(arr)

arr = np.array([[0,0,0,0],[0,0,0,0]])

arr[1][3] = 15

print(arr[1][3])

# Data types

arr_int = np.array([1,2,3,4,5])
arr_string = np.array(['Rafael','Sasha'])

print(arr_string.dtype) # <U6
print(arr_int.dtype) # int64


arr = np.array([1,2,3,4,], dtype='S')

print(arr) # [b'1' b'2' b'3' b'4']
print(arr.dtype) # |S1

arr = np.array([1,2,3,4,], dtype='i4')

print(arr) # [1 2 3 4]
print(arr.dtype) #int32


#Converse Array, the best method exist is use the astype('')


arr = np.array([1.1,2.1,3.1])

new_arr = arr.astype('i')

print(new_arr) # [1,2,3] #Type int32

# To convert to int64 use 'int'

new_arr = arr.astype(int)   

#To convert to bool

arr = np.array([1,0,3])

new_arr = arr.astype(bool)

print(new_arr) # [ True False True]    

#arr = np.full((3,3), 1, dtype=bool)

arr = np.arange(10)

out = np.where(arr % 2 == 1, -1, arr)

print(arr)
print(out)

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr_3d:
  for y in x:
    for z in y:
      print(z)

print("-----------------------------------------")

for x in np.nditer(arr_3d):
  print(x)


new_arr = np.array([1,2,3])

for x in np.nditer(new_arr, flags=['buffered'], op_dtypes=['S']):
  print(x)


#arr = np.full((3,3), 1, dtype=bool)
arr_using_for = np.arange(1,11)

arr = np.array([[1,2,3],[4,5,6]])
ndim = np.array(['1','2','3','4','5'])
ast = arr.astype('i')
print(arr_using_for)

for i in arr:
  print(i)

print(ast.dtype)
print(ast)
#new_arr = arr.reshape(-1)
print(new_arr)
#out = np.where(arr % 2 == 1, -1, arr)

print(arr)
print(out)
