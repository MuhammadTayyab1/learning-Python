import time
import os




def condition(h,a,b,c,d,e,f,g,h1,i,j):
    if h==0:
        print(j)
    elif h==1:
        print(a)
    elif h==2:
        print(b)
    elif h==3:
        print(c)
    elif h==4:
        print(d)
    elif h==5:
        print(e)
    elif h==6:
        print(f)
    elif h==7:
        print(g)
    elif h==8:
        print(h1)
    elif h==9:
        print(i)


        


a ="       |\n"
a+="       |\n"
a+="       |\n"
a+="       |\n"
a+="       |\n"

b ="      ____\n"
b+="          |\n"
b+="      ____|\n"
b+="     |    \n"
b+="     |____\n"

c ="      ____\n"
c+="          |\n"
c+="      ____|\n"
c+="          |\n"
c+="      ____|\n"


d ="     |    |\n"
d+="     |    |\n"
d+="     |____|\n"
d+="          |\n"
d+="          |\n"

e ="      ____\n"
e+="     |     \n"
e+="     |____\n"
e+="          |\n"
e+="     _____|\n"

f ="      ____\n"
f+="     |     \n"
f+="     |____\n"
f+="     |    |\n"
f+="     |____|\n"

g ="     _____\n"
g+="          |\n"
g+="          |\n"
g+="          |\n"
g+="          |\n"

h ="      ____\n"
h+="     |    |\n"
h+="     |____|\n"
h+="     |    |\n"
h+="     |____|\n"

i ="      ____\n"
i+="     |    |\n"
i+="     |____|\n"
i+="          |\n"
i+="          |\n"


j ="      ____\n"
j+="     |    |\n"
j+="     |    |\n"
j+="     |    |\n"
j+="     |____|\n"


for i in range(10000):
    time.sleep(1)
    os.system('cls')
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%H:%M:%S", named_tuple)

    arr=[]


    for i in range(len(time_string)):
        if time_string[i]==":":
            pass
        else:
            arr.append(time_string[i])


    h1=int(arr[0])
    condition(h1,a,b,c,d,e,f,g,h,i,j)

    h2=int(arr[1])
    condition(h2,a,b,c,d,e,f,g,h,i,j)

    print("=================")

    m1=int(arr[2])
    condition(m1,a,b,c,d,e,f,g,h,i,j)

    m2=int(arr[3])
    condition(m2,a,b,c,d,e,f,g,h,i,j)

    
    
    print("=================")

    s1=int(arr[4])
    condition(s1,a,b,c,d,e,f,g,h,i,j)

    s2=int(arr[5])
    condition(s2,a,b,c,d,e,f,g,h,i,j)


input()
