
arr=[6,3,1,4,9,2]

for i in range(len(arr)):
    j=i-1
    hold=arr[i]

    while j>=0:
        if hold < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        else:
            break


    arr[j+1]=hold

print(arr)






