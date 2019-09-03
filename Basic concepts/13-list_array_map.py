import numpy as mn

arr=list(map(int,(input() for i in range(2))))

# list to array
arr=mn.array(arr)
print(arr/2)


arr=list(arr)

# delete whole array to free the variable
del arr

# Again use of arr variable in other functions
arr=90
print(arr)