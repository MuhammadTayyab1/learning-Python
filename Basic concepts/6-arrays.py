# string array
cars = ["Ford", "Volvo", "BMW"]

for x in range(3):
    print(cars[x])



# Or 
cars = ["Ford", "Volvo", "BMW"]

for x in cars:
    print(x)



# Adding, removing in arrays
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")

for y in cars:
    print(y)

print("============================")

cars.remove("Ford")
for y in cars:
    print(y)


# 2d array/list

arr=[[90,98],[77,90],[99,89],[95,94]]

print(arr)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print("i=",i,"  j=",j,"    value",arr[i][j])
        
        
    
        
        
        
# Add remove in multidimensional 
arr=[(10,99),(20,90)]
print(arr)

arr.append((90,90))
print(arr)

arr.pop(0)
print(arr)

arr.remove((20,90))
print(arr)



# List Comprehension
lis= [i for i in range(10)]


print(lis)
