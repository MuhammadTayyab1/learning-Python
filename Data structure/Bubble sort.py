def bubblesort(arr):

    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1]= temp
    return arr


arr1=[1,9,3,7,2,5]
print(bubblesort(arr1))