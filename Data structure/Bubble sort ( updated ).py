def bubblesort(arr):
    flag=False
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1]= temp
                flag=True
                print("Running")
        if flag==False:
            print("sorted")
            break

        
    return arr


arr1=[5,9,3,7,2,5,3,3,3,1,5]
print(bubblesort(arr1))