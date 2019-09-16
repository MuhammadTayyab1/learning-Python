num={
    1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninty",100:"hundered"}



count=0
arr=[]

for i in range(10):
    for j in range(i):
        print(j+1,end=" ")
        arr.append(j+1)


    for k in range(10,i,-1):
        if k==10:
            print("+ ",end="")
            arr.append(99)

        else:
            print(k,end=" ")
            arr.append(k)



    for p in range(len(arr)):
        if arr[p]==99:
            count+=p
        else:
            count+=arr[p]
    if arr[5]==99:
        count+=0
    else:
        count+=arr[5]
    
    
    print("  =  ",count,"  ====>  ",end="")
    try:
        print(num[count-count%10],"",num[count%10],end="")
    except:
        print(num[count],end="")
    count=0
    arr.clear()
    print("")




    
