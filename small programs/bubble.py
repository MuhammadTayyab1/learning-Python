def bubblesort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    



arr=[64,34,25,12,22,11,90]
print(arr)
bubblesort(arr)
print(arr)