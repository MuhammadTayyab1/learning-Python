for i in range(5):
    for j in range(10-i):
        print(" ",end="")
    for k in range(10+i):
        print("*",end=" ")
    print("|",end="")
    for j in range(10+i):
        print("*",end=" ")
    print("")
    
for i in range(4):
    for j in range(17):
        print("*",end=" ")
    print("|",end="")
    for k in range(20+i):
        print("* ",end="")
    print("")
    
for i in range(2):
    for j in range(10):
        print(" ",end="")
    for k in range(2):
        print("* ",end="")
    for j in range(50):
        print(" ",end="")
    for k in range(2):
        print("* ",end="")
    print("")