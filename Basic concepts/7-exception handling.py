import sys

try:
    val1=int(input("Enter value 1"))
    val2=int(input("Enter value 2"))
    
    division= val1/val2
    print(division)
    
except:
    print(sys.exc_info()[0])
          
else:
    print("Thanks for using")