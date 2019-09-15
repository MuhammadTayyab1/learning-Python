for i in range(9):
    for j in range(40-i):
        print(" ",end="")
    for k in range(i+2):
        print("* ",end="")
    print("")
    
    
for i in range(7):
    for k in reversed(range(21+i)):
        print(" ",end="")
    for j in range(20-i):
        print("* ",end="")
    print("")
    
for i in reversed(range(7)):
    for k in reversed(range(21+i)):
        print(" ",end="")
    for j in range(20-i):
        print("* ",end="")
    print("")
    
for i in reversed(range(9)):
    for j in range(40-i):
        print(" ",end="")
    for k in range(i+2):
        print("* ",end="")
    print("")