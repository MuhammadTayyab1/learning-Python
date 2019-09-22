import numpy as nm


arr=nm.array([[[1,2],[3,4]] , [[3,4],[5,5]]])

# array diamentions
print(arr.shape)
print(arr[0][1][0])


# resize array
a = nm.array([[1,2,3],[4,5,6]]) 
a.shape = (3,2) 
print(a)


# insert range
b = nm.arange(24)
print(b)


# Data type size 

# 8, 16, 32, 64, 128
q = nm.array([1,2,3,4,9,7], dtype=nm.int64)
print(q.itemsize)



# 
a = nm.arange(0,60,5)
a = a.reshape(3,4)

print('Original array is:')
print(a)
print('\n')

print('Modified array is:')
for x in nm.nditer(a):
   print(x)


# insert zeros
a= nm.zeros(5)
print(a)


# insert value
a= nm.insert(a,0,9)
print(a)
print(a.itemsize)


# Slicing 

a = nm.arange(10) 
s = slice(2,7,2) 
print(a[s])



# delete index

a=nm.arange(10)
a=nm.delete(a,1)
print(a)


# mathmatical operations

arr1=nm.array([191,192,193,194])
arr2=nm.array([91,92,93,94])

sum= arr1+arr2

print(sum)

multiply= arr1*arr2

print(multiply)

divide= arr1/arr2

print(divide)

sub= arr1-arr2

print(sub)