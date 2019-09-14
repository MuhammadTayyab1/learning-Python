cs=int(input("Enter intervals = "))
count=0

for i in range(cs):
    n=int(input("Length of list = "))
    arr=list(map(int,(input("Enter value ") for i in range(n))))

    l=int(len(arr))
    for j in range(l):
        for k in range(l):
            sum = int(arr[j])+int(arr[k]) 

            if sum%4==0:
                print("(",arr[j],",",arr[k],")")
                count+=1


    print(count)


