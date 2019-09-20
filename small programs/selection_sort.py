arr=[27,16,3,22,5,9]
print(arr)

for i in range(len(arr)):
    min=i
    for j in range(i+1,len(arr)):
        
        if arr[min] > arr[j]:
            min=j

    hold=arr[min]
    arr[min]=arr[i]
    arr[i]=hold
    
    del min
    del hold
            


print(arr)
input()

    