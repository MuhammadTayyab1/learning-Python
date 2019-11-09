for i in range(8):
    for j in range(40-i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print("")
    

    
for i in range(10):
    for k in reversed(range(10+i)):
        print(" ",end="")
    for j in range(30-i):
        print("*",end="")
    for m in range(30-i):
        print("*",end="")
    print("")
