def binarysearch(arr,low,high,key):
    if high < low:
        return -1

    mid=int((low+high)/2)

    if key==arr[mid]:
        return mid

    if key > arr[mid]:
        return binarysearch(arr,(mid+1),high,key)

    return binarysearch (arr,(mid-1),high,key)


arr=[5,6,7,8,9,10]
n=len(arr)
key=int(10)

print("index ",int(binarysearch(arr,0,n,key)))

input()
