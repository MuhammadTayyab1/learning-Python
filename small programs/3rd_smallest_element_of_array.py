arr=[9,4,5,2,3,7,8,4,90]

k=int(input(""))

for i in range(len(arr)):
    for j in range(i):
        if arr[j] > arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp


print(arr)
print(arr[k-1])