def myclass(a,b):
    print("new project",a,b)



myclass(100,"ok")
myclass(87,"done")




# using return

def myclass(a,b):
    return ("new project",a,b)

# due to different data type it return a obj 
q=myclass(100,"ok")
w=myclass(87,"done")

# breaking obj into variables
for i in q:
    print(i)





# classes

class student():
    name="ali"
    id="90"
    
    def s1():
        print("ok")
        
        
student.s1()
print(student.name)

student.name="zubair"
print(student.name)







# Constructor

class car(object):
    wheel=4
    
    def __init__(a,name,num):
        a.name=name
        a.num=num
        print(a.name)
        print(a.num)
        
hold= car("ali",90)
print(hold.wheel)
print(car.wheel)
