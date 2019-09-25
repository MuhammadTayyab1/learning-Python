def binarysearch(seq, value):
    lo=0
    hi=len(seq)-1

    while lo <= hi:
        mid= int((lo+hi)/2)

        if seq[mid] < value:
            lo=mid+1
        elif seq[mid] > value:
            lo=mid-1
        elif seq[mid]==value:
            return mid


arr=[2,3,8,9]
data=binarysearch(arr,9)
print(arr[data],"   ",data)
