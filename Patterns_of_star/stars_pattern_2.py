count=int(10)

for i in range(1,10):
    for j in range(1,count):
        print("*",end=" ")
    count-=1
    
    for k in range(2*i-1):
        print(" ",end=" ")
        
    for j in range(1,count):
        print("*",end=" ")
    print("")
    
count=1

for i in range(2,10):
    for j in range(count):
        print("*",end=" ")
    count+=1
    
    for k in range(2*(10-i)-1):
        print(" ",end=" ")
        
    for j in range(count):
        print("*",end=" ")
    print("")
    