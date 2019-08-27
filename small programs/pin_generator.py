import random

try:
    
    length= int(input("Enter length of pin"))
    level= int(input("Difficulty level\n press 1 for hard\n press 2 for medium \n press 3 for easy"))
    
    
    save = ""

    if level==1:
        for i in range(length):
            save += str(random.randint(1,10))
    
    
    elif level==2:
        for i in range(length):
            save += str(random.randint(1,7))
    
    
    elif level==3:
        for i in range(length):
            save += str(random.randint(1,5))
    
    else:
        print("wrong input")
    
    
    print(save)
    
except:
    
    print("Kindly give your input in correct format")

else:
    print("Thanks for using our services")