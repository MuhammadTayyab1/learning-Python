arr= [-2,-1,-8,-4,-3]
max=arr[0]

for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]

print(max)