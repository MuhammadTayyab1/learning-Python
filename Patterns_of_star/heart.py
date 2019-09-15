for i in range(10):
    for j in range(10-i):
        print("  ",end="")
    for k in range(i):
        print("\033[0;31;31m*  ",end=" ")
    for l in range(2*(9-i)):
        print("  ",end="")
    for m in range(i):
        print("*  ",end=" ")
    print("")
    
for i in reversed(range(19)):
    for j in range(19-i):
        print("  ",end="")
    for k in range(i):
        print("*  ",end=" ")
    print("")
    
