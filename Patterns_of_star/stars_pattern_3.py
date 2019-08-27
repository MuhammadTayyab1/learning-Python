for i in range(4):
    for j in range(4-i-1):
        print(" ",end=(" "))
    for k in range(i+1):
        print("*  ",end=(" "))
    for j in range(2*(4-i-1)):
        print(" ",end=(" "))
    for k in range(i+1):
        print("*  ",end=(" "))
    print("")
    
for i in reversed(range(8)):
    for j in range(8-i):
        print(" ",end=(" "))
    for k in reversed(range(i)):
        print("*  ",end=(" "))
    print("")