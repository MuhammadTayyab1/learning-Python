# while loop structure
i=0
while i < 6:
    print(i)
    i+=1


# while with else
i=0
while i < 6:
    print(i)
    i+=1
else:
	print("now i is greator then 6")


# while with condition 
i=0
while i < 6:
    i+=1
    if i==3:
        continue
    else:
        print(i)
    


# Break or continue
i=0
while i < 6:
    i+=1
    if i==3:
        break
    else:
        print(i)
        continue
    
