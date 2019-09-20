arr=[12,11,13,5,6]


for i in range(1,len(arr)):
    hold=arr[i]
    j=i-1

    while j>=0 and hold <arr[j]:
        arr[j+1]=arr[j]
        j-=1
    
    
    arr[j+1]=hold
    print(arr)

input()
    